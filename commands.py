from ezcord import discord
from ezcord.internal.dc import commands

def setup(bot):
    @bot.command()
    async def via(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            return
        response = (
            "Here's how to set up VIA:\n"
            "[Find the .json here](<https://epomaker.com/blogs/via-json>)\n"
            "[usevia.app](<https://usevia.app/>)\n"
            "https://cdn.discordapp.com/attachments/850980474028687371/1367965498007883796/via.mp4\n"
            " \n"
            "Or follow this guide: https://discord.com/channels/726610136084250764/1390653548475318367"
        )
        await ctx.send(response)

    @bot.command()
    async def support(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            return
        response = (
            "If customer support is needed please Email:\n"
            "**support@epomaker.com**\n"
            " \n"
            "**For a support regarding keyboard troubleshooting and specific keyboard questions please ask your question by posting in** https://discord.com/channels/726610136084250764/1020599685930549289\n"
            " \n"
            "We ask that you refrain from pinging Epomaker, Epomaker Staff, and Moderators as they will respond to your inquiry as soon as they see it."
        )
        await ctx.send(response)

    @bot.command()
    async def collab(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            return
        response = (
            "# For Collaboration Inquiries:\n\n"
            "- **YouTube, TikTok, Facebook, PR**: Please contact the Marketing team via email.: marketing@epomaker.com\n\n"
            "- **Twitter, Instagram**: Feel free to DM our official accounts directly.\n\n"
            "- **For collaborations related to Discord, Facebook groups, or any community**: Please DM <@*epomakersupport*>\n\n"
            "- **For any collaborations related to exhibitions, events, or sponsorships**: Please contact the Marketing team via email. (marketing@epomaker.com)\n\n"
            "- **To apply as a reviewer in our Discord server**: Please check out https://discord.com/channels/726610136084250764/1309443436742443048  https://discord.com/channels/726610136084250764/1392065267055460403 and make sure to pay attention to the pinned messages."
        )
        await ctx.send(response)

    @bot.command()
    async def language(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            return
        response = (
            "To change the language of your keyboard, please follow these steps:\n"
            " \n"
            "https://cdn.discordapp.com/attachments/915825857635975198/1427789606962855976/1231.mp4"
        )
        await ctx.send(response)

    @bot.command(aliases=['list','ref'])
    async def spreadsheet(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            return
        response = (
            "Here is JoMama's [spreadsheet for Keyboards and Switches](https://docs.google.com/spreadsheets/d/1Otv49VQ1uQ3dLBgFrd623c7ceAWgCqu6s20mSKxfZUg/edit?pli=1&gid=0#gid=0)"
        )
        await ctx.send(response)

    @bot.command()
    async def help(ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            return
        response = (
            "Here are the available commands:\n"
            "- `!via`: Instructions for setting up VIA\n"
            "- `!support`: How to contact support\n"
            "- `!collab`: Information for collaboration inquiries\n"
            "- `!language`: Guide to changing keyboard language\n"
            "- `!spreadsheet` (or `!list`, `!ref`): Link to JoMama's spreadsheet for keyboards and switches\n"
            "- `!help`: Display this help message"
        )
        await ctx.send(response)