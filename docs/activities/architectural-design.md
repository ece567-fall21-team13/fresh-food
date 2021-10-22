# Architectural Design
The Architectural Design phase in the first iteration entails an abstract discussion of the basic building blocks for our system. 
The following action items were assigned the highest priority as much of subsequent development hinges on their completion:


## Choose a architecture and why - Monolithic, Service Oriented, Lambda, Microservices,
MVC, 4 plus 1

## Language and Framework choice:
1. Application modality:

    **Iteration 1:** For universality and ease of access, we have decided to create a web application. A web application will ensure that we have the widest possible audience reach, and that there are likely to be fewer compatibility issues between various mobile OS releases.

    **Iteration 2:** Develop mobile application
1. Application modality - web or mobile? For universality and ease of access, we have decided to create a web application, rather than mobile. A web application will ensure that we have the widest possible audience reach, and that there are likely to be fewer compatibility issues between various mobile OS releases.
2. In the preliminary stages of development, we have chosen to write our application in Python due to simplicity of syntax, universality of implementation, and prior group coding experience.
3. As the application is going to be web-based, we will be using the Flask web framework. The choice was made due to the vast array of existing Flask libraries that would ease our implementation and facilitate speedy delivery.

## I/O requirements:
1. The user should be able to log in with a simple text box, and their password input should be star-protected.
2. The output of the restaurant selection page should adapt to the screen window size selected by the user (window size agnostic).

## Various components of the system

## UI Client 
The application will be accessible via mobile, web, tablets, etc. Based on the actor, the interfaces presented will be different, or a combination of many. So, individual interfaces/pages will talk to the respective service for parts of the functionality. Primarily, there will be four versions of the interface for the four actors, viz customer, restaurant, Delivery man & admin.

## Search Ecosystem
The most important and coveted functionality that must be provided by the system is the capability of searching on menu items, cuisines, restaurants, among other things. In the food ordering journey, this functionality will be the point of entry for all the customers, unless they already have a favourite restaurant in their preferences from which they can select dishes. E.g.:  Elasticsearch or Apache Solr for quick look up as per user search parameters. 

## Ordering Service
This service will manage the menu selection, shopping cart management, and placement of food orders. It will process the payment using an External Payment Gateway and persist the result into an Orders database. Because order placement is transactional in nature, the best idea is to use a relational database. Customers will be able to get the full receipt of their order using this service along with other details about the order. They can also cancel the order if they changed their mind for some reason. Customers can also view their past order histories.



###  adjust and reformat -
I/O requirements
How various services communicate with each other. ( eg  REST, JSON-RPC)
Choice of Database (eg. RDBMS, Document-based, KeyValue)
Caching layers & their storage - how many level of caching layer -  (eg.  memcached, in memory, redis)
Language Platforms / Framework
