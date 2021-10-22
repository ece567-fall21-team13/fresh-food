# Architectural Design
The Architectural Design phase in the first iteration entails an abstract discussion of the basic building blocks for our system. 
The following action items were assigned the highest priority as much of subsequent development hinges on their completion:


## Choose a architecture and why - Monolithic, Service Oriented, Lambda, Microservices,
MVC, 4 plus 1

## Language and Framework choice:
1. Application modality:

    **Iteration 1:** For universality and ease of access, we have decided to create a web application. A web application will ensure that we have the widest possible audience reach, and that there are likely to be fewer compatibility issues between various mobile OS releases.

    **Iteration 2:** Develop mobile application
2. In the preliminary stages of development, we have chosen to write our application in Python due to simplicity of syntax, universality of implementation, and prior group coding experience.

3. As the application is going to be web-based, we will be using the Flask web framework. The choice was made due to the vast array of existing Flask libraries that would ease our implementation and facilitate speedy delivery.


## I/O requirements:
1. The user should be able to log in with a simple text box, and their password input should be star-protected

2. The output of the restaurant selection page should adapt to the screen window size selected by the user (window size agnostic)
    
3. User can select the restaurant nearby and view the menu on the website
# Various components of the system

### UI Client 
The system can be accessible via mobile, web, tablets, etc. Based on the actor, the interfaces presented will be different, or a combination of many. So, individual interfaces/pages will talk to the respective service for parts of the functionality. Primarily, there will be four versions of the interface for the four actors, viz customer, restaurant, Delivery man & admin.

### Search Ecosystem

1. The most important and coveted functionality that must be provided by the system is the capability of searching on menu items, restaurants. In the food ordering journey, this functionality will be the point of entry for all the customers, unless they already have a favourite restaurant in their preferences from which they can select dishes.
   
2. Based on the user's location, the webpage will return all the restaurant/menus. It is based on a defined radius from the location of the user. What this essentially means is, users will be shown only those restaurants that are reachable from the users’ addresses. Eg: Geo-distance query, Spatial Search
> To include how to user can see menu on the webpage

**### Ordering Service**
This service will manage the menu selection, shopping cart management, and placement of food orders. It will process the payment using an External Payment Gateway and persist the result into an Orders database. For iteration 1 we have decided to keep the payment method as cash. Customers will be able to get the full receipt of their order using this service along with other details about the order. Customers can also view their past order histories. Ordering is a transactional process and can be stored in Oracle/MySQL/Postgres

>**To include or not: They can also cancel the order if they changed their mind for some reason. User have 5 mins after the order is plcaed to cancel the order**

### Order Fulfillment Service
1. The restaurant accepts the order 
2. Customers can check the status of their orders.
3. Delivery person can check if the order is ready to be picked up.
4. Notifies the customer of any delay or any change in the order, if necessary (Using Notification Service)

### User Profile Management & Preferences Service
The actors in the system, namely, customers, restaurant , delivery person will need a way to create their profile with personal information, contact, address, and will be assigned a role based on their profile. Individual actors will also have preferences based on their role. For example, customers may have set preferences for selecting from a fixed set of restaurants or zip codes or cuisines. Delivery person might have a preference for delivering only within their specific area codes depending on it's current location. Notification preferences of actors will also vary (Eg. Delivery person will be notified from where to pick and delver the order, restaurant will be notified if customer plaed the order). This service will manage the profiles and preferences of all such actors across the board.

### Delivery dispatch Service
This service will be used to accomplish use-cases related to delivery person. A delivery person will be able to:
1. View pick-up orders from a list, that they can accept
2. View past orders that they have accepted

### Restaurant Profile Service
This service will be managing the data related to restaurants, menus, offerings, etc. A restaurant or business can:
1. Register
2. Update/Delete their profile
3. Create/Update/See/Delete menus, dishes etc

**### Notification Service**
This service is responsible for delivering notifications to every actor with the system. The notifications could be sent out to the individual actors in the preferences they have set for receiving them. Some actors might prefer push notifications, some might receive text or emails. This service is supposed to abstract out the medium in which notifications are being sent. This means the underlying interactions with the mobile carrier, email service providers, etc will be abstracted. 
The responsibilities are notifying:
1. **The customer**: About various status of the order, for example, the order was placed successfully, or, the restaurant has accepted the order, or, delivery guy has picked up the order and is on his/her way to deliver it.
2. **The restaurant**: That an order was placed, or a delivery guy has accepted to pick up the order from the restaurants, or the delivery guy is on his/her way to pick up the order.
3. **The delivery person**: That orders are waiting in their queue for their acceptance, or that the order is ready to be picked up.


###  adjust and reformat -
I/O requirements
How various services communicate with each other. ( eg  REST, JSON-RPC)
Choice of Database (eg. RDBMS, Document-based, KeyValue)
Caching layers & their storage - how many level of caching layer -  (eg.  memcached, in memory, redis)
Language Platforms / Framework

