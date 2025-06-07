from http import HTTPStatus

from nlb_catalogue_client.api.catalogue import get_search_titles
from nlb_catalogue_client.models.search_titles_response_v2 import SearchTitlesResponseV2
from nlb_catalogue_client.client import AuthenticatedClient


def test_search_titles_integration_success(client: AuthenticatedClient):
    """Integration test for SearchTitles against live NLB API."""
    response = get_search_titles.sync_detailed(client=client, keywords="science")

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.parsed, SearchTitlesResponseV2)
    assert isinstance(response.parsed.total_records, int)
    assert response.parsed.total_records >= 0
    assert isinstance(response.parsed.titles, list)
    assert isinstance(response.parsed.facets, list)
