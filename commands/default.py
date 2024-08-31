import discord
from discord import app_commands
from discord.ext import commands

class DefaultCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction) -> None:
        """봇의 응답속도를 알려줍니다."""
        
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! `{latency}ms`")

    @app_commands.command(name="help")
    async def ping(self, interaction: discord.Interaction) -> None:
        """봇의 정보를 알려줍니다."""
        
        embed = discord.Embed(
                color=0xFDFD96,
        )
        embed.set_author(
            name=f"{self.bot.user.name} 소개",
            icon_url=f"{self.bot.user.avatar}"
        )
        
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="명령어 목록 보기", custom_id="show_command_list"))

        await interaction.response.send_message(embed=embed, view=view)
    
    @app_commands.command(name="list")
    async def ping(self, interaction: discord.Interaction) -> None:
        """봇의 명령어 목록을 보여줍니다."""
        
        embed = discord.Embed(
            color=0xFDFD96,
            title=f"{self.bot.user.name} 명령어 목록",
            description="아래는 봇의 명령어 목록입니다."
        )
        embed.add_field(name="/ping", value="봇의 응답속도를 알려줍니다.", inline=False)
        embed.add_field(name="/help", value="봇의 정보를 알려줍니다.", inline=False)
        embed.add_field(name="/list", value="봇의 명령어 목록을 보여줍니다.", inline=False)
        
        await interaction.response.send_message(embed=embed)
        
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.data.get("custom_id") == "show_command_list":
            await self.command_list(interaction)

    
async def setup(bot: commands.Bot):
    await bot.add_cog(DefaultCommand(bot))
