from fastapi import status

from app.core.exceptions.base_exception import AppException


class UserNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="User not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )


class EmailAlreadyExistsException(AppException):

    def __init__(self):
        super().__init__(
            message="Email already exists.",
            status_code=status.HTTP_409_CONFLICT,
        )
        
class UserAlreadyExistsException(AppException):
    
    def __init__(self):
        super().__init__(
            message="User has been registered.",
            status_code=status.HTTP_409_CONFLICT,
        )