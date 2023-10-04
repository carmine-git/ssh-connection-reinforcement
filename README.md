<!---
TODO: 
- Redaction
 - Utilisation de titres (#), sous-titres (##) ou sous-sous-titres (###, etc.)
 - Merci de tout écrire en français pour eviter les erreurs d'incompréhension.
 - Ecrire le code ou les commandes utilisées directement sur le fichier sans prendre de photos d'écran
 - Spécifier aussi le langage si possible comme par ex.: ```py "le code" ```

- Procédure
 - Nous utiliserons Google authenticator pour implémenter la couche de sécurité
 - Vincent rédigera le PPT et le markdown.
 - Lukmane et vincent pourra setup une MV client et une MV serveur pour la connection SSH
 - Talal fera en sorte de setup la A2F sur la machine server.
 - Nous ferons en sorte que nous pouvons désactiver l'autentification a 2 facteurs.
--->

# Projet de Sécurisation d'un accès SSH

## Cahier des Charges 

### Problèmatique 
- Comment ajouter une couche de sécurité pour une connexion SSH ?

### Fourniture  
- 3 personnes : Talal, Lukmane, Vincent
- 2 VM (Virtual Machine)

### Budget  
- 0 $

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Parties 

## Hypothèse et Théories 

 [Source des hypothèses](https://www.rcdevs.com/fr/7-ways-to-secure-your-ssh-server/)

1) Utiliser des connexions basées sur la clé publique SSH :
   
   pour cela, il faut générer une paire de clés à l'aide de la commande "ssh-keygen" à partir de la machine Linux, Windows ou Mac
   
   ensuite, il faut entrer le chemin d'accès au fichier dans lequel on veux enregistrer la clé.

   Exemple :

   ```sh
   [root@webcadmin1 tmp]# ssh-keygen -t rsa -b 3072 -c 
   Generating public/private rsa key pair.
   Enter file in which to save the key (/root/.ssh/id_rsa):/root/.ssh/id_rsa2
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   ...
   The key fingerprint is:
   ...
   The key's randomart image is:
   ...
   
   ```
   Informations ci-dessus :

   - l'option " -t " permet de donner un nom à l'algorithme, ici c'est " rsa "

   - l'option " -b " permet de définir le nombre de bits dans la création de la clé, ici c'est " 3072 " car pour une clé RSA,

     généralement on peut mettre 1024 bits au minimum mais par default 3072 bits est considéré comme suffisant

   - l'option " -c " permet de donner un commantaire 


## Mise en pratique 

a) 

b) 

## Conclusion




