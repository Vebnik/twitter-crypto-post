

class Crypto:
  __slots__ = ('symbol', 'price')

  def __init__(self, config: dict) -> None:
    self.symbol: str = config.get('symbol')
    self.price: str = config.get('price')

  def __repr__(self) -> str:
    return f'{self.symbol}: {self.price}'

  def __str__(self) -> str:
    symbol = f'{self.symbol} ➜'
    price = round(float(self.price), 2)

    return f'💰 {symbol} {price}'


class CryptoStore:

  __slots__ = ('currency_list',)

  def __init__(self, currency_list: list[dict]) -> None:
    self.currency_list = [Crypto(item) for item in currency_list]

  def __repr__(self) -> str:
    return str(self.currency_list)

  def get_pretty_str(self) -> str:
    return '\n'.join(map(str, self.currency_list))
