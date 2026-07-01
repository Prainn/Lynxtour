"""Local Google Ads API client setup.

This integration is read-only: it is intended only for GAQL reporting queries.
Credentials are loaded from .env.local and are never written by this module.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any


ENV_FILE = Path(".env.local")

REQUIRED_ENV_VARS = (
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
    "GOOGLE_ADS_CUSTOMER_ID",
)


def _strip_env_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def load_local_env(path: Path = ENV_FILE) -> None:
    if not path.exists():
        raise RuntimeError(
            f"Missing {path}. Add local Google Ads credentials there first."
        )

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        if key and key not in os.environ:
            os.environ[key] = _strip_env_value(value)


def require_env_vars() -> dict[str, str]:
    missing = [name for name in REQUIRED_ENV_VARS if not os.environ.get(name)]
    if missing:
        joined = ", ".join(missing)
        raise RuntimeError(f"Missing required .env.local values: {joined}")

    return {name: os.environ[name] for name in REQUIRED_ENV_VARS}


def get_google_ads_client() -> Any:
    load_local_env()
    values = require_env_vars()

    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:  # pragma: no cover - depends on local environment
        raise RuntimeError(
            "Missing dependency: google-ads. Install the official google-ads "
            "Python package in your local environment."
        ) from exc

    config = {
        "developer_token": values["GOOGLE_ADS_DEVELOPER_TOKEN"],
        "client_id": values["GOOGLE_ADS_CLIENT_ID"],
        "client_secret": values["GOOGLE_ADS_CLIENT_SECRET"],
        "refresh_token": values["GOOGLE_ADS_REFRESH_TOKEN"],
        "use_proto_plus": True,
    }

    login_customer_id = os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "").strip()
    if login_customer_id:
        config["login_customer_id"] = login_customer_id.replace("-", "")

    return GoogleAdsClient.load_from_dict(config)


def get_customer_id() -> str:
    load_local_env()
    values = require_env_vars()
    return values["GOOGLE_ADS_CUSTOMER_ID"].replace("-", "")
