from .base_exception import AppException

from .profile_exception import (
    ProfileAlreadyExistsException,
    ProfileNotFoundException,
)

from .user_exception import (
    UserNotFoundException,
    EmailAlreadyExistsException,
)

from .interest_exception import (
    InterestNotFoundException,
    InterestsNotFoundException,
    InterestAlreadyExistsException,
)

from .address_exception import (
    AddressNotFoundException,
    AddressAlreadyExistsException,
)

__all__ = [
    "AppException",
    "ProfileAlreadyExistsException",
    "ProfileNotFoundException",
    "UserNotFoundException",
    "EmailAlreadyExistsException",
    "InterestNotFoundException",
    "InterestsNotFoundException",
    "InterestAlreadyExistsException",
    "AddressNotFoundException",
    "AddressAlreadyExistsException",
]