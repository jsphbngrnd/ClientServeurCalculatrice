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

# Addition

if valeur3 == "+":
    resultadd = valeur1 + valeur2
    print(resultadd)

# Soustraction

elif valeur3 == "-":
    resultsub = valeur1 - valeur2
    print(resultsub)

# Multiplication

elif valeur3 == "*":
    resultmult = valeur1 * valeur2
    print(resultmult)

# Division

elif valeur3 == "/":
    resultdiv = valeur1 / valeur2
    print(resultdiv)

# Autre entrée

else:
    print("Invalide")

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
