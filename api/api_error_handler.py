from functools import wraps

import logging

logger = logging.getLogger(__name__)


def api_error_handler(func):
    """
    Decorator to catch all exceptions from Flask endpoints and return them as JSON errors.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            logger.error(f"Error processing request: {exc}")
            return {'error': 'Internal server error'}, 500

    return wrapper
