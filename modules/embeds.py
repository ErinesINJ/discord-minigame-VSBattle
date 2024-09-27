import discord

async def battleEmbed(player, opponent):
    embed = discord.Embed(title=f"", color=discord.Color.red())
    embed.set_image(url='https://cdn.discordapp.com/attachments/1124664448485953576/1201804342022381568/IMG_2333-1.png')
    embed.set_footer(text=f'You have 30 seconds to accept the duel...')
    
    return embed

async def battleWinner():
    embed = discord.Embed(title=f'', color=discord.Color.green())
    embed.set_image(url='https://cdn.discordapp.com/attachments/1124664448485953576/1209120081364262992/IMG_2595.png')
        
    return embed

async def acceptedDuel():
    embed = discord.Embed(title=f'', color=discord.Color.red())
    embed.set_image(url='https://cdn.discordapp.com/attachments/1124664448485953576/1201804349022670868/IMG_2502.png')
        
    return embed

async def duelEmbed(img_url):
    embed = discord.Embed(title='Name the weapon', color=discord.Color.red())
    embed.set_image(url=img_url)
    
    return embed


