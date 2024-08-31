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
    async def help(self, interaction: discord.Interaction) -> None:
        """봇의 정보를 알려줍니다."""
        
        embed = discord.Embed(
                color=0xFDFD96,
                description="""설명 여기에"""
        )
        embed.set_author(
            name=f"{self.bot.user.name} 소개",
            icon_url=f"{self.bot.user.avatar}"
        )
        # 명령어 보기 버튼 생성
        view = discord.ui.View()

        button = discord.ui.Button(
            label="명령어 목록 보기",
            style=discord.ButtonStyle.primary,
            custom_id="show_command_list",
        )
        button.callback = self.button_callback
        view.add_item(button)

        await interaction.response.send_message(embed=embed, view=view)

    async def button_callback(self, interaction: discord.Interaction):
        if interaction.data['custom_id'] == "show_command_list":
            await self.show_command_list(interaction)

    # 버튼을 통해서도 불러와야 해서 별도의 메서드로 분리
    async def show_command_list(self, interaction: discord.Interaction) -> None:
        """봇의 명령어 목록을 보여주는 내부 메서드."""
        
        embed = discord.Embed(
            color=0xFDFD96,
            title=f"{self.bot.user.name} 명령어 목록"
        )
        embed.add_field(name="/ping", value="봇의 응답속도를 알려줍니다.", inline=False)
        embed.add_field(name="/help", value="봇의 정보를 알려줍니다.", inline=False)
        embed.add_field(name="/list", value="봇의 명령어 목록을 보여줍니다.", inline=False)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="list")
    async def list(self, interaction: discord.Interaction) -> None:
        """봇의 명령어 목록을 보여줍니다."""
        await self.show_command_list(interaction)

    
async def setup(bot: commands.Bot):
    await bot.add_cog(DefaultCommand(bot))
