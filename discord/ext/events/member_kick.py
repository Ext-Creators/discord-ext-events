import discord

from ._events import _ALL
from .utils import fetch_recent_audit_log_entry


EVENT_NAME = 'member_kick'


async def check_member_kick(client: discord.Client, event: str, *args, **kwargs):
    if event != 'member_remove':
        return

    member, = args
    guild = member.guild

    if not guild.me.guild_permissions.view_audit_log:
        return

    entry = await fetch_recent_audit_log_entry(client, member.guild, target=member, action=discord.AuditLogAction.kick, retry=3)
    if entry is None:
        return

    client.dispatch(EVENT_NAME, member, entry)


_ALL[EVENT_NAME] = check_member_kick
