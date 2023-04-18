# My Sokoban

Le Sokoban est un jeu de puzzle. L’objectif est de déplacer des caisses à travers un
entrepôt pour les emmener a une place définie dans cet entrepôt. Les caisses peuvent
être poussées mais pas tirées, donc le joueur doit bien anticiper ses mouvements pour
ne pas coincer une caisse contre un mur ou dans un angle. Une caisse peut être rangée
sur n’importe quel emplacement disponible dans l'entrepôt. Une caisse rangée peut tout
de même être déplacée à nouveau si le joueur la pousse ailleurs. La partie se termine
quand toutes les caisses sont rangées.

### Job
En utilisant la bibliothèque PyGame, développer un jeu de Sokoban. Le joueur doit
pouvoir utiliser les flèches directionnelles pour déplacer son personnage et pour
pousser les caisses. Un bouton cliquable et une touche clavier doivent être prévus pour
réinitialiser la partie.  

Ajouter également différents éléments tels que:
- Une touche pour annuler le dernier mouvement
- De la musique
- Des sons spécifiques pour certaines actions
- Un système de classement sauvegardé dans une base de données
- Un éditeur de map  

Le développement du jeu doit respecter quelques étapes :
1. Réaliser un modèle de données (architecture de classe, création de maps…)
2. Créer une boucle de jeu ainsi qu’une boucle d'évent clavier
3. Représenter graphiquement le jeu avec l’aide de la librairie Pygame
