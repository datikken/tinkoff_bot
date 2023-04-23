from grpc import StatusCode
from tinkoff.invest import Client, RequestError, InstrumentIdType
from pprint import pprint
from accounts import get_sandbox_accounts
from setting import settings


def get_instrument_by(figi):
    with Client(settings.token) as client:
        try:
            return client.instruments.get_instrument_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=figi)
        except RequestError as e:
            if e.code == StatusCode.UNAUTHENTICATED:
                return get_sandbox_accounts()


def get_shares():
    with Client(settings.token) as client:
        try:
            return client.instruments.shares()
        except RequestError as e:
            if e.code == StatusCode.UNAUTHENTICATED:
                return get_sandbox_accounts()


def get_share_by_figi(figi):
    shares = get_shares()
    for share in shares.instruments:
        if figi in share.figi:
            return share


if __name__ == "__main__":
    share = get_share_by_figi('BBG00Y91R9T3')
    pprint(share)
