import random

possibility = {
    "sword": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804341300953151/IMG_1758.png',
    "axe": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804340764102656/IMG_1756.png',
    "spear": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804340436672513/IMG_1755.png',
    "hammer": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804340088537129/IMG_1754.png',
    "bow": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804339732025404/IMG_1753.png',
    "club": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804338637582397/IMG_1750.png',
    "crossbow": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804339069599816/IMG_1751.png',
    "flail": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804339396743199/IMG_1752.png',
    "shield": 'https://cdn.discordapp.com/attachments/1124664448485953576/1201804338197176371/IMG_1749.png'
}

async def randomizer():
    random_item = random.choice(list(possibility.keys()))
    item_link = possibility[random_item]
    return random_item, item_link
