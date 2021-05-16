# This implementation is copied from pythons requests
# module requests.exceptions
class DomainException(Exception):
    def __init__(self, *args, **kwargs):
        response = kwargs.pop("response", None)
        self.response = response
        self.request = kwargs.pop("request", None)
        if response is not None and not self.request and hasattr(response, "request"):
            self.request = self.response.request
        super(DomainException, self).__init__(*args, **kwargs)
