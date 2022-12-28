# libs
import json


class Utils:

  @staticmethod
  def url_prettier(crypto_list: list[str]) -> str:

    del_brackets_left = lambda el: el.replace('[', '%5B')
    del_brackets_right = lambda el: el.replace(']', '%5D')
    del_quote = lambda el: el.replace('"', '%22')
    del_space = lambda el: el.replace(' ', '')

    string_data = json.dumps(crypto_list)

    for replace_func in [del_brackets_left, del_brackets_right, del_quote, del_space]:
      string_data = replace_func(string_data)
    return string_data