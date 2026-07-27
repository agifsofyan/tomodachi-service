from fastapi import status

from app.core.exceptions.base_exception import AppException


class PasswordNotMatchException(AppException):
    def __init__(self):
        super().__init__(
            message="Password not match.",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
