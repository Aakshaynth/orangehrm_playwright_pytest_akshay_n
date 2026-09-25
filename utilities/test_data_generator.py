import random
import string

class TestDataGenerator:
    @staticmethod
    def generate_random_string_with_int(length: int = 5) -> str:
        """Generate a random alphanumeric string with an integer suffix."""
        # Random uppercase letters + digits
        rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        # Random integer (2–3 digits for compactness)
        rand_int = str(random.randint(10, 999))
        return rand_str + rand_int