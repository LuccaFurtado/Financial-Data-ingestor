
from code import DataWriter, GetAnualIngestor
import dataingestor


ingestor= GetAnualIngestor( writer=DataWriter,tickers=['PETR4','ITUB3'])
ingestor.ingest()
