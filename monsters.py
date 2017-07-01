#!/usr/bin/env python3
import asyncio, discord
from discord.ext import commands

global monsterList
monsterList = {
    "belladeon": "Belladeon is Runed Swift/Energy or Violent/Energy SPD HP HP with at least 45% Accuracy for Giants 55% for Dragons, and as much speed as you can! ",
    "rakan": "Rakan is Runed Vampire/Will HP CRIT DAMAGE HP With as much Speed and Crit Rate Subs as you can!",
    "Daphnis": "Daphnis is Runed Fatal/Blade Rage/Blade Violent/blade SPD CRIT DAMAGE ATTACK with Atleast 65%+ Crit Damage and As much Attack and speed as Possible!",
}

class Monsters():
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def monster(self,ctx,*,msg:str):
        try:
            foundit=0
            for key,value in monsterList.items():
                if msg.lower() in key.lower():
                    await self.client.say(value)
                    foundit+=1
            if foundit == 0:
                await self.client.say("Not found")
        except Exception as e:
            await self.client.say(e)
            return

def setup(client):
    client.add_cog(Monsters(client))