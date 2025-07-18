from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class Prompts:
    domain: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(
        self,
        domain: str,
        token: str,
        telemetry: bool = True,
        timeout: TimeoutType = 5.0,
        protocol: str = "https",
        rest_options: RestClientOptions | None = None,
    ) -> None: ...
    def get(self) -> dict[str, Incomplete]: ...
    async def get_async(self) -> dict[str, Incomplete]: ...
    def update(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    async def update_async(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get_custom_text(self, prompt: str, language: str): ...
    async def get_custom_text_async(self, prompt: str, language: str): ...
    def update_custom_text(self, prompt: str, language: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    async def update_custom_text_async(
        self, prompt: str, language: str, body: dict[str, Incomplete]
    ) -> dict[str, Incomplete]: ...
