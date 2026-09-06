import typing

import pydantic

from src.models.strict_base_model import StrictBaseModel


class DefaultHeaders(StrictBaseModel):
    content_type: pydantic.StrictStr = pydantic.Field(default="application/json", alias='Content-Type')
    authorization: typing.Optional[pydantic.StrictStr] = pydantic.Field(default=None, alias='Authorization')