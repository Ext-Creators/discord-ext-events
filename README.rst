discord-ext-events
==================

|dependencies| |license|

Custom events derived from events dispatched by Discord. 

    ⚠️ Work In Progress!

Installation
------------

This extension is currently not in PyPI.

.. code-block:: sh

    $ python3 -m pip install -U git+https://github.com/Ext-Creators/discord-ext-events


Usage
-----

An example for when subscribing to the on_member_kick event.

.. code-block:: py

    import discord
    from discord.ext import commands, events
    from discord.ext.events import member_kick


    class MyBot(commands.Bot, events.EventsMixin):

        async def on_ready(self):
            print('Logged in!')

        async def on_member_kick(self, member: discord.Member, entry: discord.AuditLogEntry):
            print(f'{member} was kicked from {member.guild}!')


    bot = MyBot(command_prefix='!', intents=discord.Intents.all())

    bot.run("TOKEN")

.. |dependencies| image:: https://img.shields.io/librariesio/github/Ext-Creators/discord-ext-events
.. |license| image:: https://img.shields.io/pypi/l/discord-ext-events.svg
