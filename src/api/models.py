from pydantic import BaseModel, fields
from enum import StrEnum
from typing import Any


class Config(BaseModel):
    root_url: str
    phone: str
    password: str


class AuthData(BaseModel):
    status: str


class OfferItem(BaseModel):
    status: int|None
    oper: str|None
    id: int|None
    address: str|None
    orient: str|None
    rooms: int|None
    floor: str|None
    area: str|None
    autoupdate: bool|None
    price: str|None
    exclusiveComment: str|None
    exclusiveStatus: int|None
    rate: float|int|None
    itemType: str|None
    cityName: str|None
    mainImage: str|None
    commonArea: int|None
    usefulArea: int|None
    kitchenArea: int|None
    dailyCost: int|None
    premiumLabel: str|None
    flatfyUrl: str|None
    updatedAt: str|None
    createdAt: str|None
    viewToday: int|None
    viewYesterday: int|None
    viewAll: int|None
    offerUrl: str|None
    cityPos: int|None
    savedRates: Any
    userId: int|None


class Data(BaseModel):
    items: list[OfferItem]


class OffersData(BaseModel):
    data: Data|None
    status: str


class Action(StrEnum):
    REFRESH = 'refresh'


class Endpoints:
    login_password = '/users/login-password/'

    @staticmethod
    def offers_action(id: str, action: Action):
        return f'/offers/item-action/?{id=}&action={action}'
    
    @staticmethod
    def offers_list(page: int = 1, limit: int = 50):
        return f'/offers/list/?{page=}&{limit=}'