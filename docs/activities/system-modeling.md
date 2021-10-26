# System Modeling
The initial System Modeling phase involves creating an abstract view of the system. System Modeling of the first iteration answers the preliminary big questions related to the project requirements: 
1. What is the external perspective of the system? 
2. What will be the interaction between the system and its environment?
3. Modeling the organization of the system and how it will process data.
4. How will the application behave in a dynamic environment where it responds to external inputs.

All of these questions are answered partially in other parts of the supporting documentation, but the system modeling chapter summarizes them succinctly. In order, those "macro" questions are answered as follows:

1. The external perspective of the system is resposible for the interaction between the restaurant database, the users who are placing their orders, and the delivery drivers who are capable of delivering the meals within the constraints specified in the requirements engineering phase.
2. The interaction between the system and its environment responds to the changing circumstances under which the many components of our system connect the three parties mentioned above. This interaction is partially demonstrated in the UML documentation provided.
3. Modeling the organization of the system and the manner in which it handles user input and output is annotated in the class diagram and the UML diagram provided. The state diagram contains all of the workflow of the system, as well as the classes present in the environment and the methods along which they interact with each other. 

#TODO CREATE CONTEXT DIAGRAM
#TODO ADD LINK TO CLASS DIAGRAM

4. The application is modeled such that it can handle varying data inputs, as long as they conform to the specifications of the requirements engineering. In other words, the application should be able to adapt to a number of circumstances, such as a changing number of suppliers, cancellation of orders, and other events unforseen by the standard workflow procedures. 

As discussed with the team, the system modeling part of the first iteration is largely defining an abstract view of the system. The following key functionalities were identified in the most abstract manner:

1. The user (customer) should be able to browse a selection of pre-sorted restaurants. In the final iteration, the user will be able to filter the available restaurants by distance, cuisine, rating, and price range.
2. The supplier (restaurant) should be able to limit the number of orders in their queue for a given time, to accomodate the delivery in a timely manner.
3. The user should be able to browse all of the avaiable items on the menu, which can either be pre-set or, in the final iteration closer to production, be dynamically chosen by the restaurant based on seasonality and availability.
4. The user should be able to track the order in real time, based on the user's geolocation and the position of the delivery driver.

Naturally, all of these functionalities are expanded upon more in the development phase and put into more precise language.