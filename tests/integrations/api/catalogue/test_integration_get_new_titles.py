from http import HTTPStatus

from nlb_catalogue_client.api.catalogue import get_get_new_titles
from nlb_catalogue_client.models.search_new_titles_response_v2 import SearchNewTitlesResponseV2


def test_get_new_titles_integration_success(client):
    """Integration test for GetNewTitles against live NLB API."""
    response = get_get_new_titles.sync_detailed(client=client)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.parsed, SearchNewTitlesResponseV2)
    assert isinstance(response.parsed.total_records, int)
    assert response.parsed.total_records >= 0
    assert isinstance(response.parsed.titles, list)
