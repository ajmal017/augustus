import abc
from typing import Generator

from augustus.system.metabase_env import augustusEnvBase


class ReaderBase(augustusEnvBase, abc.ABC):
    
    def __init__(self, ticker: str, key: str = None) -> None:
        self.ticker = ticker
        self.key = key

        if key:
            self.env.readers[f'{ticker}_{key}'] = self
        else:
            self.env.readers[ticker] = self

    @abc.abstractmethod
    def load(self, fromdate: str, todate: str, frequency: str) -> Generator:
        raise NotImplementedError

    def load_by_cleaner(self, fromdate: str, todate: str,
                        frequency: str) -> Generator:

        return self.load(fromdate, todate, frequency)

