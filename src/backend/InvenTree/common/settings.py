"""User-configurable settings for the common app."""

import logging

from django.conf import settings
from django.core.cache import cache

from moneyed import CURRENCIES

logger = logging.getLogger('inventree')


def currency_code_default():
    """Returns the default currency code (or USD if not specified)."""
    from common.models import InvenTreeSetting

    try:
        cached_value = cache.get('currency_code_default', '')
    except Exception:
        cached_value = None

    if cached_value:
        return cached_value

    try:
        code = InvenTreeSetting.get_setting(
            'INVENTREE_DEFAULT_CURRENCY', backup_value='', create=True, cache=True
        )
    except Exception:  # pragma: no cover
        # Database may not yet be ready, no need to throw an error here
        code = ''

    if code not in CURRENCIES:
        code = 'USD'  # pragma: no cover

    # Cache the value for a short amount of time
    try:
        cache.set('currency_code_default', code, 30)
    except Exception:
        pass

    return code


def all_currency_codes():
    """Returns a list of all currency codes."""
    return [(a, CURRENCIES[a].name) for a in CURRENCIES]


def currency_code_mappings():
    """Returns the current currency choices."""
    return [(a, CURRENCIES[a].name) for a in settings.CURRENCIES]


def currency_codes():
    """Returns the current currency codes."""
    return list(settings.CURRENCIES)


def stock_expiry_enabled():
    """Returns True if the stock expiry feature is enabled."""
    from common.models import InvenTreeSetting

    return InvenTreeSetting.get_setting('STOCK_ENABLE_EXPIRY', False, create=False)


def prevent_build_output_complete_on_incompleted_tests():
    """Returns True if the completion of the build outputs is disabled until the required tests are passed."""
    from common.models import InvenTreeSetting

    return InvenTreeSetting.get_setting(
        'PREVENT_BUILD_COMPLETION_HAVING_INCOMPLETED_TESTS', False, create=False
    )
