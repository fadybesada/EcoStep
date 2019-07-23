const CHART = document.getElementByID("lineChart"),
Chart.defaults.scale.ticks.beginAtZero = true;

let barChart = new Chart(CHART, {
  type: 'pie',
  data: {
    labels: ['Home', 'Travel', 'Food'],
    datasets: [
      {
        label: 'Points',
        backgroundColor: ['#f1c40f','#e67e22','#16a085'
        data: [10, 20, 55, 12]
      }
    ]
  }
});
