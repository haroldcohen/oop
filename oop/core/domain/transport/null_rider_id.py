from uuid import UUID


class NullRiderId(UUID):

    def __init__(self):
        super().__init__("00000000-0000-0000-0000-000000000000")
