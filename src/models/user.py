import typing

import pydantic

from src.models.strict_base_model import StrictBaseModel


class CreateUserPayload(StrictBaseModel):
    firstName: pydantic.StrictStr = pydantic.Field(default='TestUserName')
    lastName: pydantic.StrictStr = pydantic.Field(default='TestLastName')
    age: pydantic.StrictInt = pydantic.Field(default=30)


class UserLoginResponse(StrictBaseModel):
    id_ : pydantic.StrictInt = pydantic.Field(alias='id')
    username: pydantic.StrictStr
    email: pydantic.StrictStr
    firstName: pydantic.StrictStr
    lastName: pydantic.StrictStr
    gender: pydantic.StrictStr
    image: pydantic.StrictStr
    accessToken: pydantic.StrictStr
    refreshToken: pydantic.StrictStr


class CryptoResponse(StrictBaseModel):
    coin: pydantic.StrictStr
    wallet: pydantic.StrictStr
    network: pydantic.StrictStr


class UserCoordinatesResponse(StrictBaseModel):
    lat: typing.Optional[pydantic.StrictFloat] = None
    lng: typing.Optional[pydantic.StrictFloat] = None


class AddressResponse(StrictBaseModel):
    address: pydantic.StrictStr
    city: pydantic.StrictStr
    state: pydantic.StrictStr
    stateCode: pydantic.StrictStr
    postalCode: pydantic.StrictStr
    coordinates: UserCoordinatesResponse
    country: pydantic.StrictStr


class CompanyResponse(StrictBaseModel):
    department: pydantic.StrictStr
    name: pydantic.StrictStr
    title: pydantic.StrictStr
    address: AddressResponse


class UserBankResponse(StrictBaseModel):
    cardExpire: pydantic.StrictStr
    cardNumber: pydantic.StrictStr
    cardType: pydantic.StrictStr
    currency: pydantic.StrictStr
    iban: pydantic.StrictStr


class UserHairAuthResponse(StrictBaseModel):
    color: pydantic.StrictStr
    type: pydantic.StrictStr


class UserResponse(StrictBaseModel):
    id_: pydantic.StrictInt = pydantic.Field(alias='id')
    firstName: pydantic.StrictStr
    lastName: pydantic.StrictStr
    maidenName: pydantic.StrictStr
    age: pydantic.StrictInt
    gender: pydantic.StrictStr
    email: pydantic.StrictStr
    phone: pydantic.StrictStr
    username: pydantic.StrictStr
    password: pydantic.StrictStr
    birthDate: pydantic.StrictStr
    image: pydantic.StrictStr
    bloodGroup: pydantic.StrictStr
    height: typing.Optional[pydantic.StrictFloat] = None
    weight: typing.Optional[pydantic.StrictFloat] = None
    eyeColor: pydantic.StrictStr
    hair: UserHairAuthResponse
    ip: pydantic.StrictStr
    address: AddressResponse
    macAddress: pydantic.StrictStr
    university: pydantic.StrictStr
    bank: UserBankResponse
    company: CompanyResponse
    ein: pydantic.StrictStr
    ssn: pydantic.StrictStr
    userAgent: pydantic.StrictStr
    crypto:CryptoResponse
    role: pydantic.StrictStr


class UsersResponse(StrictBaseModel):
    users: typing.List[UserResponse]
    total: pydantic.StrictInt
    skip: pydantic.StrictInt
    limit: pydantic.StrictInt


class UpdateUserPayload(StrictBaseModel):
    firstName: typing.Optional[pydantic.StrictStr] = None
    lastName: typing.Optional[pydantic.StrictStr] = None
    age: typing.Optional[pydantic.StrictInt] = None


class DeletedUserResponse(UserResponse):
    isDeleted: pydantic.StrictBool
    deletedOn: pydantic.StrictStr


class UserNotFoundErrorResponse(StrictBaseModel):
    message: pydantic.StrictStr


class GenerateApiRequest(StrictBaseModel):
    json_body: typing.Dict = pydantic.Field(default_factory=dict, alias="json")
    method: pydantic.StrictStr = pydantic.Field(default='GET')


class BadRequestResponse(StrictBaseModel):
    status: pydantic.StrictInt = pydantic.Field(default=400)
    title: pydantic.StrictStr
    type: pydantic.StrictStr
    detail: pydantic.StrictStr
    message: pydantic.StrictStr