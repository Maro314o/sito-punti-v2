from pydantic import BaseModel


class TokenResponse(BaseModel):
    token: str


class ErrorResponse(BaseModel):
    error: str
