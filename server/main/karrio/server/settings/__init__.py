__path__ = __import__("pkgutil").extend_path(__path__, __name__)  # type: ignore

import importlib.util
from karrio.server.settings.base import *
from karrio.server.settings.email import *
from karrio.server.settings.constance import *
from karrio.server.settings.workers import *
from karrio.server.settings.cache import *


if importlib.util.find_spec("karrio.server.iam") is not None:
    from karrio.server.settings.iam import *


if importlib.util.find_spec("karrio.server.graph") is not None:
    from karrio.server.settings.graph import *


if importlib.util.find_spec("karrio.server.orders") is not None:
    from karrio.server.settings.orders import *


if importlib.util.find_spec("karrio.server.orgs") is not None:
    from karrio.server.settings.orgs import *


""" Warning:: This section need to be last for settings extensibility """
if MULTI_TENANTS:
    from karrio.server.settings.tenants import *

if importlib.util.find_spec("karrio.server.settings.main") is not None:
    from karrio.server.settings.main import *
