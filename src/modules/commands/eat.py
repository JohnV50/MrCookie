import discord
from resources.mrcookie import instance as bot

from resources.checks import lookup_database, new_database, update_value

@bot.command()
async def eat(ctx):
    try:
        userID = str(ctx.author.id)
        guildID = ctx.guild.id

        ## this block fetches user data from the database
        userData = await lookup_database(userID, guildID) 
        if userData == False:
            await new_database(userID, guildID)
            userData = await lookup_database(userID, guildID)
        
        cookies = userData["users"][userID]["Cookies"] 
        if cookies < 1:
            raise Exception("You have no cookies to eat!")
        else:
            cookies -= 1
            await update_value(userID, guildID, "Cookies", cookies)
            await ctx.send("Nom nom, you ate 1 cookie 🍪")

    except Exception as Error:
        await ctx.send(Error)