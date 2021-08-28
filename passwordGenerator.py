from string import *
import numpy as np

class PasswordGenerator:

    def __init__(self, length):
        self.password = self.generate_password(length)

    def generate_password(self, length):
        allowed_schars = list("!()-.?[]_'~;:!@#$%^&*+=")
        characters = list(ascii_lowercase + ascii_uppercase + digits) + allowed_schars
        return ''.join([characters[np.random.randint(low=0, high=len(characters))] for _ in range(length)])


if __name__ == '__main__':
    pw = PasswordGenerator()
    print(pw.password)