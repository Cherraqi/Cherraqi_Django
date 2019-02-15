Creer 3 pipelines
NOM_PROJET_ENV
Ex : Metesreau_Django_Dev
Pour chaque pipelines
- Recuperer le code source depuis 
le depot central sur la bonne branche
- Declenchement */5 * * * *
- 3 etapes
-- 
Etape de build
---- Etape 1 - Run script shell : 
faire tourner les tests
---- Etape 2 - Run script shell :  
echo "deploiement (indiquer l'env)"
Apres build
---- Etape 3 - Import test result : 
importer le resultat des tests
