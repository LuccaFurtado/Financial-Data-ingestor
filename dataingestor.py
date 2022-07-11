from abc import ABC, abstractmethod
from tickerapi import get_anual_income, get_quarter_income, history_date_interval, history_max, history_period_interval, summary_details
from datawriter import DataWriter
import datetime


class DataIngestor(ABC):
    def __init__(self, writer : DataWriter, tickers :list[str]) -> None:
        self.writer = writer
        self.tickers = tickers

    @abstractmethod
    def ingest(self) -> None:
        pass


class HistoryMaxIngestor(DataIngestor):
    def ingest(self) -> None:
        for ticker in self.tickers:
            api = history_max(ticker=ticker)
            data = api.get_data()
            self.writer(ticker=ticker, api=api.__class__.__name__).write(data)
    
class HistoryDateIntervalIngestor(DataIngestor):
    def __init__(self, writer: DataWriter, tickers:list[str],start_date : datetime.date, end_date : datetime.date) -> None:
        super().__init__(writer, tickers)
        self.start = start_date
        self.end = end_date
    def ingest(self) -> None:
        for ticker in self.tickers:
            api=history_date_interval(ticker=ticker)
            data = api.get_data(start=self.start, end=self.end)
            self.writer(ticker=ticker, api=api.__class__.__name__).write(data) 

class HistoryPeriodIntervalIngestor(DataIngestor):
    def __init__(self, writer: DataWriter, tickers: list[str] , period : str, interval : str) -> None:
        super().__init__(writer, tickers)
        self.period = period
        self.interval = interval

    def ingest(self) -> None:
        for ticker in self.tickers:
            api= history_period_interval(ticker=ticker)
            data = api.get_data(period=self.period, interval=self.interval)
            self.writer(ticker=ticker, api=api.__class__.__name__).write(data)

class SumarryDetailsIngestor(DataIngestor):
    def ingest(self) -> None:
        for ticker in self.tickers:
            api = summary_details(ticker)
            data= api.get_data()
            self.writer(ticker=ticker, api=api.__class__.__name__).write(data)

class GetAnualIngestor(DataIngestor):
    def ingest(self) -> None:
        for ticker in self.tickers:
            api = get_anual_income(ticker)
            data= api.get_data()
            self.writer(ticker=ticker, api=api.__class__.__name__).write(data)

class GetQuarterIngestor(DataIngestor):
    def ingest(self) -> None:
        for ticker in self.tickers:
            api = get_quarter_income(ticker)
            data= api.get_data()
            self.writer(ticker=ticker, api=api.__class__.__name__).write(data)