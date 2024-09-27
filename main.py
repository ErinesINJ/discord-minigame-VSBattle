import discord, certifi, random, time, datetime
from discord.ext import commands
from discord import app_commands

from modules.embeds import battleEmbed, battleWinner, duelEmbed, acceptedDuel
from modules.game import randomizer
from config import battleDelay, responseDelay, allowed_channel_id, allowed_role_id, guild_id, discord_bot_token

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
            print("Slash commands synced")
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

class verification_ui(discord.ui.View):
    def __init__(self, player, user, channel):
        super().__init__()
        self.player = player
        self.user = user
        self.channel = channel
        self.accepted = False

    async def on_timeout(self):
        try:
            if not self.accepted:
                await self.channel.send(f"The duel between <@{self.player.id}> and <@{self.user.id}> has timed out. Duel is cancelled.")
                global duel_in_progress
                duel_in_progress = False
        except Exception as e:
            print(f'Error on_timeout: {e}')

    @discord.ui.button(label='Accept', style=discord.ButtonStyle.green)
    async def one(self, interaction: discord.Interaction, _: discord.ui.Button):
        await interaction.response.defer()
        global duel_in_progress
        try:
            self.accepted = True
            if self.user == interaction.user:
                self.stop()
                embed = await acceptedDuel()
                await interaction.followup.send(content=f'Duel between <@{self.player.id}> and <@{self.user.id}> is about to start in 10 seconds...', embed=embed)
                countdown_message = await interaction.followup.send('10...')
                await asyncio.sleep(1)
                for i in range(battleDelay, 0, -1):
                    await countdown_message.edit(content=f'{i}...')
                    await asyncio.sleep(1)

                item_name, item_link = await randomizer()
                embed = await duelEmbed(item_link)
                await countdown_message.edit(content='' , embed=embed)
                start_time = datetime.datetime.now()
                while True:
                    try:
                        if (datetime.datetime.now() - start_time).seconds > responseDelay:
                            await interaction.channel.send(f"<@{self.player.id}> and <@{self.user.id}> didn't respond in time. Duel is cancelled.")
                            duel_in_progress = False
                            break
                        
                        user_response = await client.wait_for('message', timeout=0.05, check=lambda m: m.author == self.player or m.author == self.user and m.channel == interaction.channel)

                        if user_response.content.lower() == item_name:
                            if user_response.author.id == self.user.id:
                                loser = self.player
                            elif user_response.author.id == self.player.id:
                                loser = self.user
                            embed = await battleWinner()
                            await interaction.channel.send(content=f'🏆 <@{user_response.author.id}> won the duel with <@{loser.id}>', embed=embed)
                            duel_in_progress = False
                            break
                        else:
                            await user_response.add_reaction("❌")

                    except asyncio.TimeoutError:
                        continue
                    except Exception as e:
                        print(f'Error while True function: {e}')
                        duel_in_progress = False
                        break
            else:
                await interaction.followup.send("You're not allowed to do that 🖕", ephemeral=True)
                duel_in_progress = False

        except Exception as e:
            duel_in_progress = False
            print(f'Error Accept Button: {e}')

    @discord.ui.button(label='Decline', style=discord.ButtonStyle.red)
    async def check_wallets(self, interaction: discord.Interaction, _: discord.ui.Button):
        await interaction.response.defer()
        global duel_in_progress
        try:
            self.accepted = True
            if self.user == interaction.user:
                self.stop()
                await interaction.followup.send(f'<@{interaction.user.id}> declined the duel')
                duel_in_progress = False
            else:
                await interaction.followup.send("You're not allowed to do that 🖕", ephemeral=True)
                duel_in_progress = False
        except Exception as e:
            duel_in_progress = False
            print(f'Error Decline Button: {e}')

async def can_use_command(user):
    try:
        guild = client.get_guild(guild_id)
        role_id = allowed_role_id
        role = discord.utils.get(guild.roles, id=role_id)

        if role in user.roles:
            print('[+] User has the role')
            return True
        else:
            print("[-] User doesn't have the role")
            return False

    except Exception as e:
        print(e)
    
duel_in_progress = False
@tree.command(name='duel', description='Duel with someone')
async def slash2(interaction: discord.Interaction, user: discord.Member):
    global duel_in_progress
    try:
        if duel_in_progress:
            await interaction.response.send_message('A duel is already in progress. Please wait until the current duel ends.', ephemeral=True)
            return
        if interaction.channel.id != allowed_channel_id:
            await interaction.response.send_message("You can't use this command in this channel...", ephemeral=True)
            return
        if user == interaction.user:
            await interaction.response.send_message(f"You can't fight yourself...", ephemeral=True)
            return
        if user.bot:
            await interaction.response.send_message(f"You can't fight a bot...", ephemeral=True)
            return
        
        player = interaction.user
        print(f'[+] {interaction.user} Wants to Fight')
        duel_in_progress = True

        can_use = await can_use_command(player)
        if can_use:
            embed = await battleEmbed(player, user)
            view = verification_ui(player, user, interaction.channel)
            view.timeout = 30
            await interaction.response.send_message(content=f"<@{user.id}> you've been challenged to a Duel!", embed=embed, view=view)
        else:
            await interaction.response.send_message(f"You're not allowed to use this command...", ephemeral=True)
    except Exception as e:
        print(f'Error while trying to duel: {e}')
        duel_in_progress = False
        
async def main():
    await client.start(discord_bot_token)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())


