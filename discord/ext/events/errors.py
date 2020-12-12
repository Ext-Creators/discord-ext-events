from discord.errors import DiscordException

class EventsException(DiscordException):
    pass

class InvalidEvent(EventsException):
    pass
