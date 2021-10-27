# Freezed API's
* **/api/restaurants/catalog** -> returns list of restaurants with average time to delivery
  * Request Command - 
```shell
curl --location --request POST 'localhost:5000/api/restaurants/catalog' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_uuid": "cus::0cdfbbe3-eb83-4e55-9559-a3f57347633d"
}'
```
  * Sample Response -
```JSON
[
    {
        "address": "101 Paterson St, New Brunswick, NJ 08901",
        "name": "Destination Dogs",
        "restaurant_uuid": "res::6b5de626-2200-477b-9431-542365497580",
        "time_to_deliver": "10 mins"
    },
    {
        "address": "542 Georges Rd, North Brunswick Township, NJ 08902",
        "name": "Fajitas Mexican Restaurant",
        "restaurant_uuid": "res::5b67a651-7ccc-4996-9999-a7c3a8a96d53",
        "time_to_deliver": "15 mins"
    },
    {
        "address": "918 Livingston Ave, North Brunswick Township, NJ 08902",
        "name": "Marlen's Deli Restaurante",
        "restaurant_uuid": "res::d9f3693f-4b87-4017-9286-733a077a680a",
        "time_to_deliver": "30 mins"
    }
]
  ```
* **/api/customer/place_oder** -> 
  * Request Command - 
```shell
curl --location --request POST 'localhost:5000/api/customer/place_oder' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_uuid": "cus::0cdfbbe3-eb83-4e55-9559-a3f57347633d",
    "restaurant_uuid":"res::6b5de626-2200-477b-9431-542365497580"
}'
```
  * Sample Response  - 
```JSON
{
    "customer_id": "cus::0cdfbbe3-eb83-4e55-9559-a3f57347633d",
    "order_uuid": "odr::deb92895-7fa2-4d2d-a94e-7d500f4bc3da",
    "restaurant_uuid": "res::6b5de626-2200-477b-9431-542365497580",
    "status": "CREATED",
    "time_delivery": '35 mins'
}
```
* **api/admin/global_average_time_metric** -> returns **mean** time_to_delivery for all orders existing in the system
  * Request Command - 
```shell
curl --location --request GET 'localhost:5000/api/admin/global_average_time_metric' \
--header 'Content-Type: application/json'
```
  * Sample Response  - 
```JSON
{
    "avg_time_to_deliver": "31.5 mins"
}
```