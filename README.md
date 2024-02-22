<div>
  <img src="/public/logo.png" style="height: 100px; width:100px;"/>
</div>

# Sécurisation d'une connnexion ssh vers un serveur

Ce dépot à pour but de vous aider a apporté une deuxième couche de sécurité pour votre serveur lors de connections SSH.

> **_ATTENTION:_** Ce dépôt n'est pas addressé aux utilisateurs de machines windows

## Générer une clé ssh

Pour pouvoir vous connecter à votre serveur via SSH, vous devez d'abords générer une clé SSH.
Pour ce faire, utilisez la commande `ssh-keygen` pour générer une clé.
On vous demandera dans quel répertoire stcoker la clé, mettez la où vous voulez.
Voici un exemple de la commande.

```sh
ssh-keygen -t rsa
```

on choisi l'algorithme de chiffrement rsa gràce à l'option `-t`

## Téléchargement du module d'authentification à 2 facteurs

Pour accéder à l'authentification à 2 facteurs nous installer le module suivant: Google Authenticator

Pour machines Debian/Ubuntu

```sh
sudo apt update && sudo apt-get install libpam-google-authenticator
```

Pour machines CentOS/RHEL

```sh
sudo yum install google-authenticator
```

## Installation du du module

Nous commençons la partie la plus dur du tutoriel mais rassurez-vous, nous avons fait les recherches à votre place!

Pour débutez l'installation, éxécuter la commande `google-authenticator`
Pendant l'installation vous aurez des options à lire, vous pouvez les approuvez ou les réfuser selon vos goûts.
Vous allez aussi recevoir un QR code générer par la commande. Flasher ce QR code dans l'application de votre choix

> **_ATTENTION:_** Merci de ne pas flasher le QR code via l'appareil photo de votre téléphone. Vous ne pourrez pas recevoir vos codes de sécurité de cette maniére

Afin que l'installation soit effective, vous allez devoir modifier quelque fichiers de configuration.
Le premier est le suivant.

```sh
sudo nano /etc/pam.d/sshd # ou vi pour les 🤓
```

ajouter en haut du fichier les deux lignes suivantes.

```txt
auth required pam_google_authenticator.so nullok
auth required pam_permit.so
```

sauvegarder et quitter le fichier.

le deuxième fichier va ouvrir la configuration du serveur SSH

```sh
sudo nano /etc/ssh/sshd_config
```

Ajouter ou modifier les lignes suivantes dans ce fichier

```txt
ChallengeResponseAuthentication yes
AuthenticationMethods publickey,password publickey,keyboard-interactive
```

redémmarer le service SSH

Pour machines Debian/Linux

```sh
sudo systemctl restart ssh
```

Pour machines CentOS/RHEL

```sh
sudo service sshd restart
```

## Tester la connection SSH

A cette étape, vous pouvez alors vous connecter via le serveur ssh en entrant son domaine généralement écris de cette manière [compte]@[adresse]
Lorsque vous avez tapé le mot de passe, vous pouvez alors taper le code de vérification générer automatiquement par votre application d'authentification.

## Application

[Sources](https://www.man7.org/linux/man-pages/man1/ssh-keygen.1.html)
[Sources](https://docs.github.com/fr/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases).
