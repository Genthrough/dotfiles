from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class Organizations:
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
    def all_organizations(
        self,
        page: int | None = None,
        per_page: int | None = None,
        include_totals: bool = True,
        from_param: str | None = None,
        take: int | None = None,
    ) -> dict[str, Incomplete]: ...
    async def all_organizations_async(
        self,
        page: int | None = None,
        per_page: int | None = None,
        include_totals: bool = True,
        from_param: str | None = None,
        take: int | None = None,
    ) -> dict[str, Incomplete]: ...
    def get_organization_by_name(self, name: str | None = None) -> dict[str, Incomplete]: ...
    async def get_organization_by_name_async(self, name: str | None = None) -> dict[str, Incomplete]: ...
    def get_organization(self, id: str) -> dict[str, Incomplete]: ...
    async def get_organization_async(self, id: str) -> dict[str, Incomplete]: ...
    def create_organization(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    async def create_organization_async(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def update_organization(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    async def update_organization_async(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def delete_organization(self, id: str): ...
    async def delete_organization_async(self, id: str): ...
    def all_organization_connections(
        self, id: str, page: int | None = None, per_page: int | None = None
    ) -> list[dict[str, Incomplete]]: ...
    async def all_organization_connections_async(
        self, id: str, page: int | None = None, per_page: int | None = None
    ) -> list[dict[str, Incomplete]]: ...
    def get_organization_connection(self, id: str, connection_id: str) -> dict[str, Incomplete]: ...
    async def get_organization_connection_async(self, id: str, connection_id: str) -> dict[str, Incomplete]: ...
    def create_organization_connection(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    async def create_organization_connection_async(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def update_organization_connection(
        self, id: str, connection_id: str, body: dict[str, Incomplete]
    ) -> dict[str, Incomplete]: ...
    async def update_organization_connection_async(
        self, id: str, connection_id: str, body: dict[str, Incomplete]
    ) -> dict[str, Incomplete]: ...
    def delete_organization_connection(self, id: str, connection_id: str): ...
    async def delete_organization_connection_async(self, id: str, connection_id: str): ...
    def all_organization_members(
        self,
        id: str,
        page: int | None = None,
        per_page: int | None = None,
        include_totals: bool = True,
        from_param: str | None = None,
        take: int | None = None,
        fields: list[str] | None = None,
        include_fields: bool = True,
    ) -> dict[str, Incomplete]: ...
    async def all_organization_members_async(
        self,
        id: str,
        page: int | None = None,
        per_page: int | None = None,
        include_totals: bool = True,
        from_param: str | None = None,
        take: int | None = None,
        fields: list[str] | None = None,
        include_fields: bool = True,
    ) -> dict[str, Incomplete]: ...
    def create_organization_members(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    async def create_organization_members_async(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def delete_organization_members(self, id: str, body: dict[str, Incomplete]): ...
    async def delete_organization_members_async(self, id: str, body: dict[str, Incomplete]): ...
    def all_organization_member_roles(
        self, id: str, user_id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = False
    ) -> list[dict[str, Incomplete]]: ...
    async def all_organization_member_roles_async(
        self, id: str, user_id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = False
    ) -> list[dict[str, Incomplete]]: ...
    def create_organization_member_roles(self, id: str, user_id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    async def create_organization_member_roles_async(
        self, id: str, user_id: str, body: dict[str, Incomplete]
    ) -> dict[str, Incomplete]: ...
    def delete_organization_member_roles(self, id: str, user_id: str, body: dict[str, Incomplete]): ...
    async def delete_organization_member_roles_async(self, id: str, user_id: str, body: dict[str, Incomplete]): ...
    def all_organization_invitations(
        self, id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = False
    ) -> dict[str, Incomplete]: ...
    async def all_organization_invitations_async(
        self, id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = False
    ) -> dict[str, Incomplete]: ...
    def get_organization_invitation(self, id: str, invitaton_id: str) -> dict[str, Incomplete]: ...
    async def get_organization_invitation_async(self, id: str, invitaton_id: str) -> dict[str, Incomplete]: ...
    def create_organization_invitation(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    async def create_organization_invitation_async(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def delete_organization_invitation(self, id: str, invitation_id: str): ...
    async def delete_organization_invitation_async(self, id: str, invitation_id: str): ...
    def get_client_grants(
        self,
        id: str,
        audience: str | None = None,
        client_id: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        include_totals: bool = False,
    ) -> dict[str, Incomplete]: ...
    async def get_client_grants_async(
        self,
        id: str,
        audience: str | None = None,
        client_id: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        include_totals: bool = False,
    ) -> dict[str, Incomplete]: ...
    def add_client_grant(self, id: str, grant_id: str) -> dict[str, Incomplete]: ...
    async def add_client_grant_async(self, id: str, grant_id: str) -> dict[str, Incomplete]: ...
    def delete_client_grant(self, id: str, grant_id: str) -> dict[str, Incomplete]: ...
    async def delete_client_grant_async(self, id: str, grant_id: str) -> dict[str, Incomplete]: ...
