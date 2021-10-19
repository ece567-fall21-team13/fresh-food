# Requirements Engineering
The requirements engineering phase of the first iteration consists of a high-level conversation with the customer.
It entails a discussion of maximum capacity for suppliers (restaurants), drivers, and customers.
The customer specifies that the application is to handle 25 restaurants and up to 1000 food orders every hour.

# Report from Requirements elicitation
We observed food delivery companies mainly DoorDash and Zomato. We observed the way a order is booked into the app and passed
to the restaurants. The food delivery business was found to be time-bounded and involves problems like routing, travelling salesman.
We also observed how existing food delivery companies have integrated their system with restaurants.

# Choosing a SRS languague - We choose structured language
> TODO: We do understand that requirement specification is usually at a more granular level, but here we defining requirements for a system as a whole.  
> We could offer SRS for submodules in future iteration.  
  
**Food Delivery/Operational Software/SRS/3.3.2**

**Function** Deliver Food from restaurant to customer.

**Description**	The system will receive a order from customer, assign the order to a Driver. 
The Driver then picks the order from the restaurant and delivers to customer.

**Inputs** Order from customer, customer information like address

**Source** A catalog which is displayed to customer.   

**Outputs** Order delivered to the customer.

**Destination** web app interface.

**Action**:	The order will be is assigned to the nearest Driver. The delivery is supposed to pick order. The Driver is suggested with shortest path / cheapest path with a viable time. The customer is provided with real time tracking of the Driver.  

**Requires** Address with coordinates of the restaurant and the customer.  

**Precondition** The restaurant should be open, the restaurant should confirm the order.

**Postcondition** The order is marked delivered

**Side effects**  None.


# Functional requirements
1. The system should be able to list available restaurants which could deliver as a **catalog** to the customer.   
2. The customer should get a **list of items** of a selected restaurant.
3. The customer should be able to select and order the item.
4. The order should be notified to the restaurant and take a confirmation from the restaurant.   
5. The system should assign an UNASSIGNED INPROGRESS order to a Driver.
6. The customer should be able to **track** the oder.
7. The restaurants should be able to access average delivery time for a zipcode.

# Non-functional requirements
1. The system should be able to able to deliver orders under 1 hour.
2. The system should be able track 1000 order concurrently, which also means we could be having over 10000 customers.
3. The number of restaurants is expected to be somewhere around 25, but system should support more number of restaurants.
4. The customer should be highly available as food delivery business is real time operational in nature.
5. The system should be strongly consistent when placing orders, processing payments etc.
6. The customer information should be stored securely eg. customer email, address, or any sensitive data.  

# Use-case diagram