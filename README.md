# PROJET LIME_ Bloc 1 :  

Vidéo de présentation : https://share.vidyard.com/watch/RGUzTUkG67r1DufgkPWrFV (Durée : 9mn55)  
Mon adresse mail : datayannick@gmail.com  
Linkdln : https://linkedin.com/in/yannick-icard  

## _Présentation de Lime :_      

Lime est une société de location de matériel de transport en libre-service basée aux États-Unis et créée en janvier 2017.
Lime est présente dans une vingtaine de villes en Europe et au Canada.  

## _Le projet :_  

Lime souhaite s'implanter à Paris où Vélib' à le monopole. Afin de déterminer les emplacements les plus rentables, les équipes techniques de LIME ont besoin de connaitre en temps réel les quais disponibles et les vélos disponibles par stations vélib'.  

## _L'ojectif :_    

Récupérez les données en temps réel des stations Velib  
Créer une infrastructure qui puisse fournir du temps réel  
Mettre à disposition un outil de visualisation pour voir sur une carte où les vélos LIME devraient être.






## _PIPELINE :_    

![image](https://user-images.githubusercontent.com/98116639/191927823-621269fe-4d22-4da0-8773-c036c9057224.png)

_<ins>En savoir plus :</ins>_  

__Velib :__   
Connexion à l'API vélib pour récupérer la data.

__Kafka :__   
Maitre d'orchestre de mon processus ETL, Kafka produit la donnée (Producer) pour alimenter la base de donnée PostegreSQL (Consumer).
Le setup du cluster Kafka a été paramétré grâce à Confluent.

__Heroku Postegre:__  
La base de donnée PostegreSQL est hébergée sur Heroku ce qui nous permet d'y avoir accès à tous moment sans serveur local.
Le choix de Heroku Postegre a été orienté par une question de coût.
L'alternative à Heroku Postgre aurait été de récupérer la donnée, la nettoyer et la transformer d'un Data Lake à un Data Warehouse grâce à AWS, Azur ou GCP. 

__Zapier :__    
Zapier est une plateforme no code qui permet d'automatiser des Workflows.

__Google sheet :__  
Google sheet est idéal pour la synchronisation.  
La relation entre ma base PostegreSQL et Google Sheet se fait avec très peu de paramètrage et de plus, l'URL de ma Google Sheet permet d'alimenter PowerBI.

__PowerBI :__    
C'est un outils de Data Visualisation très puissant, leader sur le marché avec Tableau Sotfware. Contrairement à Tableau, PowerBI permet d'accéder gratuitement à Google Sheet et d'avoir une visualisation sur une carte. 
Une alternative aurait été d'utiliser une librairie dans Python comme MatplotLib mais dans notre cas, PowerBI est intuitif, performant et adapté aux besoins de LIME. 
