[TODO]: # (Continuer le fichier markdown) 
[TODO]: # (Setup les deux machines virtuels)
[TODO]: # (Implémenter la connexion 2FA)
[TODO]: # (Tester le ficher d'installation)


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

<!---
Essaye d'utiliser "``" (sans les guillemets) pour surligner les options de la commandes.
Tu peux aussi tout écrire sur la même ligne, c'est plus propre et plus pro.

Si tu veux faire une liste avec des lettres utilise ces balises HTML.
<ol type="a">
    <li>truc</li>
    <li>machin</li>
</ol>
--->

   Informations ci-dessus :

   - l'option " -t " permet de donner un nom à l'algorithme, ici c'est " rsa "

   - l'option " -b " permet de définir le nombre de bits dans la création de la clé, ici c'est " 3072 " car pour une clé RSA,

     généralement on peut mettre 1024 bits au minimum mais par default 3072 bits est considéré comme suffisant

   - l'option " -c " permet de donner un commantaire 


## Mise en pratique 

a) 

b) 

## Conclusion
