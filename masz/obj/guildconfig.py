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
        self.preferred_language = kwargs.get("preferredLanguage", "en")

    def __str__(self) -> str:
        return self.guild_id

    def to_dict(self) -> dict:
        return {
            "modRoles": self.mod_roles,
            "adminRoles": self.admin_roles,
            "mutedRoles": self.muted_roles,
            "modNotificationDM": self.dm_notification,
            "modPublicNotificationWebhook": self.public_webhook,
            "modInternalNotificationWebhook": self.internal_webhook,
            "strictModPermissionCheck": self.strict_permission_check,
            "executeWhoisOnJoin": self.execute_whois_on_join,
            "preferredLanguage": self.preferred_language
        }
