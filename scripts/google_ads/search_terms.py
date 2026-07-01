"""List Google Ads search term performance for a date range.

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
        description="List read-only Google Ads search term performance."
    )
    parser.add_argument("--start", required=True, help="Start date, YYYY-MM-DD.")
    parser.add_argument("--end", required=True, help="End date, YYYY-MM-DD.")
    return parser.parse_args()


def validate_date(value: str, label: str) -> None:
    if not DATE_PATTERN.match(value):
        raise ValueError(f"{label} must use YYYY-MM-DD format: {value}")


def micros_to_currency(value: int) -> str:
    return str((Decimal(value) / Decimal("1000000")).quantize(Decimal("0.01")))


def ratio_to_percent(value: float) -> str:
    return f"{Decimal(str(value)) * Decimal('100'):.2f}%"


def decimal_to_two_places(value: float) -> str:
    return f"{Decimal(str(value)):.2f}"


def build_query(start: str, end: str) -> str:
    return f"""
        SELECT
          campaign.id,
          campaign.name,
          ad_group.id,
          ad_group.name,
          search_term_view.search_term,
          segments.keyword.info.text,
          segments.keyword.info.match_type,
          metrics.impressions,
          metrics.clicks,
          metrics.ctr,
          metrics.average_cpc,
          metrics.cost_micros,
          metrics.conversions,
          metrics.all_conversions
        FROM search_term_view
        WHERE segments.date BETWEEN '{start}' AND '{end}'
          AND campaign.advertising_channel_type = 'SEARCH'
        ORDER BY metrics.cost_micros DESC
    """


def list_search_terms(start: str, end: str) -> None:
    client = get_google_ads_client()
    customer_id = get_customer_id()
    service = client.get_service("GoogleAdsService")
    stream = service.search_stream(customer_id=customer_id, query=build_query(start, end))

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(
        (
            "campaign_id",
            "campaign_name",
            "ad_group_id",
            "ad_group_name",
            "search_term",
            "keyword_text",
            "keyword_match_type",
            "impressions",
            "clicks",
            "ctr",
            "average_cpc_cost",
            "cost",
            "conversions",
            "all_conversions",
        )
    )

    for batch in stream:
        for row in batch.results:
            writer.writerow(
                (
                    row.campaign.id,
                    row.campaign.name,
                    row.ad_group.id,
                    row.ad_group.name,
                    row.search_term_view.search_term,
                    row.segments.keyword.info.text,
                    row.segments.keyword.info.match_type.name,
                    row.metrics.impressions,
                    row.metrics.clicks,
                    ratio_to_percent(row.metrics.ctr),
                    micros_to_currency(row.metrics.average_cpc),
                    micros_to_currency(row.metrics.cost_micros),
                    decimal_to_two_places(row.metrics.conversions),
                    decimal_to_two_places(row.metrics.all_conversions),
                )
            )


def main() -> int:
    args = parse_args()

    try:
        validate_date(args.start, "--start")
        validate_date(args.end, "--end")
        list_search_terms(args.start, args.end)
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
