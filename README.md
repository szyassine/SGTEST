# Python programme pour SG

## Resume du Programme

 1. Une fois le programme executé, il est demandé de fournir une indice boursière, que ca soit en majuscule ou en miniscule
 2. Le programme retourne le nom de la compagnie, et la dernière cote boursière a la fermeture.
 3. La librairie  urllib.request est utilisé pour la connexion au site web etc.
 4. La librairie json est aussi utilisé pour la gestion des données en JSON
 5. Un fichier requirement.txt pour les lib requis.

## Notions pas claire
 Puisque le nombre de stock que l'utilisateur n'a pas été demandé, j'ai utilisé une seule entrée.
 Par contre, on peut gerer cela avec plusieurs entrés et les mettres dans un tableau qu'on pourrait parcourir.
 J'ai afficher le nom de la compagnie et la dernière cote boursière.

## Atout
 J'ai programmer un programme similaire dans un de mes cours en language C, qui recupère une liste de cote boursière mis dans un fichier text. 
 Ensuite, un script télécharge les données json et les mets dans un dossier nommé data. Il recupère des données specifique de chacune des index,
 puis il calcul avec un algorithme, et affiche les indices en classement. Vue la similarité avec ce test, je pourrai vous donner accès puisque c'est un repo privé.

## Rappel des consignes
Python test 3:

Objective:
- The candidate has to do a python api to connect to "Yahoo Finance API Pricing" 
- Provided instrument's pricing through this python REST api
- When user send an intrument to the api, the api replied with the last close price.

Note:
- Basic cost is free for Pricing
- First 500 API calls is still free
- you shouldn't use yfinance module
- we will run your code in virtual env. Please ensure that you got everything need it in the git repo.

Requirement:
- python 3.7
- code versioning with git
- send code through github (please provide the link)