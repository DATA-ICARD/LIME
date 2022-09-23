![crack](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Lime_%28transportation_company%29_logo.svg/1200px-Lime_%28transportation_company%29_logo.svg.png)

# Urban Mobility with Lime

## Context 📇

Throughout the years, governments and companies led more and more [Open Data](https://opendatahandbook.org/guide/en/what-is-open-data/) projects. The goal is simple, providing free and updated sources of data for private companies to work on and bring growth to their country. 

One successful project is [City Mapper](https://citymapper.com/) that uses Open Data in Europe to help users navigate from point A to point B in a given city. 

Another project that can leverage Open Data is [Lime](https://www.li.me/en-co). As one of the first company to provide alternative urban transports (like scooters and electric bikes), one of the key component is to leverage data to know where to station their transports in a city. 

One way to do so is to leverage Open Data. Paris provides a real-time API that retrieve the current availabilities of Velib stations (the city's public bike-sharing service) and use that to know where Lime bikes should be in real-time to meet demands. 

## Project goals 🎯

As a Machine Learning Engineering team, you goal is to leverage Paris Open Data to:

* Retrieve real-time data from Velib stations 
* Create an infrastructure that ingest in real-time
* Provide a visualisation tool to see in a map where Lime bikes (and/or scooters) should be

## Where to get data 

To achieve this project, you will need to get access to some data! Here are data sources that can be of interest:

* [Velib availabilities real-time API](https://opendata.paris.fr/explore/dataset/velib-disponibilite-en-temps-reel/information/?disjunctive.name&disjunctive.is_installed&disjunctive.is_renting&disjunctive.is_returning&disjunctive.nom_arrondissement_communes)
    * the API is updated every minute, don't push real-time too far 😉

* [Velib Stations informations](https://opendata.paris.fr/explore/dataset/velib-emplacement-des-stations/information/)
    * This API provides information on any velib station 


## Deliverables 📬

To complete this project, you will need to produce:

* A schema of the infrastructure you chose to build and **why** you built it that way
    * This can be in a Powerpoint, Word document
    * You can get inspiration from the below picture 
    ![crack](https://lead-program-assets.s3.eu-west-3.amazonaws.com/M05-Projects/sample_data_infrastructure.png)

* The source code of all elements necessary to build your infrastructure 

* A video of your working infrastructure on an example
    * You can use [Vidyard](https://www.vidyard.com/) to do so 

## Tips 🦮

To help you in your task, we would like to give you a few tips on how to tackle that project. 

### I don't know where to start

First things first, in this project you need to at least:

* Collect data from an API
* Store the retrieved data in real-time
* Use that data to visualize it using any tool (like [plotly](https://plotly.com/) or [Tableau](https://www.tableau.com/))

This is our recommandation on where to start:

![basic_infrastructure](https://lead-program-assets.s3.eu-west-3.amazonaws.com/M05-Projects/sample_data_infrastructure_without_ml.png)


:::important 
The above example is just a suggestion, you can deviate from this infrastructure. The only minimal elements we need to have are:

* An element collecting & storing data
* An element consuming data 
* An ETL (or ELT) process
:::

### How do I split work among my teammates?

Working together is key here! You can split your work several ways, but here is a suggestion:

* One team member can retrieve data from the API and automate the process on Airflow
* One team member can consume and store data
* One team member can build all the visualisations