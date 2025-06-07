"""Integration test fixtures: load .env and provide api_key, app_id, brn, and client fixtures."""

import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def api_key():
    """Return NLB API key from environment, skip if missing."""
    key = os.environ.get("NLB_API_KEY")
    if not key:
        pytest.skip("NLB_API_KEY not found; skipping integration tests")
    return key


@pytest.fixture(scope="session")
def app_id():
    """Return NLB App ID from environment, skip if missing."""
    app = os.environ.get("NLB_APP_ID")
    if not app:
        pytest.skip("NLB_APP_ID not found; skipping integration tests")
    return app


@pytest.fixture(scope="session")
def brn():
    """Return BRN (Bibliographic Record Number) from environment, skip if missing or invalid."""
    brn_str = os.environ.get("NLB_BRN")
    if not brn_str:
        pytest.skip("NLB_BRN not found; skipping integration tests")
    try:
        return int(brn_str)
    except ValueError:
        pytest.skip("NLB_BRN is not an integer; skipping integration tests")


@pytest.fixture(scope="session")
def client(api_key, app_id):
    """Return an AuthenticatedClient configured for integration testing."""
    from nlb_catalogue_client.client import AuthenticatedClient

    return AuthenticatedClient(
        base_url="https://openweb.nlb.gov.sg/api/v2/Catalogue/",
        auth_header_name="X-API-KEY",
        token=api_key,
        prefix="",
        headers={"X-APP-Code": app_id},
        raise_on_unexpected_status=True,
    )
