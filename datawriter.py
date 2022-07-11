import datetime
import json
import os
from typing import List

from pandas import DataFrame


class DataWriter:
    def __init__(self, ticker:str , api : str) -> None:
        self.api =api
        self.ticker = ticker
        self.filename = f"{self.api}/{self.ticker}/{datetime.datetime.now().strftime('%Y-%m-%d+%H-%M')}.json"
     

    def _write_row(self, row:str) ->None:
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, "a") as f:
            f.write(row)

    def write(self, data: list[ DataFrame, dict] ):
        if isinstance(data, dict):
            self._write_row(json.dumps(data)+ "\n")
        elif isinstance(data,DataFrame):
            self._write_row(data.to_json(orient='index').replace('},',"},\n")+ "\n")
        else:
            print('erro')
