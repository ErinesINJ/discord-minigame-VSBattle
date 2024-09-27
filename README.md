# VS battle Discord Minigame
Source code contains discord based mini game called VS Battle.

# Usage
After correctly configuring the Discord bot, you can start a mini-game using the slash command ``/duel @discord_member``.

The bot will ping the selected player and display an option to accept or decline the challenge. Once the second player accepts, the game begins. The bot will display a picture of an item, and whoever types the correct name of the item first wins the duel!

You can edit the pictures of the items and their names in the ``modules/game.py`` file, and you can customize the images and descriptions of the embeds shown during the game in the ``modules/embeds.py`` file.

# Config
allowed_channel_id = allowed discord channel ID to interact with bot (int)
allowed_role_id = allowed discord role ID to interact with bot (int)
guild_id = discord server ID (int)
discord_bot_token = token to access your discord bot
