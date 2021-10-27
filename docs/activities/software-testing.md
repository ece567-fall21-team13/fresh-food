# Software Testing

<<<<<<< Updated upstream
# Approach / Details 
Testing will proceed in this order: unit testing, component testing, then system testing.
=======
# Approach / Details

The testing of our software will be done in three phases.

* Development Testing
* Release Testing
* User Testing

Development testing will proceed in this order: unit testing, component testing, then system testing.
>>>>>>> Stashed changes

## Unit tests
Each individual object class shall be tested separately by evaluating each method in the class by at least 3 separate values/conditions that lie in different equivalence partitions. Each class attribute should be retrieved and attempt to be set, to ensure proper visibility of class components are realized, and placing the class in all possible states.
In a feature iteration, these tests will be elaborated upon and could even be tested using an automation framework for unit testing.

### Test ideas
1. Invalid inputs
   1. No pin code, wrong address, etc.
   2. Invalid email/credit card number

## Component tests
Upon successful unit testing, component testing shall follow. This will include the interfaces that must interact between the various classes. Here we shall stress test the timing of one component interfacing with another, quickly repeating calls to another component, and testing parameters at the edges of parameter limits.

### Test ideas 
1. Overloading the interfaces between components with quick, back-to-back requests and seeing how the components respond.

## System tests
Upon successful completion of component testing, system testing shall proceed. Here we shall ensure that the system has integrated properly by evaluating the enumerated and developed use cases and ensure that the output matches what is expected.

### Test Ideas
1. Testing time constraints for delivery - looking for accuracy of estimation.
   1. Ensure that we can accommodate the carrying capacity proposed.
2. Security testing (pen testing, payment encryption protocols, etc.)

## Use-case testing
Use cases tests will be added as more use cases are enumerated. Here we shall run through the system in the manner in which a user would as described in various use-cases.

Each of the action items in section 1.4 (Iteration 1 Design and Implementation) are to be tested with an emphasis on functionality rather than UX design.
1. Item 1.4.1 (Design of customer login page) implementation testing:
    1. A pre-set customer with a unique login credential should be able to log in and be redirected to a restaurant list page with no errors.
    2. When either the login or password is entered incorrectly, the system prompts the user to retry.
2. Item 1.4.2 (Design of restaurant order manager login page) implementation testing:
    1. A pre-set restaurant order manager with a unique login credential should be able to log in and be redirected to a restaurant list page with no errors.
    2. When either the login or password is entered incorrectly, the system prompts the user to retry.
3. Item 1.4.3 (Preliminary UI for restaurant selection) implementation testing:
   1. Upon successful login by the customer, a pre-set number of restaurants are viewed in a single column.
   2. If the column size exceeds the screen resolution, the user should be able to scroll through the list in order to view all available restaurants.

## User acceptance testing
1. Potential beta users
2. Users test across different platforms - does our service run equally well on mobile/web, Android/iOS?