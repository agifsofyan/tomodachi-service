from dataclasses import dataclass
from uuid import UUID

@dataclass
class InterestEntity:
    id: UUID
    name: str
    code: str