
import abc

from augustus.constants import ActionType
from augustus.system.base_recorder import RecorderBase
from augustus.system.components.signal_generator import SignalGenerator
from augustus.system.metabase_env import augustusEnvBase


class StrategyBase(augustusEnvBase, abc.ABC):

    def __init__(self) -> None:
        self.name = self.__class__.__name__
        self.env.strategies.update({self.name: self})

        self.buy = SignalGenerator(ActionType.Buy, self.name).buy_or_short
        self.sell = SignalGenerator(ActionType.Sell, self.name).sell_or_cover
        self.short = SignalGenerator(ActionType.Short, self.name).buy_or_short
        self.cover = SignalGenerator(ActionType.Cover, self.name).sell_or_cover
        self.cancel_pending = SignalGenerator(
            ActionType.Cancel, self.name).cancel_pending
        self.cancel_tst = SignalGenerator(
            ActionType.Cancel, self.name).cancel_tst
        self.params: dict = None

    @property
    def recorder(self) -> RecorderBase:
        
        return self.env.recorder

    @abc.abstractmethod
    def handle_bar(self):
        raise NotImplementedError

    def run(self):
        self.handle_bar()

    def cur_price(self, ticker: str) -> float:
        return self.env.feeds[ticker].cur_price

    def set_params(self, params: dict):
        self.params.update(params)
