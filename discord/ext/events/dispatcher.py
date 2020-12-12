import asyncio
from typing import List, Optional

import discord

from .custom_events import _ALL
from .errors import InvalidEvent


class CustomEventDispatcher:
    def __init__(self, listening_to: Optional[List[str]]=None):
        valid_handlers = _ALL

        if listening_to:
            try:
                valid_handlers = {name: _ALL[name] for name in listening_to}
            except KeyError as e:
                raise InvalidEvent('no registered handler for {!r}'.format(e.args[0]))
        
        self.valid_handlers = valid_handlers

    def handle(self, client: discord.Client, event: str, *args, **kwargs):
        if event in self.valid_handlers:
            return

        for event_check in self.valid_handlers.values():
            asyncio.ensure_future(event_check(client, event, *args, **kwargs))
