from fastapi import status

from app.core.exceptions.base_exception import AppException


class ExternalServiceException(AppException):
    def __init__(self, message: str):
        self.status_code = status.HTTP_502_BAD_GATEWAY
        self.message = message


class RegionNotFoundException(AppException):
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            message=message,
        )
