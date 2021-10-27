import React, {FunctionComponent} from 'react';
import './App.css';

//need to display restaurants, orders, drivers
//output display average time to delivery

type Restaurant = {
  name: string,
  address: string
}

type Customer = {
  name: string,
  address: string
}

type Driver = {
  name: string,
  address: string
}

type LiveOrder = {
  id: number,
  customerName: string,
  driverName: string,
  timeToDelivery: number
}

type MyState = {
  restaurants: Restaurant[],
  drivers: Driver[],
  customers: Customer[],
  live_orders: LiveOrder[],
  avgDeliveryTime: number 
}

class App extends React.Component {

  state: MyState = {
    restaurants: [{
      name: 'Destination Dogs', address: '101 Paterson St, New Brunswick, NJ 08901'
    },{
      name: 'Fajitas Mexican Restaurant', address: '542 Georges Rd, North Brunswick Township, NJ 08902'
    },
    {
      name: 'Marlen\'s Deli Restaurante', address: '918 Livingston Ave, North Brunswick Township, NJ 08902'
    },
    {
      name: 'Carmen\'s Restaurant', address: '68 Georges Rd, New Brunswick, NJ 08901'
    },
    {
      name: 'El Viejo Restaurant', address: '166 Remsen Ave, New Brunswick, NJ 08901'
    },
    {
      name: 'Smashburger', address: '975 US-1, North Brunswick Township, NJ 08902'
    },
    {
      name: 'Roberto\'s Restaurant', address: '776 Carolier Ln, North Brunswick Township, NJ 08902'
    },
    {
      name: 'Chef Tan Highland Park', address: '441 Raritan Ave, Highland Park, NJ 08904'
    },
    {
      name: 'KitTea', address: '248 Raritan Ave, Highland Park, NJ 08904'
    },
    {
      name: 'Paris Baguette', address: '1739 NJ-27, Edison, NJ 08817'
    },
    {
      name: 'Baguette Delite | Vietnamese Restaurant', address: '381 Old Post Rd, Edison, NJ 08817'
    },
    {
      name: 'Wonder Seafood Restaurant', address: '1984 NJ-27, Edison, NJ 08817'
    },
    {
      name: 'Franco\'s Pizza', address: '170 Talmadge Rd, Edison, NJ 08817'
    },
    {
      name: 'Evely\'s Restaurant', address: '45 Easton Ave, New Brunswick, NJ 08901'
    },
    {
      name: 'Dunkin\'', address: '720 Somerset St, New Brunswick, NJ 08901'
    }
    ],
    drivers: [
      {name: 'Lilly Brady', address: '10 Paul Robeson Blvd, New Brunswick, NJ 08901'},
      {name: 'Elisha Robinson', address:'131 Jones Avenue, New Brunswick, NJ 08901'},
      {name: 'Taylah Merrill', address: '156 George St, New Brunswick, NJ 08901'},
      {name: 'Morwenna Hampton', address: '96 Commercial Ave, New Brunswick, NJ 08901'},
      {name: 'Lincoln Donnelly', address: '88 Townsend St, New Brunswick, NJ 08901'},
      {name: 'Emile Roche', address: '92 Suydam St, New Brunswick, NJ 08901'},
      {name: 'Jill Kenny', address: '113 Baldwin St, New Brunswick, NJ 08901'},
      {name: 'Boyd Jefferson', address: '128A Remsen Ave, New Brunswick, NJ 08901'},
      {name: 'Joely Harper', address: '68 Throop Ave, New Brunswick, NJ 08901'},
      {name: 'Aidan Sanderson', address: '59 Baldwin St, New Brunswick, NJ 08901'},
      {name: 'Ursula Handley', address: '103 Delavan St, New Brunswick, NJ 08901'},
      {name: 'Hadley Flores', address: '65 Wyckoff St, New Brunswick, NJ 08901'},
      {name: 'Clinton Frank', address: '20 Newell Ave, New Brunswick, NJ 08901'},
      {name: 'Konrad Joyce', address: '60 Comstock St, New Brunswick, NJ 08901'},
      {name: 'Aizah Davis', address: '204 Paul Robeson Blvd, New Brunswick, NJ 08901'},
      {name: 'Viktor Kelley', address: '336 Livingston Ave, New Brunswick, NJ 08901'},
      {name: 'Lawson Odom', address: '390 Lee Ave, New Brunswick, NJ 08901'},
      {name: 'Candice Gentry', address: '486 Remsen Ave, New Brunswick, NJ 08901'},
      {name: 'Arun Carlson', address: '874 Nassau St, North Brunswick Township, NJ 08902'},
      {name: 'Madeleine Goodman', address: '884 Stevens St, North Brunswick Township, NJ 08902'}
  ],

  customers: [
    {name: 'Suman Murray', address: "360 Somerset St, New Brunswick, NJ 08901"},
    {name: 'Mitchel Schofield', address: "15 Wilcox Rd, New Brunswick, NJ 08901"},
    {name: 'Anja Espinoza', address: "10 Voorhees Rd, New Brunswick, NJ 08901"},
    {name: 'Fox Trujillo', address: "57 Pennington Rd, New Brunswick, NJ 08901"},
    {name: 'Jobe Abbott', address: "17 Goodale Cir, New Brunswick, NJ 08901"},
    {name: 'Shaan Monroe', address: "80 Phelps Ave, New Brunswick, NJ 08901"},
    {name: 'Billie-Jo Mcfarland', address: "6 Cobb Rd, New Brunswick, NJ 08901"},
    {name: 'Leyla Oconnor', address: "90 Howard St, New Brunswick, NJ 08901"},
    {name: 'Alfie-Jay Gould', address: "104 Howard St, New Brunswick, NJ 08901"},
    {name: 'Viktor Clemons', address: "41 Renaissance Ln, New Brunswick, NJ 08901"},
    {name: 'Kailum Velez', address: "100 Fulton Ct, New Brunswick, NJ 08901"},
    {name: 'Nettie Waters', address: "175 Lawrence St, New Brunswick, NJ 08901"},
    {name: 'Myron Iles', address: "14 Wright Pl, New Brunswick, NJ 08901"},
    {name: 'Vivian Pierce', address: "57 Ray St, New Brunswick, NJ 08901"},
    {name: 'Irene Worthington', address: "43 Jefferson Ave, New Brunswick, NJ 08901"},
    {name: 'Timur Talbot', address: "105 Renaissance Ln, New Brunswick, NJ 08901"},
    {name: 'Inara Kaiser', address: "35 S Talmadge St, New Brunswick, NJ 08901"},
    {name: 'Mae Galindo', address: "5 Wellington Pl, New Brunswick, NJ 08901"},
    {name: 'Ruby-Leigh Acevedo', address: "251 Joyce Kilmer Ave, New Brunswick, NJ 08901"},
    {name: 'Vivek Potts', address: "313 Powers St, New Brunswick, NJ 08901"},
  ],
    live_orders: [
    ],
    avgDeliveryTime: 10
  }

