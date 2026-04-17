


import discord
from discord import app_commands
import os

# CONFIGURATION
TOKEN = os.getenv('DISCORD_TOKEN')
TON_ID = 1287493067271835740  # Ton ID Discord

class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"✅ Bot connecté : {self.user}")

bot = Bot()
tree = app_commands.CommandTree(bot)

# COMMANDE : /demandecam
@tree.command(name="demandecam", description="Demande d'accès à la caméra")
async def demandecam(interaction: discord.Interaction):
    user = interaction.user
    admin = await bot.fetch_user(TON_ID)
    await admin.send(f"🔴 **{user.name}** a demandé un accès caméra !\n👤 ID: {user.id}")
    await interaction.response.send_message(f"✅ Demande envoyée à l'admin, {user.mention} !", ephemeral=False)

# COMMANDE : /demande
@tree.command(name="demande", description="Envoyer une demande à l'admin")
async def demande(interaction: discord.Interaction, message: str):
    admin = await bot.fetch_user(TON_ID)
    await admin.send(f"📩 **Nouvelle demande de {interaction.user.name}** :\n{message}\n👤 ID: {interaction.user.id}")
    await interaction.response.send_message(f"✅ Demande envoyée !", ephemeral=True)

# COMMANDE : /demandephish
@tree.command(name="demandephish", description="Signaler un lien de phishing")
async def demandephish(interaction: discord.Interaction):
    user = interaction.user
    admin = await bot.fetch_user(TON_ID)
    await admin.send(f"🎣 **{user.name} a signalé un lien de phishing !**\n👤 ID: {user.id}")
    await interaction.response.send_message(f"✅ Merci pour ton signalement, {user.mention} !", ephemeral=True)

# LANCEMENT
if __name__ == "__main__":
    bot.run(TOKEN)
