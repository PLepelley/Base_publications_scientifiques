# Base_publications_scientifiques

## Contexte du projet  
Il s’agit de créer une base Mongo, une collection, d’y insérer des données et de l’interroger grâce à Python. Les documents fournis correspondent à un extrait d’une base de publications scientifiques, The DBLP Computer Science Bibliography.


Pour commencer, vérifier les conteneurs actifs :
`sudo docker ps`  

Pour activer un conteneur  
`sudo docker start mongodb` (nom du conteneur)   


### Créer la base DBLP, ajouter une collection publis et importer dans la base les données du fichier dblp.json

1. Copier le fichier json dans le conteneur  
`sudo docker cp dblp.json bfe323305ac2:/dblp.json`  

2. Importer la bdd   
`sudo docker exec -it mongodb mongoimport --db=DBLP --collection=publis --file=dblp.json -u=root --authenticationDatabase=admin -p=`  

3. Vérification de la bdd dans le terminal  
`show dbs`  
`use publis`  

4. Création d'une classe DataAccess pour se connecter à la base de données, et des méthodes pour interroger la bdd  

5. Création d'un fichier data.py qui appelle les méthodes de la classe   
