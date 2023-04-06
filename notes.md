
# id: 2017310133, name: Брокерский счёт, type: AccountType.ACCOUNT_TYPE_TINKOFF
# id: 2031542356, name: Инвесткопилка, type: AccountType.ACCOUNT_TYPE_INVEST_BOX
# id: 2013229493, name: ИИС, type: AccountType.ACCOUNT_TYPE_TINKOFF_IIS # blocked
# id: 2029571742, name: ИИС 1, type: AccountType.ACCOUNT_TYPE_TINKOFF_IIS

# TODO:
# 1. Try to reimplement via binance-connector or bybit
# 2. There is no potential to trade instrument when corridor top is reached 
# 3. Instrument volatility beta
# 4. Create next app or process to find an instrument which is in it's own corridor bottom

docker build -t tinek .

docker run -d -it --rm --name running-tinek tinek