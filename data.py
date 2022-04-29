from connexion_mongodb import DataAccess
from pprint import pprint


#Compter le nombre de documents de la collection publis;
print(DataAccess.count_publis())

#Lister tous les livres (type “Book”)
#DataAccess.list_books()

#Lister les livres depuis 2014
#DataAccess.books_2014()

#Lister les publications de l’auteur “Toru Ishida”
#DataAccess.author_TI()

#Lister tous les auteurs distincts
#DataAccess.distinct_authors()

#rier les publications de “Toru Ishida” par titre de livre
#DataAccess.sort_title_TI()

#Compter le nombre de ses publications 
#print(DataAccess.count_pub_TI())

#Compter le nombre de publications depuis 2011 et par type 
#pprint(DataAccess.count_pub())

#Compter le nombre de publications par auteur et trier le résultat par ordre croissant
# pprint(DataAccess.count_pub_authors())
# DataAccess.close_connexion