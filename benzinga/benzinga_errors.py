class BenzingaError(Exception):

    def __init__(self, msg=None):
        self.general_message = "Something went wrong. Please again try again later"
        if msg is None:
            self.benzinga_message = self.general_message
        else:
            self.benzinga_message = msg

    def __str__(self):
        return "Error Message: %s \n" % self.benzinga_message


class TokenAuthenticationError(BenzingaError):
    pass


class AccessDeniedError(BenzingaError):
    pass


class RateLimitError(BenzingaError):
    pass


class RequestAPIEndpointError(BenzingaError):
    pass


class IncorrectParameterEntry(BenzingaError):
    pass


class URLIncorrectlyFormattedError(BenzingaError):
    pass


class MissingParameter(BenzingaError):
    pass


class ServiceUnavailableError(BenzingaError):
    pass


class PreconditionFailedError(BenzingaError):
    pass


class NotFoundError(BenzingaError):
    pass


class BadRequestError(BenzingaError):
    pass


class GatewayTimeoutError(BenzingaError):
    pass
