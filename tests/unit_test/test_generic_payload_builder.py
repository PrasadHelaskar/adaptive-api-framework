import pytest
from dataclasses import dataclass
from core.payloads.generic_payload_builder import BasePayload


@dataclass
class Payloadtest(BasePayload):
    name: str
    description: str | None = None
    private: bool = False

    required_fields = ["name","private"]

@pytest.mark.unit
def test_base_payload_missing_required():
    with pytest.raises(TypeError):
        Payloadtest().build() # Intentionally retained for unit testing

@pytest.mark.unit
def test_base_payload_valid():
    payload = Payloadtest(name="test").build()
    assert payload == {"name": "test", "private": False}
