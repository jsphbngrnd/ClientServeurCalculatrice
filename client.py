import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

valeur1 = input("Valeur 1 = ").encode()
valeur2 = input("Valeur 2 = ").encode()
valeur3 = input("Valeur 3 = ").encode()

connexion_avec_serveur.send(valeur1)
connexion_avec_serveur.send(valeur2)
connexion_avec_serveur.send(valeur3)

print(connexion_avec_serveur.recv(1).decode())

print("Fermeture de la connexion")
connexion_avec_serveur.close()
