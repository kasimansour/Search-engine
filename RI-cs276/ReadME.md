# GUIDE D'UTILISATION DU MOTEUR DE RECHERCHE CS-276

Ce readme a pour but de guider l'utilisation do moteur de recherche fait pour la collection cs276.

## 1. Prérequis

Le projet est fait en python 3. Voici la liste des librairies à installer:

* matplotlib
* nltk

Les autres librairies utilisées sont des librairies incorporées de base dans python.

## 2. Utilisation

Afin de faire marcher le code, il faut ouvrir le fichier Main.py dans l'IDE de votre choix et décommenter la partie que vous souhaitez faire fonctionner. 

Par exemple pour avoir la réponse aux questions 3 et 4, décommentez le code correspondant aux questions 3 et 4. 
Pour faire fonctionner le moteur de recherche booléen, décommentez le code suivant :

```
boolean_query()
```
Après l'apparition de "Type your serach here" en ligne de commande, vous pouvez taper votre recherche booléenne sous FNC.

De même pour faire fonctionner le moteur de recherche vectoriel, décommentez le code suivant : 

```
vectorial_query()
```
Après l'apparition de "Type your serach here", vous pouvez taper votre recherche.

Si l'index est déjà créé et stocké sur le disque vous pouvez directement taper votre recherche, sinon il faut attendre que le programme créé l'index et le stocke sur le disque.