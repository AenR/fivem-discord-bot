from interactions import *
import interactions
import sqlite3

bot = Client(intents=Intents.DEFAULT)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS bot_settings (
    id INTEGER PRIMARY KEY,
    prefix TEXT,
    server_name,
    server_ip TEXT,
    ts3_ip TEXT,
    dc_link TEXT,
    server_logo TEXT
)
''')
conn.commit()

cursor.execute('SELECT * FROM bot_settings')
settings = cursor.fetchone()

if settings is not None:
    prefix = settings[1]
    server_name = settings[2]
    server_ip = settings[3]
    ts3_ip = settings[4]
    dc_link = settings[5]
    server_logo = settings[6]
else:
    prefix = "!"
    server_name = "AenR Fivem Sunucusu"
    server_ip = "aenrfivem"
    ts3_ip = "aenrts3"
    dc_link = "https://discord.gg/"
    server_logo = "https://media.discordapp.net/attachments/966752496410320967/1091863852632780830/tan-yellow-pp.png?width=662&height=662"

@listen()
async def on_ready():
    print("Bot ready")


@slash_command(name="aktif", description="Sunucunun aktif olduğunu belirtir.")
async def aktif_command(ctx: SlashContext):
    embed = Embed(
            title="Sunucu Aktif",
            description="Sunucuya Giris Yapabilirsiniz",
            color=0x4bb543)
    embed.set_author(name=server_name, icon_url=server_logo)
    embed.set_thumbnail(url="https://w7.pngwing.com/pngs/392/551/png-transparent-grand-theft-auto-five-illustration-grand-theft-auto-v-grand-theft-auto-san-andreas-gta-5-online-gunrunning-playstation-4-mod-gta-miscellaneous-emblem-label-thumbnail.png")
    embed.set_footer(text=f"IP: {server_ip} , TS3: {ts3_ip}")
    await ctx.send(embed=embed)

@slash_command(name="restart", description="Sunucunun yeniden başlatıldığını belirtir.")
async def restart_command(ctx: SlashContext):
    embed = Embed(title="Sunucu Yeniden Başlatılıyor.",
                  description="Sunucuya Giriş Yapmayınız.",
                  color=0x5bc0de)
    embed.set_author(name=server_name, icon_url=server_logo)
    embed.set_thumbnail(url="https://w7.pngwing.com/pngs/392/551/png-transparent-grand-theft-auto-five-illustration-grand-theft-auto-v-grand-theft-auto-san-andreas-gta-5-online-gunrunning-playstation-4-mod-gta-miscellaneous-emblem-label-thumbnail.png")
    embed.set_footer(text=f"IP: {server_ip} , TS3: {ts3_ip}")
    await ctx.send(embed=embed)

@slash_command(name="bakım", description="Sunucunun bakımda olduğunu belirtir.")
async def bakim_command(ctx: SlashContext):
    embed=Embed(title="Sunucu Bakımda.",
                description="Sunucumuz bakımdadır.",
                color=0xf0ad4e)
    embed.set_author(name=server_name, icon_url=server_logo)
    embed.set_thumbnail(url="https://w7.pngwing.com/pngs/392/551/png-transparent-grand-theft-auto-five-illustration-grand-theft-auto-v-grand-theft-auto-san-andreas-gta-5-online-gunrunning-playstation-4-mod-gta-miscellaneous-emblem-label-thumbnail.png")
    embed.set_footer(text=f"IP: {server_ip} , TS3: {ts3_ip}")
    await ctx.send(embed=embed)

@slash_command(name="dc", description="Discord sunucusunun linkini verir.")
async def dc_command(ctx: SlashContext):
    embed=Embed(title="Discord Linki",
                url=dc_link,
                color=0x332d2d)
    embed.set_author(name=server_name, icon_url=server_logo)
    embed.set_thumbnail(url="https://www.freepnglogos.com/uploads/discord-logo-png/concours-discord-cartes-voeux-fortnite-france-6.png")
    embed.set_footer(text=f"IP: {server_ip} , TS3: {ts3_ip}")
    await ctx.send(embed=embed)

@slash_command(name="ip", description="Sunucunun iplerini verir.")
async def dc_command(ctx: SlashContext):
    embed=Embed(title="Sunucu IP Adresi",
                color=0x332d2d)
    embed.set_author(name=server_name, icon_url=server_logo)
    embed.set_thumbnail(url="https://www.freepnglogos.com/uploads/discord-logo-png/concours-discord-cartes-voeux-fortnite-france-6.png")
    embed.add_field(name="Fivem IP", value=server_ip, inline=True)
    embed.add_field(name="TS3 IP", value=ts3_ip, inline=True)
    await ctx.send(embed=embed)

@interactions.slash_command(name="oylama", description="Bir oylama başlatır.",
    options=[
        {
            "name": "question",
            "description": "Oylama için bir soru girin.",
            "type": 3,
            "required": True
        }
    ]
)
async def oylama_command(ctx: interactions.SlashContext, question: str):
    embed = Embed(
        title="Yeni Oylama",
        description=question,
        color=0x332d2d
    )
    embed.set_author(name=server_name, icon_url=server_logo)
    embed.set_thumbnail(url="https://www.bedford.gov.uk/sites/default/files/2023-01/Bedford%20Borough%20Council%20Budget%20Consultation%20%2811%29.png")
    embed.set_footer(text=f"IP: {server_ip} , TS3: {ts3_ip}")

    message = await ctx.send(embed=embed)
    await message.add_reaction("👍")
    await message.add_reaction("👎")

bot.start("TOKEN")

@listen()
async def on_shutdown():
    conn.close()