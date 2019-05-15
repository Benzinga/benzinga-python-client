class Endpoint_Request_Error(Exception):

    def __init__(self, msg = None):
        if msg == None:
            msg = "The Benzinga API Endpoint you requested did not work."


