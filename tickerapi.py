from abc import ABC, abstractmethod
import datetime
from pandas import DataFrame
from yahooquery import Ticker


class tickerAPI(ABC):
    
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker + ".SA"
        self.base = Ticker(self.ticker)

    @abstractmethod
    def get_data(self, *args, **kwargs) -> None:
        pass  

    
class summary_details(tickerAPI):
    def get_data(self, *args, **kwargs) -> dict:
        return (self.base.summary_detail)

class get_anual_income(tickerAPI):
    def get_data(self, *args, **kwargs) -> DataFrame:
        return (self.base.income_statement('a').reset_index().set_index(['symbol','asOfDate','periodType','currencyCode']))

class get_quarter_income(tickerAPI):
    def get_data(self, *args, **kwargs) -> DataFrame:
        return (self.base.income_statement('q').reset_index().set_index(['symbol','asOfDate','periodType','currencyCode']))


class history_max(tickerAPI):

    def get_data(self, **kwargs) -> DataFrame:
        return self.base.history(period='max')

class history_date_interval(tickerAPI):

    def get_data(self, start :datetime.date, end :datetime.date) -> DataFrame:
        return self.base.history(start=start, end=end)

class history_period_interval(tickerAPI):

    def get_data(self, period:str, interval:str ) -> DataFrame:
        return self.base.history(period=period, interval=interval)
