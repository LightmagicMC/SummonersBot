#!/usr/bin/env python3
import asyncio, discord
from discord.ext import commands

class Runes():
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def rune(self,ctx,*,msg : str):
        await self.client.say("HI\n".format(msg))
        return

def setup(client):
    client.add_cog(Runes(client))