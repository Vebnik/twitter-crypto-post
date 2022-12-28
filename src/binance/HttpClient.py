# libs
import requests as req
from requests import Response, RequestException


class HttpClient:

  __slots__ = ('http_config')

  def __init__(self) -> None:
    self.http_config = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
    }

  def get(self, url: str) -> bool|Response:
    try:
      response = req.get(url, headers=self.http_config, allow_redirects=True)

      if response.status_code > 300:
        raise RequestException(f'Error in get requests | Code {response.status_code}')

      return response.json()
    except Exception as ex:
      print(ex); return False