const electricity = document.getElementById('electricityCO');
const electricityCO = Number(electricity.innerHTML);

const natural_gas = document.getElementById('natural_gasCO');
const natural_gasCO = Number(natural_gas.innerHTML);

const heating_oil = document.getElementById('heating_oilCO');
const heating_oilCO = Number(heating_oil.innerHTML);

const miles_driven = document.getElementById('miles_drivenCO');
const miles_drivenCO = Number(miles_driven.innerHTML);

const miles_flown = document.getElementById('miles_flownCO');
const miles_flownCO = Number(miles_flown.innerHTML);

const miles_train = document.getElementById('miles_trainCO');
const miles_trainCO = Number(miles_train.innerHTML);

const miles_bus = document.getElementById('miles_busCO');
const miles_busCO = Number(miles_bus.innerHTML);

const hotel_nights = document.getElementById('hotel_nightsCO');
const hotel_nightsCO = Number(hotel_nights.innerHTML);

const total = document.getElementById('totalCO');
const totalCO = Number(total.innerHTML);

var barChartData = {
  labels: [
    "Home Utility",
    "Personal Travel",
    "Commuter Travel",
    "Hotel",
    "Total"
  ],
  datasets: [
    {
      label: "My Carbon Footprint",
      backgroundColor: "pink",
      borderColor: "red",
      borderWidth: 1,
      data: [(electricityCO + natural_gasCO + heating_oilCO), (miles_drivenCO + miles_flownCO), (miles_trainCO + miles_busCO), hotel_nightsCO, totalCO]
    },
    {
      label: "National Average Carbon Footprint",
      backgroundColor: "lightblue",
      borderColor: "blue",
      borderWidth: 1,
      data: [14.536325, 6.002, 2.834, 0.076, 23.6]
    }
  ]
};

var chartOptions = {
  responsive: true,
  legend: {
    position: "top"
  },
  title: {
    display: true,
    text: "Carbon Footprint (metric tons of CO2)"
  },
  scales: {
    yAxes: [{
      ticks: {
        beginAtZero: true
      }
    }]
  }
}

window.onload = function() {
  var ctx = document.getElementById("canvas").getContext("2d");
  window.myBar = new Chart(ctx, {
    type: "bar",
    data: barChartData,
    options: chartOptions
  });
};
