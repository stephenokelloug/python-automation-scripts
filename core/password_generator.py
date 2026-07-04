import random

class PasswordGenerator:
    @staticmethod
    def generate(length: int = 4) -> str:
        # Generate a random numeric password of given length
        return ''.join(random.choices("0123456789", k=length))
