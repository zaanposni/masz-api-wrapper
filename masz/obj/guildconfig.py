class GuildConfig:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.guild_id = kwargs.get("guildId")
        self.mod_roles = kwargs.get("modRoles", [])
        self.admin_roles = kwargs.get("adminRoles", [])
        self.muted_roles = kwargs.get("mutedRoles", [])
        self.dm_notification = kwargs.get("modNotificationDM", False)
        self.public_webhook = kwargs.get("modPublicNotificationWebhook", '')
        self.internal_webhook = kwargs.get("modInternalNotificationWebhook", '')
        self.strict_permission_check = kwargs.get("strictModPermissionCheck", False)
        self.execute_whois_on_join = kwargs.get("executeWhoisOnJoin", False)

    def __str__(self) -> str:
        return self.guild_id
