from http import HTTPStatus

from nlb_catalogue_client.api.catalogue import get_get_availability_info
from nlb_catalogue_client.models.get_availability_info_response_v2 import GetAvailabilityInfoResponseV2


def test_get_availability_info_integration_success(client, brn):
    """Integration test for GetAvailabilityInfo against live NLB API."""
    response = get_get_availability_info.sync_detailed(client=client, brn=brn)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.parsed, GetAvailabilityInfoResponseV2)
    assert isinstance(response.parsed.total_records, int)
    assert response.parsed.total_records >= 0
    assert response.parsed.items is not None
