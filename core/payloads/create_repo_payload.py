from dataclasses import dataclass
from core.payloads.generic_payload_builder import BasePayload


@dataclass
class CreateRepoPayload(BasePayload):
    name: str
    description: str | None = None
    private: bool = False
    auto_init: bool = False
    gitignore_template: str = "Python"
    
    required_fields = ["name"]
