import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

# Réception des valeurs et décodage

valeur1 = connexion_avec_client.recv(1).decode()
valeur2 = connexion_avec_client.recv(1).decode()
valeur3 = connexion_avec_client.recv(1).decode()


# Début de la calculatrice
# Addition

if valeur3 == "+":
    connexion_avec_client.send(str(int(valeur1) + int(valeur2)).encode())


# Soustraction

elif valeur3 == "-":
    connexion_avec_client.send(str(int(valeur1) - int(valeur2)).encode())


# Multiplication

elif valeur3 == "*":
    connexion_avec_client.send(str(int(valeur1) * int(valeur2)).encode())


# Division

elif valeur3 == "/":
    connexion_avec_client.send(str(int(valeur1) / int(valeur2)).encode())


# Autre entrée

else:
    connexion_avec_client.send("Invalide").encode()

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
