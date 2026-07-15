from dataclasses import dataclass
from uuid import UUID

@dataclass
class UserEntity:
    id: UUID
    name: str
    email: str
    password: str