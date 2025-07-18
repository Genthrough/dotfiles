from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Azure(VaultApiBase):
    def configure(
        self, subscription_id, tenant_id, client_id=None, client_secret=None, environment=None, mount_point="azure"
    ): ...
    def read_config(self, mount_point="azure"): ...
    def delete_config(self, mount_point="azure"): ...
    def create_or_update_role(self, name, azure_roles, ttl=None, max_ttl=None, mount_point="azure"): ...
    def list_roles(self, mount_point="azure"): ...
    def generate_credentials(self, name, mount_point="azure"): ...
