from pydantic import BaseModel, ConfigDict


class StrictBaseModel(BaseModel):
    model_config = ConfigDict(extra='forbid', validate_by_name=True, serialize_by_alias=True)