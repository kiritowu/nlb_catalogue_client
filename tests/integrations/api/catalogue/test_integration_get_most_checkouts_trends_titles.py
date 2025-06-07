from http import HTTPStatus

from nlb_catalogue_client.api.catalogue import get_get_most_checkouts_trends_titles
from nlb_catalogue_client.models.search_most_checkouts_titles_response import (
    SearchMostCheckoutsTitlesResponse,
)
from nlb_catalogue_client.models.checkouts_trend import CheckoutsTrend


def test_get_most_checkouts_trends_titles_integration_success(client):
    """Integration test for GetMostCheckoutsTrendsTitles against live NLB API."""
    response = get_get_most_checkouts_trends_titles.sync_detailed(
        client=client,
        location_code="AMKPL",
    )

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.parsed, SearchMostCheckoutsTitlesResponse)
    assert isinstance(response.parsed.checkouts_trends, list)
    for item in response.parsed.checkouts_trends:
        assert isinstance(item, CheckoutsTrend)
