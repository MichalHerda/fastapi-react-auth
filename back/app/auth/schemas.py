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
    username: str | None = None
    email: str | None = None
    password: str

    @model_validator(mode="after")
    def validate_identifiers(self):
        if not self.username and not self.email:
            raise ValueError("Either email or username is required")
        return self


class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "bearer"
