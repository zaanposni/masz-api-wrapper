from .base_exception import MASZBaseException

class MASZInvalidResponse(MASZBaseException):
    def __init__(self, message, errors=None):            
        super().__init__(message)
            
        self.message = message
        self.errors = errors
