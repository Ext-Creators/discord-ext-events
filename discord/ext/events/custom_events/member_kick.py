import discord

from ..utils import fetch_recent_audit_log_entry, listens_for


@listens_for('member_remove')
async def check_member_kick(client: discord.Client, member: discord.Member):
    guild = member.guild

    if not guild.me.guild_permissions.view_audit_log:
        return

    entry = await fetch_recent_audit_log_entry(client, member.guild, target=member, action=discord.AuditLogAction.kick, retry=3)
    if entry is None:
        return

    return member, entry
