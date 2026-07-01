"""Generate a Google Ads OAuth refresh token for local development.

Reads a Desktop App OAuth client JSON from secrets/google_ads_oauth_client.json.
Does not call the Google Ads API and does not write tokens to disk.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:  # pragma: no cover - depends on local environment
    InstalledAppFlow = None


CLIENT_SECRETS_FILE = Path("secrets/google_ads_oauth_client.json")
SCOPES = ["https://www.googleapis.com/auth/adwords"]


def main() -> int:
    if InstalledAppFlow is None:
        print(
            "Missing dependency: google-auth-oauthlib. "
            "Install it in your local environment, then rerun this helper.",
            file=sys.stderr,
        )
        return 1

    if not CLIENT_SECRETS_FILE.exists():
        print(
            f"OAuth client file not found: {CLIENT_SECRETS_FILE}",
            file=sys.stderr,
        )
        return 1

    flow = InstalledAppFlow.from_client_secrets_file(
        str(CLIENT_SECRETS_FILE),
        scopes=SCOPES,
    )

    credentials = flow.run_local_server(
        host="localhost",
        port=0,
        authorization_prompt_message=(
            "Opening a browser for Google Ads OAuth consent. "
            "If it does not open, visit this URL:\n{url}"
        ),
        success_message=(
            "Authorization complete. You can close this browser window."
        ),
        open_browser=True,
    )

    if not credentials.refresh_token:
        print(
            "No refresh token was returned. Revoke the app grant in your "
            "Google Account permissions, then rerun this helper.",
            file=sys.stderr,
        )
        return 1

    print(credentials.refresh_token)
    print()
    print("Paste the refresh token into .env.local as:")
    print("GOOGLE_ADS_REFRESH_TOKEN=<the refresh token above>")
    print()
    print("Do not commit .env.local or files under secrets/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
