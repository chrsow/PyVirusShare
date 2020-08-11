import requests
from pathlib import Path

_API_ENDPOINT = 'https://virusshare.com/apiv2'
# _RATE_LIMIT = 4

class APIError(Exception):
    """Raised when there is any error from the API."""
    pass

class VirusShare:
    """Client for interacting with VirusShare.
    :param api_key: VirusShare API key.
    """
    # :param rateLimit: A rate limit for request per minute.

    def __init__(self, api_key: str):#, rateLimit: int):    
        if not isinstance(api_key, str):
            raise ValueError('API can only be a string.')
        if not api_key:
            raise ValueError('Please specify API key.')
        
        self.endpoint = _API_ENDPOINT
        self.api_key = api_key
        # self.rateLimit = rateLimit or _RATE_LIMIT

    def _request(self, req_path: str, hash_str: str) -> dict:
        payload = {'apikey': self.api_key, 'hash': hash_str}
        try:
            resp = requests.get(self.endpoint + req_path, params=payload)
            status_code = resp.status_code
            if status_code == 204:
                raise APIError('GET {}, {} {}'.format(req_path, status_code, 'Request rate limit exceeded.'))
            elif status_code == 400:
                raise APIError('GET {}, {} {}'.format(req_path, status_code, 'Bad request.'))
            elif status_code == 403:
                raise APIError('GET {}, {} {}'.format(req_path, status_code, 'Forbidden.'))
            elif status_code == 404:
                raise APIError('GET {}, {} {}'.format(req_path, status_code, 'Not found.'))
            elif status_code == 500:
                raise APIError('GET {}, {} {}'.format(req_path, status_code, 'Internal server error.'))
            elif status_code == 503:
                raise APIError('GET {}, {} {}'.format(req_path, status_code, 'Service unavailable.'))
            else:
                return resp
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def info(self, hash_str: str) -> dict:
        result = self._request('/file', hash_str)
        return {'data': result.json()}

    def download(self, hash_str: str, dest: str):
        result = self._request('/download', hash_str)
        
        dest_folder = Path(dest)
        with open(dest_folder / ('VirusShare_%s.zip' % hash_str) , 'wb') as f:
            f.write(result.content)

    def quick(self, hash_str: str) -> dict:
        result = self._request('/file', hash_str)
        return {'data': result.json()}

    def source(self, hash_str: str) -> dict:
        result = self._request('/file', hash_str)
        return {'data': result.json()}

