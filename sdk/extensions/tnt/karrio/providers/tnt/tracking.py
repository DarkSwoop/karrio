import karrio.schemas.tnt.tracking_request as tnt
import karrio.schemas.tnt.tracking_response as tracking
import typing
import karrio.lib as lib
import karrio.core.models as models
import karrio.providers.tnt.error as provider_error
import karrio.providers.tnt.utils as provider_utils
import karrio.providers.tnt.units as provider_units


def parse_tracking_response(
    _response: lib.Deserializable[dict],
    settings: provider_utils.Settings,
) -> typing.Tuple[typing.List[models.TrackingDetails], typing.List[models.Message]]:
    response = _response.deserialize()
    details = lib.find_element("Consignment", response)
    tracking_details = [_extract_detail(node, settings) for node in details]

    return tracking_details, provider_error.parse_error_response(response, settings)


def _extract_detail(
    node: dict, settings: provider_utils.Settings
) -> models.TrackingDetails:
    detail: typing.Any = None
    events: list = []

    return models.TrackingDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        tracking_number=detail.ConsignmentNumber,
        events=[
            models.TrackingEvent(
                # date=DF.fdate(status.LocalEventDate.valueOf_, "%Y%m%d"),
                # description=status.StatusDescription,
                # location=SF.concat_str(
                #     status.Depot, status.DepotName, join=True, separator="-"
                # ),
                # code=status.StatusCode,
                # time=DF.ftime(status.LocalEventTime.valueOf_, "%H%M"),
            )
            for status in events
        ],
        delivered=(detail.SummaryCode == "DEL"),
    )


def tracking_request(
    payload: models.TrackingRequest, settings: provider_utils.Settings
) -> lib.Serializable:
    request = tnt.TrackRequestType(
        locale="en_US",
        version="3.1",
        SearchCriteria=tnt.SearchCriteriaType(
            marketType="INTERNATIONAL",
            originCountry=(settings.account_country_code or "US"),
            ConsignmentNumber=payload.tracking_numbers,
        ),
        LevelOfDetail=tnt.LevelOfDetailType(
            Complete=tnt.CompleteType(
                originAddress=True,
                destinationAddress=True,
            )
        ),
    )

    return lib.Serializable(request, lib.to_dict)
