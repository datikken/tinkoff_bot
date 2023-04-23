import asyncio
import logging
from app.strategies.base import BaseStrategy
from app.client import client
from tinkoff.invest import AioRequestError
from app.strategies.interval.IntervalStrategy import IntervalStrategy

logger = logging.getLogger(__name__)


class IntervalStrategySearch(BaseStrategy):
    def __init__(self, figi: str, **kwargs):
        self.strategy = IntervalStrategy(figi, **kwargs)
        self.figi = figi
        self.state = False

    async def search_circle(self):
        # TODO implement loop break rules and persist
        while self.state is False:
            try:
                await self.strategy.ensure_market_open()
                await self.strategy.update_corridor()

                last_price = await self.strategy.get_last_price()
                logger.debug(f"Search: last price: {last_price}, figi={self.figi}")

                if last_price >= self.strategy.corridor.top:
                    logger.debug(
                        f"Search: last price {last_price} is higher than top corridor border "
                        f"{self.strategy.corridor.top}. figi={self.figi}"
                    )
                elif last_price <= self.strategy.corridor.bottom:
                    logger.debug(
                        f"Search: last price {last_price} is lower than bottom corridor border "
                        f"{self.strategy.corridor.bottom}. figi={self.figi}"
                    )
            except AioRequestError as are:
                logger.error(f"Client error {are}")

            await asyncio.sleep(self.strategy.config.check_interval)

    async def start(self):
        if self.strategy.account_id is None:
            try:
                self.strategy.account_id = (await client.get_accounts()).accounts.pop().id
            except AioRequestError as are:
                logger.error(
                    f"Error taking account id. Stopping strategy. {are}")
                return
        await self.search_circle()
