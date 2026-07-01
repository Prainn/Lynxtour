"""List Google Ads conversion action performance for a date range.

This integration is read-only: it only runs a GAQL reporting query through
GoogleAdsService search_stream.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from decimal import Decimal

from google_ads_client import get_customer_id, get_google_ads_client


DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List read-only Google Ads conversion action performance."
    )
    parser.add_argument("--start", required=True, help="Start date, YYYY-MM-DD.")
    parser.add_argument("--end", required=True, help="End date, YYYY-MM-DD.")
    return parser.parse_args()


def validate_date(value: str, label: str) -> None:
    if not DATE_PATTERN.match(value):
        raise ValueError(f"{label} must use YYYY-MM-DD format: {value}")


def decimal_to_two_places(value: float) -> str:
    return f"{Decimal(str(value)):.2f}"


def conversion_action_id(resource_name: str) -> str:
    return resource_name.rsplit("/", 1)[-1] if resource_name else ""


def build_query(start: str, end: str) -> str:
    return f"""
        SELECT
          campaign.id,
          campaign.name,
          segments.conversion_action,
          segments.conversion_action_name,
          metrics.conversions,
          metrics.all_conversions,
          metrics.conversions_value
        FROM campaign
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        ORDER BY campaign.id, segments.conversion_action_name
    """


def list_conversion_action_performance(start: str, end: str) -> None:
    client = get_google_ads_client()
    customer_id = get_customer_id()
    service = client.get_service("GoogleAdsService")
    stream = service.search_stream(customer_id=customer_id, query=build_query(start, end))

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(
        (
            "campaign_id",
            "campaign_name",
            "conversion_action_id",
            "conversion_action_name",
            "conversions",
            "all_conversions",
            "conversion_value",
            "cost",
        )
    )

    for batch in stream:
        for row in batch.results:
            writer.writerow(
                (
                    row.campaign.id,
                    row.campaign.name,
                    conversion_action_id(row.segments.conversion_action),
                    row.segments.conversion_action_name,
                    decimal_to_two_places(row.metrics.conversions),
                    decimal_to_two_places(row.metrics.all_conversions),
                    decimal_to_two_places(row.metrics.conversions_value),
                    # metrics.cost_micros is not supported with conversion
                    # action segments, so cost is intentionally blank.
                    "",
                )
            )


def main() -> int:
    args = parse_args()

    try:
        validate_date(args.start, "--start")
        validate_date(args.end, "--end")
        list_conversion_action_performance(args.start, args.end)
    except (RuntimeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        if exc.__class__.__name__ != "GoogleAdsException":
            raise
        print(
            "Google Ads API request failed. "
            f"request_id={exc.request_id} failure={exc.failure}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
