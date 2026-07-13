from ezcord import discord

app_commands = discord.app_commands


def setup(bot):
    @app_commands.command(name="via", description="Show instructions for setting up VIA")
    async def via(interaction: discord.Interaction):
        response = (
            "Here's how to set up VIA:\n"
            "[Find the .json here](<https://epomaker.com/blogs/via-json>)\n"
            "[usevia.app](<https://usevia.app/>)\n"
            "https://cdn.discordapp.com/attachments/850980474028687371/1367965498007883796/via.mp4\n"
            "\n"
            "Or follow this guide: https://discord.com/channels/726610136084250764/1390653548475318367"
        )
        await interaction.response.send_message(response)

    @app_commands.command(name="support", description="Show support contact information")
    async def support(interaction: discord.Interaction):
        response = (
            "If customer support is needed please Email:\n"
            "**support@epomaker.com**\n"
            "\n"
            "**For support regarding keyboard troubleshooting and specific keyboard questions please ask your question by posting in** "
            "https://discord.com/channels/726610136084250764/1020599685930549289\n"
            "\n"
            "We ask that you refrain from pinging Epomaker, Epomaker Staff, and Moderators as they will respond to your inquiry as soon as they see it."
        )
        await interaction.response.send_message(response)

    @app_commands.command(name="collab", description="Show collaboration inquiry information")
    async def collab(interaction: discord.Interaction):
        response = (
            "# For Collaboration Inquiries:\n\n"
            "- **YouTube, TikTok, Facebook, PR**: Please contact the Marketing team via email: marketing@epomaker.com\n\n"
            "- **Twitter, Instagram**: Feel free to DM our official accounts directly.\n\n"
            "- **For collaborations related to Discord, Facebook groups, or any community**: Please DM <@epomakersupport>\n\n"
            "- **For collaborations related to exhibitions, events, or sponsorships**: Please contact the Marketing team via email (marketing@epomaker.com).\n\n"
            "- **To apply as a reviewer in our Discord server**: \n"
            "  -https://discord.com/channels/726610136084250764/1309443436742443048\n"
            "  -https://discord.com/channels/726610136084250764/1392065267055460403"
        )
        await interaction.response.send_message(response)

    @app_commands.command(name="language", description="Show keyboard language change instructions")
    async def language(interaction: discord.Interaction):
        response = (
            "To change the language of your keyboard, please follow these steps:\n\n"
            "https://cdn.discordapp.com/attachments/915825857635975198/1427789606962855976/1231.mp4"
        )
        await interaction.response.send_message(response)

    @app_commands.command(name="spreadsheet", description="Show JoMama's spreadsheet for keyboards and switches")
    async def spreadsheet(interaction: discord.Interaction):
        response = (
            "Here is JoMama's [spreadsheet for Keyboards and Switches]"
            "(https://docs.google.com/spreadsheets/d/1Otv49VQ1uQ3dLBgFrd623c7ceAWgCqu6s20mSKxfZUg/edit?pli=1&gid=0#gid=0)"
        )
        await interaction.response.send_message(response)

    @app_commands.command(name="help", description="Show available slash commands")
    async def help_command(interaction: discord.Interaction):
        response = (
            "Here are the available commands:\n"
            "- `/via`: Instructions for setting up VIA\n"
            "- `/support`: How to contact support\n"
            "- `/collab`: Information for collaboration inquiries\n"
            "- `/language`: Guide to changing keyboard language\n"
            "- `/spreadsheet`: Link to JoMama's spreadsheet\n"
            "- `/help`: Display this help message"
        )
        await interaction.response.send_message(response)

    # commands
    bot.tree.add_command(via)
    bot.tree.add_command(support)
    bot.tree.add_command(collab)
    bot.tree.add_command(language)
    bot.tree.add_command(spreadsheet)
    bot.tree.add_command(help_command)