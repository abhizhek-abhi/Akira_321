import os
import json
import random

# Pokémon Categories
SAFARI = set([])
NEST_BALL = set([])
ULTRA_BALL = set([])
GREAT_BALL = set([])
REGULAR_BALL = set([
    "Abra", "Accelgor", "Aerodactyl", "Alcremie", "Amaura", "Ampharos", "Anorith", "Applin", "Archen", "Arctovish",  
    "Arctozolt", "Arrokuda", "Avalugg", "Axew", "Bagon", "Barraskewda", "Basculin", "Beedrill", "Beldum", "Blissey",  
    "Bounsweet", "Braixen", "Brionne", "Buizel", "Bulbasaur", "Buneary", "Carkol", "Charmander", "Charmeleon",  
    "Chespin", "Chewtle", "Chimchar", "Cinccino", "Clauncher", "Clawitzer", "Combusken", "Corvisquire", "Croagunk",  
    "Croconaw", "Cryogonal", "Cufant", "Cutiefly", "Cyndaquil", "Darmanitan", "Dartrix", "Deino", "Delphox",  
    "Dhelmise", "Dracovish", "Dracozolt", "Dragonair", "Drakloak", "Drampa", "Dratini", "Drilbur", "Drizzile",  
    "Druddigon", "Ducklett", "Dunsparce", "Duraludon", "Durant", "Dwebble", "Electrike", "Espeon", "Farfetch'd",  
    "Fennekin", "Ferroseed", "Feraligatr", "Flaaffy", "Flabebe", "Flapple", "Flareon", "Fletchinder", "Fletchling",  
    "Floatzel", "Floette", "Fraxure", "Frillish", "Froslass", "Gabite", "Gastly", "Gible", "Gligar", "Golbat",  
    "Golett", "Goomy", "Gourgeist", "Greavard", "Greninja", "Grimer", "Grookey", "Grovyle", "Growlithe", "Gurdurr",  
    "Hakamo-o", "Hatenna", "Hattrem", "Haunter", "Hawlucha", "Heliolisk", "Helioptile", "Herdier", "Horsea",  
    "Houndour", "Honedge", "Impidimp", "Ivysaur", "Jangmo-o", "Jolteon", "Joltik", "Kadabra", "Karrablast",  
    "Kingdra", "Kirlia", "Kleavor", "Krokorok", "Lampent", "Lanturn", "Lapras", "Larvesta", "Lillipup", "Litleo",  
    "Litten", "Litwick", "Lombre", "Lotad", "Lucario", "Ludicolo", "Magikarp", "Mankey", "Manectric", "Mareanie",  
    "Mareep", "Marowak", "Marshtomp", "Meowth", "Mienshao", "Mienfoo", "Mimikyu", "Monferno", "Morgrem", "Darumaka",  
    "Mr. Mime", "Mr. Rime", "Mudbray", "Mudkip", "Muk", "Ninetales", "Ninjask", "Noibat", "Noivern", "Oranguru",  
    "Orbeetle", "Overqwil", "Pancham", "Passimian", "Perrserker", "Phantump", "Pidgeotto", "Pidgey", "Pidove",  
    "Pignite", "Pikipek", "Piplup", "Popplio", "Ponyta", "Porygon", "Porygon-Z", "Porygon2", "Primeape", "Prinplup",  
    "Pumpkaboo", "Pyroar", "Quiladin", "Quilava", "Raboot", "Ralts", "Rhydon", "Rhyhorn", "Ribombee", "Rillaboom",  
    "Riolu", "Rolycoly", "Rotom", "Rookidee", "Rowlet", "Rufflet", "Salamence", "Salandit", "Sandile", "Scorbunny",  
    "Scraggy", "Scyther", "Seadra", "Shelgon", "Shellder", "Shelmet", "Sizzlipede", "Skiddo", "Skorupi", "Slakoth",  
    "Sliggoo", "Sneasel", "Sneasler", "Sobble", "Spiritomb", "Stantler", "Staravia", "Starly", "Starmie", "Staryu",  
    "Steenee", "Swampert", "Swanna", "Sylveon", "Talonflame", "Tauros", "Teddiursa", "Tentacool", "Tentacruel",  
    "Tepig", "Thwackey", "Timburr", "Togekiss", "Togepi", "Togetic", "Torchic", "Torracat", "Totodile", "Toxapex",  
    "Tranquill", "Treecko", "Trevenant", "Trumbeak", "Turtonator", "Turtwig", "Tyrunt", "Unfezant", "Ursaring",  
    "Vaporeon", "Vigoroth", "Vikavolt", "Volcarona", "Voltorb", "Vullaby", "Vulpix", "Wartortle", "Wimpod",  
    "Wishiwashi", "Wyrdeer", "Yamper", "Haxorus", "Zorua", "Zubat", "Zweilous"
])

REPEAT_BALL = set([
        "Abomasnow", "✨"
])

TEMP_DOWNLOAD_PATH = "./downloads"

# Owner and Bot Information
OWNER_NAME = "Aron"
BOT_VERSION = "69.2"
ALIVE_IMG_PATH = "https://envs.sh/INk.mp4"

# Commands
PING_COMMAND_REGEX = r'^\.ping$'
ALIVE_COMMAND_REGEX = r'^\.alive$'
HELP_COMMAND_REGEX = r'^\.help(?: (.*))?$'
EVAL_COMMAND_REGEX = r'^\.eval (.+)'
GUESSER_COMMAND_REGEX = r'^\.guess (on|off|stats)$'
HUNTER_COMMAND_REGEX = r'^\.hunt (on|off|stats)$'
LIST_COMMAND_REGEX = r'^\.list(?:\s+(\w+))?$'  # Now supports `.list <category>`

# AFK Commands
AFK_COMMAND_REGEX = r'^\.afk(?: |$)(.*)'  # Matches `.afk` or `.afk <message>`
UNAFK_COMMAND_REGEX = r'^\.unafk$'  # Matches `.unafk`

# Timing and Limits

COOLDOWN = lambda: random.randint(2, 3)  # Random cooldown between 3 and 6 seconds
PERIODICALLY_GUESS_SECONDS = 20  # Guess cooldown
PERIODICALLY_HUNT_SECONDS = 160  # Hunt cooldown (5 minutes)
HEXA_BOT_ID = 572621020  # ID of the Hexa bot

# Auto-Battle Constants
HUNT_DAILY_LIMIT_REACHED = "Daily hunt limit reached. Auto-battle stopped."
SHINY_FOUND = "Shiny Pokémon found! Auto-battle stopped for {0}."

# API Credentials
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION = os.getenv('SESSION')

# Chat ID
CHAT_ID = int(os.getenv('CHAT_ID'))

# Load Pokémon Data
with open('pokemon.json', 'r') as f:
    POKEMON = json.load(f)

__version__ = '1.0.0'
