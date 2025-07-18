from _typeshed import Incomplete
from typing import Final

class ClientRegistrationEndpoint:
    ENDPOINT_NAME: Final = "client_registration"
    software_statement_alg_values_supported: Incomplete
    server: Incomplete
    claims_classes: list[type[Incomplete]]
    def __init__(self, server=None, claims_classes: list[type[Incomplete]] | None = None) -> None: ...
    def __call__(self, request) -> dict[Incomplete, Incomplete]: ...
    def create_registration_response(self, request): ...
    def extract_client_metadata(self, request): ...
    def extract_software_statement(self, software_statement, request): ...
    def generate_client_info(self): ...
    def generate_client_registration_info(self, client, request) -> None: ...
    def create_endpoint_request(self, request): ...
    def generate_client_id(self): ...
    def generate_client_secret(self): ...
    def get_server_metadata(self) -> None: ...
    def authenticate_token(self, request) -> None: ...
    def resolve_public_key(self, request) -> None: ...
    def save_client(self, client_info, client_metadata, request) -> None: ...
