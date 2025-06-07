from http import HTTPStatus

from nlb_catalogue_client.api.catalogue import get_get_title_details
from nlb_catalogue_client.models.get_title_details_response_v2 import GetTitleDetailsResponseV2


def test_get_title_details_integration_success(client, brn):
    """Integration test for GetTitleDetails against live NLB API."""
    response = get_get_title_details.sync_detailed(client=client, brn=brn)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.parsed, GetTitleDetailsResponseV2)
    assert response.parsed.brn == brn
    assert isinstance(response.parsed.title, str)
