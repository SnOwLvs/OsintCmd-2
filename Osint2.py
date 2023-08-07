import os
import sys
import click
from colorama import init, Fore
init(autoreset=True)
# By SnowFish
TOOLS = [
    {
        'name': 'Censys',
        'description_en': "Censys is a platform that enables researchers to discover, monitor, and analyze devices that are accessible from the internet.",
        'description_fr': "Censys est une plateforme qui permet aux chercheurs de découvrir, surveiller et analyser les appareils accessibles depuis Internet.",
        'url': 'https://censys.io/'
    },
    {
        'name': 'Epieos',
        'description_en': "Epieos is a web-based OSINT tool that helps to gather information about a target's online presence.",
        'description_fr': "Epieos est un outil OSINT basé sur le web qui aide à rassembler des informations sur la présence en ligne d'une cible.",
        'url': 'https://epieos.com/'
    },
    {
        'name': 'Holehe',
        'description_en': "Holehe is an information gathering tool that helps to gather data from social media platforms about a target.",
        'description_fr': "Holehe est un outil de collecte d'informations qui aide à rassembler des données à partir de plates-formes de médias sociaux sur une cible.",
        'url': 'https://github.com/megadose/holehe'
    },
    {
        'name': 'Invid',
        'description_en': "Invid is a web-based tool that helps to verify and analyze online videos and images.",
        'description_fr': "Invid est un outil basé sur le web qui aide à vérifier et analyser les vidéos et les images en ligne.",
        'url': 'https://invid.app/'
    },
    {
        'name': 'Intel Techniques',
        'description_en': "Intel Techniques is a collection of OSINT tools and resources for online investigations.",
        'description_fr': "Intel Techniques est une collection d'outils et de ressources OSINT pour les enquêtes en ligne.",
        'url': 'https://inteltechniques.com/'
    },
    {
        'name': 'Maigret',
        'description_en': "Maigret is a tool for investigating social media profiles by gathering information about a target's online presence.",
        'description_fr': "Maigret est un outil d'enquête sur les profils de médias sociaux en collectant des informations sur la présence en ligne d'une cible.",
        'url': 'https://github.com/soxoj/maigret'
    },
    {
        'name': 'Maltego',
        'description_en': "Maltego is a data visualization and investigation tool that helps to understand the relationships between pieces of information.",
        'description_fr': "Maltego est un outil de visualisation et d'investigation de données qui aide à comprendre les relations entre les informations.",
        'url': 'https://www.maltego.com/'
    },
    {
        'name': 'Osint Framework',
        'description_en': "Osint Framework is a collection of various OSINT tools for information gathering.",
        'description_fr': "Osint Framework est une collection de divers outils OSINT pour la collecte d'informations.",
        'url': 'https://osintframework.com/'
    },
    {
        'name': 'Sherlock',
        'description_en': "Sherlock is a tool for finding social media profiles by username across various online platforms.",
        'description_fr': "Sherlock est un outil pour trouver des profils de médias sociaux par nom d'utilisateur sur différentes plateformes en ligne.",
        'url': 'https://github.com/sherlock-project/sherlock'
    },
    {
        'name': 'Shodan',
        'description_en': "Shodan is a search engine for internet-connected devices. It allows users to find specific types of devices, vulnerabilities, and more.",
        'description_fr': "Shodan est un moteur de recherche pour les appareils connectés à Internet. Il permet aux utilisateurs de trouver des types spécifiques d'appareils, des vulnérabilités, et plus encore.",
        'url': 'https://www.shodan.io/'
    },
    {
        'name': 'SpiderFoot',
        'description_en': "SpiderFoot is an open-source OSINT automation tool that helps you to automate the process of gathering intelligence about a target.",
        'description_fr': "SpiderFoot est un outil d'automatisation OSINT open-source qui vous aide à automatiser le processus de collecte de renseignements sur une cible.",
        'url': 'https://www.spiderfoot.net/'
    },
    {
        'name': 'h8mail',
        'description_en': "h8mail is an email OSINT and breach hunting tool that helps to find compromised email accounts.",
        'description_fr': "h8mail est un outil OSINT d'analyse d'emails et de recherche de violations qui aide à trouver des comptes email compromis.",
        'url': 'https://github.com/khast3x/h8mail'
    }
]
# By SnowFish
INTRO_TEXT = Fore.MAGENTA + '''
  .-')        .-') _                (`\ .-') /`                     .-')                 .-') _  .-') _    
 ( OO ).     ( OO ) )                `.( OO ),'                    ( OO ).              ( OO ) )(  OO) )   
(_)---\_),--./ ,--,'  .-'),-----. ,--./  .--.         .-'),-----. (_)---\_)  ,-.-') ,--./ ,--,' /     '._  
/    _ | |   \ |  |\ ( OO'  .-.  '|      |  |        ( OO'  .-.  '/    _ |   |  |OO)|   \ |  |\ |'--...__) 
\  :` `. |    \|  | )/   |  | |  ||  |   |  |,       /   |  | |  |\  :` `.   |  |  \|    \|  | )'--.  .--' 
 '..`''.)|  .     |/ \_) |  |\|  ||  |.'.|  |_)      \_) |  |\|  | '..`''.)  |  |(_/|  .     |/    |  |    
.-._)   \|  |\    |    \ |  | |  ||         |          \ |  | |  |.-._)   \ ,|  |_.'|  |\    |     |  |    
\       /|  | \   |     `'  '-'  '|   ,'.   |           `'  '-'  '\       /(_|  |   |  | \   |     |  |    
 `-----' `--'  `--'       `-----' '--'   '--'             `-----'  `-----'   `--'   `--'  `--'     `--'    
'''
# By SnowFish
def print_main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran de la console
    print(INTRO_TEXT)
    print(Fore.RED + "Bienvenue dans l'interface OSINT !")
    for index, tool in enumerate(TOOLS, start=1):
        if tool['name'] != "Invid":
            print(Fore.YELLOW + f"{index: <3}) {tool['name']}")
# By SnowFish
    print(Fore.RED + f"\n 0) Quitter")
    choice = click.prompt(Fore.RED + "\nChoisissez un outil (1-12)", type=int, default=0, show_default=False)
    # By SnowFish
    if choice == 0:
        print(Fore.RED + "Au revoir !")
        sys.exit(0)
# By SnowFish
    if 1 <= choice <= len(TOOLS):
        tool = [t for t in TOOLS if t['name'] != "Invid"][choice - 1]
        show_tool_details(tool)
    else:
        print(Fore.RED + "Choix invalide.")
# By SnowFish
def show_tool_details(tool):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran de la console
    print(INTRO_TEXT)
    print(Fore.RED + f"{tool['name']} - Description (English):")
    print(Fore.CYAN + tool['description_en'])
# By SnowFish
    print(Fore.RED + f"{tool['name']} - Description (Français):")
    print(Fore.CYAN + tool['description_fr'])
# By SnowFish
    open_url = click.confirm(Fore.YELLOW + "Voulez-vous ouvrir l'URL de l'outil dans le navigateur ?", default=True)
    if open_url:
        click.launch(tool['url'])
        print(Fore.GREEN + f"L'URL a été ouverte dans le navigateur.")
    else:
        print(Fore.YELLOW + "Opération annulée.")
    
    back_to_main_menu = click.confirm(Fore.YELLOW + "Retourner au menu principal ?", default=True)
    if back_to_main_menu:
        print_main_menu()
    else:
        print(Fore.RED + "Au revoir !")
        sys.exit(0)
# By SnowFish
@click.command()
def main():
    while True:
        print_main_menu()
# By SnowFish
if __name__ == "__main__":
    main()
