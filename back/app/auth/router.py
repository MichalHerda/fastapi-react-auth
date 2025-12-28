from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import crud, schemas, security
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(
    data: schemas.SignupRequest,
    db: Session = Depends(get_db),
):
    # Optional: check uniqueness
    if data.email:
        if crud.get_user_by_email(db, data.email):
            raise HTTPException(
                status_code=400,
                detail="Email already in use",
            )

    if data.username:
        if crud.get_user_by_username(db, data.username):
            raise HTTPException(
                status_code=400,
                detail="Username already in use",
            )

    password_hash = security.hash_password(data.password)

    crud.create_user(
        db=db,
        email=data.email,
        username=data.username,
        password_hash=password_hash,
    )

    return {"message": "User created"}


@router.post("/login", response_model=schemas.AuthResponse)
def login(
    data: schemas.LoginRequest,
    db: Session = Depends(get_db),
):
    user = crud.get_user_by_identifier(db, data.identifier)

    if not user or not security.verify_password(
        data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = security.create_access_token(
        data={"sub": str(user.id)},
    )

    return schemas.AuthResponse(
        access_token=access_token,
        token_type="bearer",
    )
