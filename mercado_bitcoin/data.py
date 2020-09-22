import time
import requests


class BaseRequest:
    base_path = "https://www.mercadobitcoin.net/api"
    method = ""

    def __init__(self, coin="BTC"):
        self.coin = coin

    def _path(self):
        return '/'.join([self.base_path, self.coin, self.method])

    def get(self):
        response = requests.get(self._path())
        return response.json()


class Ticker(BaseRequest):
    method = "ticker"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class OrderBook(BaseRequest):
    method = "orderbook"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Trades(BaseRequest):
    method = "trades"

    def __init__(self, tid=None, from_date="", to_date="", **kwargs):
        super().__init__(**kwargs)

    def get_tid(self, tid=time.time()):
        response = requests.get("/".join([self._path(), tid]))
        return response.json()

    def get_from_date(self, from_date):
        response = requests.get("/".join([self._path, from_date]))
        return response.json()

    def get_from_date_to_date(self, from_date, to_date):
        response = requests.get("/".join([self._path, from_date, to_date]))
        return response.json()


class DaySummary(BaseRequest):
    method = "day-summary"

    def __init__(self, year, month, day, **kwargs):
        super().__init__(**kwargs)
        self.year = str(year)
        self.month = str(month)
        self.day = str(day)

    def get(self):
        response = requests.get("/".join([self._path(), self.year, self.month, self.day]))
        return response.json()


def main():
    coin = "BTC"
    ticker = Ticker(coin=coin)
    assert ticker.coin == coin
    assert ticker.method == 'ticker'
    assert ticker._path() == f"https://www.mercadobitcoin.net/api/{coin}/ticker"
    # print(f"{ticker.get()}")

    # orderbook = OrderBook(coin="BTC")
    # print(orderbook.coin, orderbook.method, orderbook._path())
    # print(f"{orderbook.get()}")

    # trades = Trades(coin="LTC")
    # print(trades._path(), trades.coin, trades.method)
    # print(trades.get())
    # print(trades.get_tid())
    # print(trades.get_from_date(from_date="111111111"))
    # print(trades.get_from_date_to_date(from_date="11111111", to_date="111111111"))

    # day_summary = DaySummary(coin='BTC', year=2020, month=7, day=6)
    # print(day_summary._path(), day_summary.coin, day_summary.method)
    # print(day_summary.year, day_summary.month, day_summary.day)
    # print(day_summary.get())

    # print(str(int(time.time() * 1000000)))

if __name__ == '__main__':
    main()
