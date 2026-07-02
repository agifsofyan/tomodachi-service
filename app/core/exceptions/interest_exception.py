from app.core.exceptions.base_exception import AppException

class InterestNotFoundException(AppException):
    def __init__(self):
        super().__init__(status_code=404, message="Interest not found")


class InterestAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(status_code=400, message="Interest with this code already exists")