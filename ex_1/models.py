from pydantic import BaseModel


class UserNumber(BaseModel):
    number: int

