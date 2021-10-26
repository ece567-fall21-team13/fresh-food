import React from 'react';
import './App.css';
//need to display restaurants, orders, drivers
//output display average time to delivery

type Restaurant = {
  name: string,
  latitude: number,
  longitude: number
}

type Order = {
  id: number,
  latitude: number,
  longitude: number
}

type Driver = {
  id: number,
  latitude: number,
  longitude: number
}

type MyState = {
  restaurants: Restaurant[],
  orders: Order[],
  drivers: Driver[],
  avgDeliveryTime: number 
}

class App extends React.Component {

  state: MyState = {
    restaurants: [{
      name: "test restaurant",
      latitude: 1,
      longitude: 1
    }],
    orders: [{
      id: 1,
      latitude: 2,
      longitude: 2
    }],
    drivers: [{
      id: 3,
      latitude: 3,
      longitude: 3
    }],
    avgDeliveryTime: 10
  }

  render() {
    return (
      <div>
        <div className="restaurantTable">
          <table>
            <tr>
              <th>Name</th>
              <th>Latitude</th>
              <th>Longitude</th>
            </tr>
            {
              this.state.restaurants.map ( (restaurant) => {
                return (
                  <tr>
                    <td>{restaurant.name}</td>
                    <td>{restaurant.latitude}</td>
                    <td>{restaurant.longitude}</td>
                  </tr>
                )
              })
            }
          </table>
        </div>

        <div className="orderTable">
          <table>
            <tr>
              <th>ID</th>
              <th>Latitude</th>
              <th>Longitude</th>
            </tr>
            {
              this.state.orders.map ( (order) => {
                return (
                  <tr>
                    <td>{order.id}</td>
                    <td>{order.latitude}</td>
                    <td>{order.longitude}</td>
                  </tr>
                )
              })
            }
          </table>
        </div>

        <div className="driverTable">
          <table>
            <tr>
              <th>ID</th>
              <th>Latitude</th>
              <th>Longitude</th>
            </tr>
            {
              this.state.drivers.map ( (driver) => {
                return (
                  <tr>
                    <td>{driver.id}</td>
                    <td>{driver.latitude}</td>
                    <td>{driver.longitude}</td>
                  </tr>
                )
              })
            }
          </table>
        </div>

        <div className="output">
          <h3>Average time to delivery:</h3>
          {this.state.avgDeliveryTime}
        </div>
      </div>
    )
  }
}

export default App;
