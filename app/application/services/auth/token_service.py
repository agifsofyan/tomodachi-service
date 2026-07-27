from typing import Any

from app.core.security import create_access_token, decode_token


class TokenService:
    def generate(self, user_id: str) -> str:
        return create_access_token(user_id)

    def decode(self, token: str) -> dict[str, Any]:
        return decode_token(token)
