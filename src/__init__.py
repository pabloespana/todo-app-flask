import os
from typing import TypeVar, Optional
from dotenv import load_dotenv

_T = TypeVar("_T")


def get_env_var(key: str, default: Optional[_T] = None) -> str | _T:
    """Method to access to an envirmoment variable"""
    load_dotenv()
    if os.getenv(key) is None and default is None:
        raise Exception(  # pylint: disable=W0719
            f"`{key}` environment variable is not set"
        )
    if os.getenv(key) is not None:
        return str(os.getenv(key))
    return str(os.getenv(key, default))
