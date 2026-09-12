# [SurvivalGame]

Jeu de survie multijoueur développé sous Unreal Engine 5 (Full BluePrint).

Suivi quotidien du développement sur TikTok : [@monjeuinde](https://www.tiktok.com/@monjeuinde)

## Sommaire

- [Présentation](#présentation)
  - [Multijoueur](#multijoueur)
  - [Collecte de ressources](#collecte-de-ressources)
  - [Inventaire](#inventaire)
  - [Hotbar](#hotbar)
  - [Items](#items)
  - [Sauvegarde](#sauvegarde)
  - [Climat & météo](#climat--météo)
  - [Statistiques du joueur](#statistiques-du-joueur)
  - [Heure in-game](#heure-in-game)
  - [Système de dégâts](#système-de-dégâts)
  - [Construction](#construction)
  - [Stations (craft & cuisson)](#stations-craft--cuisson)
  - [Craft](#craft)
  - [Map & minimap](#map--minimap)
  - [Grottes & carrières](#grottes--carrières)
  - [Architecture technique](#architecture-technique)
  - [Suivi & documentation du projet](#suivi--documentation-du-projet)
- [Comment jouer](#comment-jouer)
- [Licence](#licence)

## Présentation

### Multijoueur

- Jusqu'à 8 joueurs, entièrement synchronisé.
- Sauvegarde gérée uniquement côté host.

### Collecte de ressources

- Système de collecte basique : arbres et pierres à casser.
- Table de loot selon le type de ressource (plus une ressource est rare, plus elle a de PV, et plus le loot est important).
- Tables de loot entièrement modifiables.

### Inventaire

- Tous les inventaires (joueur, coffres, stations...) partagent les mêmes fonctionnalités.
- Tri rapide via un bouton dédié.
- Interaction entre inventaires par drag and drop.
- Transfert rapide via shift-clic.
- Double-clic sur un item pour regrouper les stacks.
- Touche `X` pour diviser un stack.
- Drop d'un item en dehors de l'inventaire.

### Hotbar

- 8 emplacements.
- Seuls les items autorisés (via tag) peuvent y être placés.

### Items

- Chaque item dispose d'un menu contextuel au clic droit.
- Actions implémentées : jeter, diviser.
- Actions prévues (non implémentées) : consommer, infos, réparer.

### Sauvegarde

- Système séparé en deux : sauvegarde joueurs et sauvegarde monde.
- Auto-save avec intervalle paramétrable.

### Climat & météo

- Le climat évolue en fonction de la déforestation (destruction des arbres).
- Météo dynamique changeant toutes les 30 minutes in-game (intervalle modifiable) : ensoleillé, nuageux, pluvieux, orageux.
- Basé sur Stylized Weather (Fab).
- Ambiance visuelle évoluant selon l'heure de la journée.

### Statistiques du joueur

- Oxygène, vie, eau, nourriture : statistiques indépendantes.
- Incrémentation/décrémentation par une valeur modifiable.

### Heure in-game

- Cycle horaire utilisé pour déclencher les changements météo et les sauvegardes automatiques.

### Système de dégâts

- Dégâts cohérents selon l'arme et la cible (ex : pioche efficace sur la pierre, hache efficace sur les arbres).

### Construction

- Catalogue de constructions disponibles, chacune avec un coût en matériaux.
- Placement libre par défaut, grille activable (touche `W`).
- Contrôles : clic gauche pour construire, `R` pour tourner, `X` pour réinitialiser la position, molette pour ajuster la hauteur.
- Placement intelligent basé sur des sockets : les pièces adjacentes s'alignent automatiquement (ex : un mur posé sur un sol se centre tout seul).
- Éléments disponibles : mur, sol, fenêtre, cadre de fenêtre, porte, cadre de porte, toit, demi-toit, fondations, escalier, mur triangulaire.
- Plusieurs types de matériaux (bois, pierre, métal) avec recettes personnalisables.
- Roue de construction (en plus du catalogue) : 8 emplacements configurables depuis le catalogue pour un placement rapide (maintien du clic gauche).

### Stations (craft & cuisson)

- Table de craft et four, avec recettes différentes selon la station et son tier.
- Le four nécessite un carburant, qui varie selon le tier de la station.
- Auto-cuisson : détection automatique des recettes réalisables.
- Système de file d'attente (queue).
- Gestion intelligente des ressources : priorité à l'inventaire de la station, puis à l'inventaire du joueur, avec transfert automatique si nécessaire.

### Craft

- Système de craft indépendant de celui des stations, avec ses propres recettes.

### Map & minimap

- Map et minimap fonctionnelles, minimap accessible via `Tab`.
- Plusieurs grottes et carrières.
- Modèles 3D de roches en partie récupérés sur Fab, arbres modélisés à la main.

### Grottes & carrières

- Plusieurs types de grottes et plusieurs minerais (fer, charbon, oxylite, cuivre).
- Taux d'apparition définis en base de données (ex : 25 % de chaque minerai dans une grotte T2).
- Génération aléatoire du type de roche sur des emplacements prédéfinis.
- Modèles de roches typés par minerai (ex : charbon).
- Nombre de particules aléatoire par roche.
- Placement aléatoire des emplacements via un algorithme de proximité et de gestion des collisions.
- Chaque minerai a un rendu visuel unique.

### Architecture technique

- Projet data-driven : dégâts, recettes, coûts, temps de construction et infos des items sont gérés en base de données.
- Utilisation de tags pour : le type de construction, le tier des stations, et les autorisations d'accès à la hotbar.

### Suivi & documentation du projet

- Utilisation de l'IA pour : la couverture TikTok, les discussions autour du projet, l'identification des points critiques et la planification, ainsi que la mise au propre de ce document.
- Documentation quotidienne du développement sur TikTok : [@monjeuinde](https://www.tiktok.com/@monjeuinde)

## Comment jouer

1. Rendez-vous dans la section [Releases](../../releases) du dépôt.
2. Téléchargez la dernière version disponible.
3. Décompressez l'archive et lancez l'exécutable.

## Licence

Voir le fichier [LICENSE](LICENSE) pour plus de détails.
