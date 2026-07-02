from dataclasses import dataclass

@dataclass
class InterestEntity:
    id: int | None
    name: str
    code: str