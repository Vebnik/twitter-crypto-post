# libs
import os


class ApiCollections:
  # api config
  API_URL = 'https://api.binance.com/api/v3'

  # api sample
  @property
  def get_price_by_symbols(self) -> str:
    return f'{self.API_URL}/ticker/price?symbols='

  