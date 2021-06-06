from .request_failure import MASZRequestFailure

class MASZLoginFailure(MASZRequestFailure):
    def __init__(self, message, errors=None):            
        super().__init__(message)
            
        self.message = message
        self.errors = errors
