from typing import Tuple, List
from purplship.core.utils import Serializable
from purplship.core.models import (
    PickupCancelRequest,
    ConfirmationDetails,
    Message
)

from purplship.providers.dicom.error import parse_error_response
from purplship.providers.dicom.utils import Settings


def parse_pickup_cancel_response(response: dict, settings: Settings) -> Tuple[ConfirmationDetails, List[Message]]:
    errors = parse_error_response(response, settings)
    details = None

    return details, errors


def pickup_cancel_request(payload: PickupCancelRequest, settings: Settings) -> Serializable:
    request = None

    return Serializable(request)
