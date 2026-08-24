from unittest.mock import Mock

from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from app.api.dependencies import get_current_user
from app.core.security import create_access_token, decode_access_token, hash_password, verify_password


def test_password_verification_round_trip():
    raw_password = "secret123"
    hashed_password = hash_password(raw_password)

    assert verify_password(raw_password, hashed_password) is True
    assert verify_password("wrong-password", hashed_password) is False


def test_access_token_round_trip():
    token = create_access_token("123e4567-e89b-12d3-a456-426614174000")

    assert decode_access_token(token) == "123e4567-e89b-12d3-a456-426614174000"


def test_get_current_user_missing_user_raises_http_exception():
    token = create_access_token("123e4567-e89b-12d3-a456-426614174000")
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)

    db = Mock()
    db.query.return_value.filter.return_value.first.return_value = None

    try:
        get_current_user(credentials=credentials, db=db)
        assert False, "Expected HTTPException to be raised"
    except HTTPException as exc:
        assert exc.status_code == 401
        assert exc.detail == "User not found"
