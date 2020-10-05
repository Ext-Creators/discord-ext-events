import discord

from .dispatcher import CustomEventDispatcher


class EventsMixin(discord.Client):
    dispatcher = CustomEventDispatcher()

    def dispatch(self, event, *args, **kwargs):
        super().dispatch(event, *args, **kwargs)  # type: ignore
        self.dispatcher.handle(self, event, *args, **kwargs)  # type: ignore
