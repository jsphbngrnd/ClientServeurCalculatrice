import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

# On input les différentes valeurs pour l'opération et on encode

# Valeur numérique 1
valeur1 = input("Valeur 1 = ").encode()

# Valeur numérique 2
valeur2 = input("Valeur 2 = ").encode()

# Symbole de l'opération
valeur3 = input("Valeur 3 = ").encode()

# On envoie les différentes valeurs au serveur

connexion_avec_serveur.send(valeur1)
connexion_avec_serveur.send(valeur2)
connexion_avec_serveur.send(valeur3)

# On print la valeur reçue par le serveur en décodant

print(connexion_avec_serveur.recv(1).decode())

print("Fermeture de la connexion")
connexion_avec_serveur.close()
