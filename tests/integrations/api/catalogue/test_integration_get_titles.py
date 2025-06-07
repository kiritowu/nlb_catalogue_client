from http import HTTPStatus

from nlb_catalogue_client.api.catalogue import get_get_titles
from nlb_catalogue_client.models.get_titles_response_v2 import GetTitlesResponseV2


def test_get_titles_integration_success(client, brn):
    """Integration test for GetTitles against live NLB API."""
    response = get_get_titles.sync_detailed(client=client, keywords="python")

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.parsed, GetTitlesResponseV2)
    assert isinstance(response.parsed.total_records, int)
    assert response.parsed.total_records >= 0
    assert isinstance(response.parsed.titles, list)
