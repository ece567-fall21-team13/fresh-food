CREATE
EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE restaurants
(
    restaurant_uuid text default 'res::' || uuid_generate_v4() primary key,
    name            text,
    address         text
);

COPY restaurants(name, address)
FROM '/home/workstation/workspace/PycharmProjects/fresh-food/raw_test_data/restaurant_name_and_addresses.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE customers
(
    customer_uuid text default 'cus::' || uuid_generate_v4() primary key,
    name          text,
    email         text,
    address       text
);

COPY customers(email, name, address)
FROM '/home/workstation/workspace/PycharmProjects/fresh-food/raw_test_data/customer_name_and_addresses.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE drivers
(
    driver_uuid      text default 'dri::' || uuid_generate_v4() primary key,
    name text,
    current_location text
);

COPY drivers(name,current_location)
FROM '/home/workstation/workspace/PycharmProjects/fresh-food/raw_test_data/driver_name_and_address.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE orders
(
    order_uuid text default 'ord::' || uuid_generate_v4(),
    created_at timestamp,
    driver_uuid text references drivers(driver_uuid),
    status text,
    customer_uuid text references customers(customer_uuid)
);

