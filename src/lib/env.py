from os import getenv


class Env:

    def __init__(self):
        self.version = getenv('VERSION', '0.0.0')
