from fastapi import status

from app.core.exceptions.base_exception import AppException


class AddressAlreadyExistsException(AppException):

    def __init__(self):
        super().__init__(
            message="Address already exists.",
            status_code=status.HTTP_409_CONFLICT,
        )


class AddressNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Address not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )