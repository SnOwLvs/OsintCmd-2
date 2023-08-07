Répertoire des meilleurs Tools d'Osint dans le CMD. 


Comment le lancer ? 
-Installer Python 
-Exécuter le code avec cmd 
-Dans cmd marquer : py Osint.py

interface en ligne de commande (CLI) pour accéder à une liste d'outils OSINT
 (Open Source Intelligence) utilisés pour collecter et analyser des informations
 à partir de sources ouvertes sur Internet. L'objectif principal de l'interface est
 de fournir une manière conviviale de choisir un outil à exécuter et de présenter des
 informations sur cet outil. Voici une explication détaillée de ce que fait ce code :

    Importation de modules :
        os: Fournit des fonctionnalités liées au système d'exploitation, bien que
 dans ce code, il ne soit pas utilisé directement.
click: Un module Python utilisé pour créer des interfaces en ligne
 de commande de manière simple et élégante.
colorama: Un module utilisé ici pour ajouter des couleurs au texte dans
 la console.

    Initialisation de Colorama :
    Le code initialise le module Colorama pour que les couleurs appliquées au
 texte soient automatiquement réinitialisées après chaque utilisation.

    Définition d'une liste d'outils OSINT :
    La variable TOOLS contient une liste de dictionnaires, où chaque dictionnaire
 représente un outil OSINT avec des détails tels que le nom, l'URL, et les descriptions
 en anglais et en français.

    Définition de la fonction print_header() :
    Cette fonction affiche un texte stylisé qui semble être une sorte de bannière 
pour cette interface. Le texte est affiché en couleur cyan pour le nom "By SnowFish" 
et en couleur rouge pour le reste du texte.

    Définition de la fonction main() :
    Cette fonction est le point d'entrée de l'application. Elle efface l'écran de la 
console, affiche l'en-tête avec print_header(), puis entre dans une boucle infinie qui 
affiche les choix disponibles pour les outils OSINT.
        Elle affiche la liste des outils avec leurs noms et attribue un numéro à chaque 
outil.
        L'utilisateur peut choisir un outil en saisissant le numéro correspondant.
        Si l'utilisateur choisit "0", l'application se termine.
        Si l'utilisateur choisit un numéro valide, l'application affiche des informations 
détaillées sur l'outil en anglais et en français, ainsi que l'option d'ouvrir l'URL de 
l'outil dans le navigateur.

    Exécution du script :
    La condition if __name__ == "__main__": permet d'exécuter la fonction main() 
lorsque le script est exécuté directement (plutôt que lorsqu'il est importé comme module).

En résumé, ce code est une interface en ligne de commande pour explorer et utiliser
divers outils OSINT. L'utilisateur peut choisir un outil spécifique et en savoir plus 
à son sujet, puis même ouvrir l'URL associée à l'outil dans le navigateur.
