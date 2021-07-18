import dateparser

class Adminstats:
    def __init__(self, **kwargs) -> None:
        self.last_logins = kwargs.get("loginsInLast15Minutes", [])
        self.tracked_invites = kwargs.get("trackedInvites", 0)
        self.modCases = kwargs.get("modCases", 0)
        self.guilds = kwargs.get("guilds", 0)
        self.automod_events = kwargs.get("automodEvents", 0)
        self.usernotes = kwargs.get("userNotes", 0)
        self.usermappings = kwargs.get("userMappings", 0)
        self.apiTokens = kwargs.get("apiTokens", 0)
        self.next_cache = dateparser.parse(kwargs.get("nextCache", 0))
        self.cached_data = kwargs.get("cachedDataFromDiscord", [])
