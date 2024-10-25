from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    name: str = Field(min_length=1, max_length=255)
