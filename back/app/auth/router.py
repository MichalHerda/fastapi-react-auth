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
    # Check uniqueness
    if data.email and crud.get_user_by_email(db, data.email):
        raise HTTPException(
            status_code=400,
            detail="Email already in use",
        )

    if data.username and crud.get_user_by_username(db, data.username):
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


@router.post("/login")
def login(data: schemas.LoginRequest, db: Session = Depends(get_db)):
    # identifier może być email lub username
    user = None
    if data.email:
        user = crud.get_user_by_email(db, data.email)
    if not user and data.username:
        user = crud.get_user_by_username(db, data.username)

    if not user or not security.verify_password(data.password, user.password_hash):             # noqa
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = security.create_access_token({"sub": user.email or user.username})
    return {"access_token": token, "token_type": "bearer"}
