# libs
import requests as req
from requests import Response, RequestException


class HttpClient:

  __slots__ = ('http_config')

  def __init__(self) -> None:
    self.http_config = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
      'Content-Type': 'application/json'
    }

  def get() -> None:
    pass
  
  def post(self, url: str, headers: dict, payload: dict) -> None|Response:
    try:
      self.http_config.update(headers)
      response = req.post(url, json=payload, headers=self.http_config)

      if response.status_code > 300:
        raise RequestException(f'Error in post request | Code: {response.status_code}')

      return response.json()
    except Exception as ex:
      print(ex); return False