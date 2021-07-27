import time
from masz import MASZClient, MASZLogLevel, console, Comment

log_level = MASZLogLevel.VERBOSE
token = 'my token'
client = MASZClient("http://127.0.0.1:5565", token, log_level=log_level)
time.sleep(2)

guild = client.discord.get_guild(769932817009606656)
console.log(f"Loaded guild '{guild.name}'.")
time.sleep(1)

guild_api = client.get_guild(769932817009606656)
modcases = guild_api.get_modcases()
console.log(f"This guild has {len(modcases)} modcases.")

modcase_api = modcases[-1]
console.log(f"The newest modcase is '{modcase_api}' with {len(modcase_api.comments)} comments.")
time.sleep(1)

comment = Comment(message="new comment")
modcase_api.post_comment(comment)
console.log(f"Posted a comment to the modcase.")
console.log(f"This modcase now has {len(modcase_api.comments) + 1} comments.")
time.sleep(1)

console.log(f"Done.")
