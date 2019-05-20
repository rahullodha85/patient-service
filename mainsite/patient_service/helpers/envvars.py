import os


class Env:
    def __init__(self):
        self.env_list = os.environ.copy()