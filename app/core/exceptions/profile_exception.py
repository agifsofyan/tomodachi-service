from fastapi import status

from app.core.exceptions.base_exception import AppException


class ProfileAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(
            message="Profile already exists",
            status_code=status.HTTP_409_CONFLICT,
        )


class ProfileNotFoundException(AppException):
    def __init__(self):
        super().__init__(
            message="Profile not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
