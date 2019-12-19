# ClientServeurCalculatrice
Une calculatrice client/serveur en python

# Pour initialiser la connexion

On lance le serveur pour qu'il soit en écoute.  
Ensuite on lance le client pour qu'il se connecte au serveur.

# Côté Client

## Étape 1

On input les valeurs pour l'opération de la calculette :  
_valeur1 = première valeur_  
_valeur2 = seconde valeur_  
_valeur3 = "+", "-", "*" ou "/"_  
On encode les trois valeurs avant de les envoyer avec .encode() .  

## Étape 2

Ensuite on se connecte avec le serveur et on envoie les trois valeurs.

## Étape 3

Enfin on print pour afficher le résultat renvoyé par le serveur que l'on décode.

# Côté Serveur

## Étape 1

On reçoit les trois valeurs envoyées par le client, il ne faut pas oublier de les décoder avec .decode() .  

## Étape 2

On créé la calculatrice et on effectue les calculs pour chaque cas de figure proposé par la **valeur3**.  
À chaque résultat on encode et on renvoie vers le client.

## Étape 3

Une fois les opération effectuées on ferme la connexion.  
