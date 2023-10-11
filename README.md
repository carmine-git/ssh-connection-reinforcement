# Projet de Sécurisation d'un accès SSH

## Cahier des Charges

### Problèmatique

Comment ajouter une couche de sécurité pour une connexion SSH ?

### Fourniture

- 3 personnes : Talal, Lukmane, Vincent
- 2 VM (Virtual Machine)

### Budget

0 $

---

# Procédure

[Source des hypothèses](https://www.rcdevs.com/fr/7-ways-to-secure-your-ssh-server/)

1. Utiliser des connexions basées sur la clé publique SSH :
   pour cela, il faut générer une paire de clés à l'aide de la commande "ssh-keygen" à partir de la machine Linux, Windows ou Mac ensuite, il faut entrer le chemin d'accès au fichier dans lequel on veux enregistrer la clé.

   Exemple :

   ```sh
   ~$ ssh-keygen -t rsa -b 3072 -c
   ```

l'option `-t` permet de donner un nom à l'algorithme, ici c'est `rsa`. l'option `-b` permet de définir le nombre de bits dans la création de la clé, ici c'est `3078` car pour une clé RSA, généralement on peut mettre 1024 bits au minimum mais par default 3072 bits est considéré comme suffisant l'option `-c` permet de donner un commantaire

## Mise en pratique

## Conclusion
