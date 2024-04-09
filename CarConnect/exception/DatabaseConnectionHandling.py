class DatabaseConnectionError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DatabaseQueryError(Exception):

    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

