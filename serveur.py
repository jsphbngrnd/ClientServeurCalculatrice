import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

# réception de la première valeur

valeur1 = connexion_avec_client.recv(1).decode()

# réception de la deuxième valeur

valeur2 = connexion_avec_client.recv(1).decode()

# réception de la troisième valeur

valeur3 = connexion_avec_client.recv(1).decode()

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
