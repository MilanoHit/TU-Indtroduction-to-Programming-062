class InvalidCommand(Exception):
    def __init__(self, message, *args : object) -> None:
        message = "Please enter a viable option"
        super().__init__(message, *args)

class InvalidDataFormat(Exception):
    def __init__(self, message, *args : object) -> None:
        message = "Please enter valid data"
        super().__init__(message, *args)

        
class CharacterExists(Exception):
    def __init__(self, message, *args : object) -> None:
        message = "This character already exists"
        super().__init__(message, *args)

class InvalidCharacterClass(Exception):
    def __init__(self, message, *args : object) -> None:
        message = "Please enter a valid character class"
        super().__init__(message, *args)

class CharacterNotFound(Exception):
    def __init__(self, message, *args : object) -> None:
        message = "This character doesn't exist"
        super().__init__(message, *args)
        
