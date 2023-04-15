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



if __name__ == "__main__":
#   inst = get_instrument_by('BBG000QDVR53')

# Shares
    shares = get_shares()
    # print(
    #     len(shares.instruments)
    # )
    for share in shares.instruments:
        if 'ozon' in share.name.lower():
            pprint(share.name)
            pprint(share.figi)
            print('')