from requests import Session
from dotenv import load_dotenv; load_dotenv()
from os import getenv
from threading import Thread

from src.api.api import Api
from src.api.models import Config


class App:

    session: Session
    api: Api
    config: Config

    def __init__(self) -> None:
        try:
            self.config = Config(
                root_url=getenv('RIELTOR_ROOT_URL'), 
                phone=getenv('RIELTOR_PHONE'), 
                password=getenv('RIELTOR_PASSWORD')
            )
            self.session = Session()
            self.api = Api(self.config, self.session)
            self._create_auth_session()
        except Exception as ex:
            print(ex)

    def _create_auth_session(self) -> None:
        self.api.auth()
        print('Create session')

    def refresh_offers(self) -> None:
        offers = self.api.get_offers()

        for offer in offers.data.items:
            Thread(target=self.api.refresh_offer, args=(offer, )).start()