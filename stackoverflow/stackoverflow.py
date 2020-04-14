import requests

STACKOVERFLOW_SITE = 'stackoverflow.com'
NO_CONTENT_MESSAGE = 'there is no content for this response'
OK_CODES = [200, 201, 202]

class ApiResponseError(Exception):
    def __init__(self, message):
        self.message = message

class ApiRequest:
    """ Classs to interact with stack overflow api
    """
    _base_url = 'https://api.stackexchange.com'
    _service = 'search'
    _resource = 'advanced'
    _method = 'get'

    def __init__(self, params):
        self._params = params

    @property
    def _url(self):
        return f'{self._base_url}/{self._service}/{self._resource}'

    def send(self):
        response = requests.request(self._method, self._url,
                params=self._params)

        return ApiResponse(response.status_code, response.json())

class ApiResponse:
    _http_status_code = None
    _body = None

    def __init__(self, http_status_code, content):
        self._http_status_code = http_status_code
        self._body = content

    @property
    def body(self):
        if  self._http_status_code not in OK_CODES:
            raise ApiResponseError(NO_CONTENT_MESSAGE)

        return self._body.get('items', [])

class StackOverFlow:
    def search(self, text=None):
        params = {'site': STACKOVERFLOW_SITE, 'q': text}
        response = ApiRequest(params).send()

        return [Question(**i) for i in response.body]

class Question:
    def __init__(self, title=None, score=None, link=None, **kwargs):
        self.title = title
        self.score = score
        self.link = link
        self.others = kwargs
