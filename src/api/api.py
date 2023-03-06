from requests import Session

from src.api.models import Config, Endpoints, AuthData, OffersData, OfferItem, Action


class Api:
    config: Config
    session: Session

    def __init__(self, config: Config, session: Session) -> None:
        self.config = config
        self.session = session

    def auth(self) -> AuthData:
        try:
            response = self.session.post(
                f'{self.config.root_url}{Endpoints.login_password}',
                json={ 'phone': self.config.phone, 'password': self.config.password }
            )   
            
            return AuthData.parse_obj(response.json())
        except Exception as ex:
            print(ex)
    
    def get_offers(self) -> OffersData:
        try:
            response = self.session.post(f'{self.config.root_url}{Endpoints.offers_list()}')
            return OffersData.parse_obj(response.json())
        except Exception as ex:
            print(ex)

    def refresh_offer(self, offer: OfferItem) -> None:
        try:
            response = self.session.get(
                f'{self.config.root_url}{Endpoints.offers_action(offer.id, Action.REFRESH)}'
            )

            if response.json().get('status') != 'OK':
                print(f'Offer - {offer.id} | problem')
            else:
                print(f'Offer - {offer.id} | OK')
        except Exception as ex:
            print(ex)