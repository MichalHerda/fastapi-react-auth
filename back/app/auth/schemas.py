from pydantic import BaseModel, model_validator


class SignupRequest(BaseModel):
    email: str | None = None
    username: str | None = None
    password: str

    @model_validator(mode="after")
    def validate_identifiers(self):
        if not self.email and not self.username:
            raise ValueError("Either email or username is required")
        return self


class LoginRequest(BaseModel):
    identifier: str  # email OR username
    password: str


class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "bearer"
