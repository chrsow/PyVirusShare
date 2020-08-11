import requests

_API_ENDPOINT = 'https://virusshare.com/apiv2'
# _RATE_LIMIT = 4

class VirusShare:
    """Client for interacting with VirusShare.
    :param apikey: VirusShare API key.
    """
    # :param rateLimit: A rate limit for request per minute.

    def __init__(self, apiKey: str):#, rateLimit: int):
        
        if not isinstance(apikey, str):
            raise ValueError('API can only be a string.')
        if not apikey:
            raise ValueError('Please specify API key.')
        
        self.endpoint = _API_ENDPOINT
        self.apiKey = apikey
        # self.rateLimit = rateLimit or _RATE_LIMIT

    def _request(self, req_path: str) -> dict:
        try:
            resp = requests.get(self.endpoint + req_path)
            status_code = resp.status_code
            if status_code == 204:
                raise ApiError('GET /{}, {} {}'.format(source, status_code, 'Request rate limit exceeded.'))
            elif status_code == 400:
                raise ApiError('GET /{}, {} {}'.format(source, status_code, 'Bad request.'))
            elif status_code == 403:
                raise ApiError('GET /{}, {} {}'.format(source, status_code, 'Forbidden.'))
            elif status_code == 404:
                raise ApiError('GET /{}, {} {}'.format(source, status_code, 'Not found.'))
            elif status_code == 500:
                raise ApiError('GET /{}, {} {}'.format(source, status_code, 'Internal server error.'))
            elif status_code == 503:
                raise ApiError('GET /{}, {} {}'.format(source, status_code, 'Service unavailable.'))
            else: 
                result = {'data': resp.json()}
                return result
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def get_info(self, hash_str: str) -> dict:
        result = self._request(hash_str)
        return result

    def download(self, hash_str: str) -> dict:
        result = self._request(hash_str)
        return result

    def quick(self, hash_str: str) -> dict:
        result = self._request(hash_str)
        return result

    def source(self, hash_str: str) -> dict:
        result = self._request(hash_str)
        return result

