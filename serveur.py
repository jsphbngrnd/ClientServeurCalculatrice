import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

valeur1 = connexion_avec_client.recv(1)  # réception de la première valeur
valeur2 = connexion_avec_client.recv(1)  # réception de la deuxième valeur
valeur3 = connexion_avec_client.recv(1)  # réception de la troisième valeur


print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
