from grpc import StatusCode
from pydantic import BaseSettings
from tinkoff.invest import Client, RequestError, InstrumentIdType
from pprint import pprint

class Settings(BaseSettings):
    token: str

    class Config:
        env_file = ".env"


settings = Settings()


def get_instrument_by(figi):
    with Client(settings.token) as client:
        try:
            return client.instruments.get_instrument_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=figi)
        except RequestError as e:
            if e.code == StatusCode.UNAUTHENTICATED:
                return get_sandbox_accounts()


if __name__ == "__main__":
  inst = get_instrument_by('BBG000QDVR53')
  pprint(inst)