  componentDidMount() {
    
    let modifiedLiveOrders = this.state.live_orders

    for (let i = 0; i < 20; i++) {
      modifiedLiveOrders.push({id: i+1, customerName: this.state.customers[i].name, driverName: this.state.drivers[i].name, timeToDelivery: .25*i*i*+1-0.2*i})
    }

    this.setState({
      live_orders: modifiedLiveOrders
    })
  }

  render() {
    return (
      <div className="group">
        <div className="restaurantTable">
          <table>
            <tr>
              <th>Restaurant Name</th>
              <th>Address</th>
            </tr>
            {
              this.state.restaurants.map ( (restaurant) => {
                return (
                  <tr>
                    <td>{restaurant.name}</td>
                    <td>{restaurant.address}</td>
                  </tr>
                )
              })
            }
          </table>
        </div>

        <div className="customerTable">
          <table>
              <tr>
                <th>Customer Name</th>
                <th>Address</th>
              </tr>
              {
                this.state.customers.map ( (customer) => {
                  return (
                    <tr>
                      <td>{customer.name}</td>
                      <td>{customer.address}</td>
                    </tr>
                  )
                })
              }
            </table>
        </div>

        <div className="driverTable">
        <table>
            <tr>
              <th>Driver Name</th>
              <th>Address</th>
            </tr>
            {
              this.state.drivers.map ( (driver) => {
                return (
                  <tr>
                    <td>{driver.name}</td>
                    <td>{driver.address}</td>
                  </tr>
                )
              })
            }
          </table>
        </div>

        <div className="combinedTable">
          <table>
            <tr>
              <th>ID</th>
              <th>Customer Name</th>
              <th>Driver Name</th>
              <th>Time to Delivery</th>
            </tr>
            {
              this.state.live_orders.map ( (live_order) => {
                return (
                  <tr>
                    <td>{live_order.id}</td>
                    <td>{live_order.customerName}</td>
                    <td>{live_order.driverName}</td>
                    <td>{live_order.timeToDelivery}</td>
                  </tr>
                )
              })
            }
          </table>
        </div>

        <div className="output">
          <div className="outputLeft">
            <h3>Average time to delivery: {this.state.avgDeliveryTime}</h3>
          </div>
          <div className="outputRight">
            Numbers of restaurants: {this.state.restaurants.length}<br/>
            Number of customers: {this.state.customers.length}<br/>
            Number of drivers: {this.state.drivers.length}<br/>
          </div>
        </div>
      </div>
    )
  }
}

export default App;
