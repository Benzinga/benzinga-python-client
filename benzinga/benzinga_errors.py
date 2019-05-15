class API_Endpoint_Error(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Incorrect_Endpoint_URL(Exception):
    pass



