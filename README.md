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

Source des hypothèses : [clic-ici](https://www.rcdevs.com/fr/7-ways-to-secure-your-ssh-server/)

1) Utiliser des connexions basées sur la clé publique SSH :
   pour cela, il faut générer une paire de clés à l'aide de la commande "ssh-keygen" à partir de la machine Linux, Windows ou Mac
   ensuite, il faut entrer le chemin d'accès au fichier dans lequel on veux enregistrer la clé


   ```sh
   [root@webcadmin1 tmp]# ssh-keygen -t rsa -b 2048 -c
   Generating public/private rsa key pair.
   Enter file in which to save the key (/root/.ssh/id_rsa):/root/.ssh/id_rsa2
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   
   The key fingerprint is:
 
   The key's randomart image is:
   
   ```


2)

## Mise en pratique 

a) approche théorique :

b) mise en oeuvre :

## Conclusion




