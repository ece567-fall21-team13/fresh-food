# Architectural Design
The Architectural Design phase in the first iteration entails an abstract discussion of the basic building blocks for our system. 
The following action items were assigned the highest priority as much of subsequent development hinges on their completion:


## Choose an architecture and why - Monolithic, Service Oriented, Lambda, Microservices,
MVC, 4 plus 1

## Language and Framework choice:
1. Application modality:

    **Iteration 1:** For universality and ease of access, we have decided to create a web application. A web application will ensure that we have the widest possible audience reach, and that there are likely to be fewer compatibility issues between various mobile OS releases.

2. In the preliminary stages of development, we have chosen to write our application in Python due to simplicity of syntax, universality of implementation, and prior group coding experience.

3. As the application is going to be web-based, we will be using the Flask web framework. The choice was made due to the vast array of existing Flask libraries that would ease our implementation and facilitate speedy delivery.


### I/O requirements:
1. The user should be able to log in with a simple text box, and their password input should be star-protected

2. The output of the restaurant selection page should adapt to the screen window size selected by the user (window size agnostic)
    
3. User can select the restaurant nearby and place the order on the website
## Various components of the system

### UI Client 
The system can be accessible through mobile, web, tablets, etc. Based on the actor, the interfaces presented will be different, or a combination of many. So, individual interfaces will talk to the respective service for parts of the functionality. Primarily, there will be three versions of the interface for the three actors that is customer, restaurant and Delivery man.

### Search Ecosystem
Based on the user's location, the webpage will return all the restaurant/menus. It is based on a defined radius from the location of the user. This means that , the users will be shown only those restaurants that are reachable from the users’ addresses. Eg: Geo-distance query, Spatial Search
> To include how to user can see menu on the webpage

### **Order Management Service**
This service will manage the placement of food orders. It will save the order placed by the customer and generate an order ID that will be saved in database. We have decided to keep the payment method as cash. Customers will be able to get the full receipt of their order using this service. Customers can also view their past order histories. Ordering is a transactional process and can be stored in Postgresql
>**To include or not: They can also cancel the order if they changed their mind for some reason. User have 5 mins after the order is placed to cancel the order**

### Order Fulfillment Service
1. The restaurant accepts the order 
2. Customers can check the status of their orders.
3. Delivery person can check if the order is ready to be picked up.
4. Notifies the customer of any delay or any change in the order, if necessary (Using Notification Service)

### User Profile Management & Preferences Service
The actors in the system, namely, customers, restaurant , delivery person will need a way to create their profile with personal information, contact, address, and will be assigned a role based on their profile. Individual actors will also have preferences based on their role. For example, customers may have set preferences for selecting from a fixed set of restaurants or zip codes or cuisines. Delivery person might have a preference for delivering only within their specific area codes depending on its current location. This service will manage the profiles and preferences of all such actors across the board.

### Delivery dispatch Service
This service will be used to accomplish use-cases related to delivery person. A delivery person will be able to:
1. View pick-up orders from a list, that they can accept
2. View past orders that they have accepted

### Restaurant Profile Service
This service will be managing the data related to restaurants, menus, offerings, etc. A restaurant or business can:
1. Register
2. Update/Delete their profile
3. Create/Update/See/Delete menus, dishes etc
4. Check driver's location and assign order for delivery

### Driver Mapping Service


###  adjust and reformat -
I/O requirements
How various services communicate with each other. ( eg  REST, JSON-RPC)
Choice of Database (eg. RDBMS, Document-based, KeyValue)
Caching layers & their storage - how many level of caching layer -  (eg.  memcached, in memory, redis)
Language Platforms / Framework

