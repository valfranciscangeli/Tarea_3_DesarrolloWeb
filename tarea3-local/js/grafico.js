console.log("grafico.js:" + "hola soy un grafico");

// ================ FUNCIONES ========================

function sacarMinimo(lista) {
  let min = 0
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] < min) {
      min = lista[i]
    }
  }
  return min
}

function sacarMaximo(lista) {
  let max = 0
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] > max) {
      max = lista[i]
    }
  }
  return max
}



// grafico de linea #####################################################

let xValues; //dias
let yValues; //cantidad de actividades


// AJAX ================================================
let xhr2 = new XMLHttpRequest();
xhr2.onreadystatechange = function () {
  if (xhr2.readyState === 4 && xhr2.status === 200) {
    let response = xhr2.responseText;
    response = JSON.parse(response);
    console.log("grafico.js:" + response);
    yValues = response[0]['cantidades'];
    xValues = response[0]['fechas'];
    console.log("grafico.js:" + yValues);
    console.log("grafico.js:" + xValues);

    let vMinimo = Math.max(sacarMinimo(yValues) - 1, 0);
    let vMaximo = sacarMaximo(yValues) + 1;

    new Chart("linea", {
      type: "line",
      data: {
        labels: xValues,
        datasets: [{
          fill: false,
          lineTension: 0,
          backgroundColor: "#9368B7",
          borderColor: "#D8A7CA",
          data: yValues
        }]
      },
      options: {
        legend: { display: false },
        scales: {
          yAxes: [{ ticks: { min: vMinimo, max: vMaximo, stepSize: 1 } }],
        },
        title: {
          display: false,
          text: "Cantidad de actividades totales por día"
        }
      }
    });
  }
}

xhr2.open("GET", "./cgi-bin/grafico_linea.py",);
xhr2.send();

console.log("grafico.js:" + yValues);
console.log("grafico.js:" + xValues);


// FIN AJAX =============================================


// grafico de torta #####################################################

let temas;
let cantidad;

// AJAX ================================================
let xhr = new XMLHttpRequest();
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    let response = xhr.responseText;
    response = JSON.parse(response);
    console.log("grafico.js:" + response);
    temas = response[0]['temas'];
    cantidad = response[0]['cantidad'];
    console.log("grafico.js:" + temas);
    console.log("grafico.js:" + cantidad);


    let barColors = [

      "#3da084",
      "#e5dd53",
      "#6b2336",
      "#263583",
      "#d26434",
      "#c4b175",
      "#2e6e85",
      "#9733e0",
      "#32b01d",
      "#dc033d",
      "#022F40",
      "#546363",
      "#846C5B",
      "#ECE7AC",
      "#74D3AE",
      "#7A9CC6",
      "#F49CBB",
      "#D8A7CA",
      "#F7B2AD",
      "#9368B7"
    ];

    new Chart("torta", {
      type: "pie",
      data: {
        labels: temas,
        datasets: [{
          backgroundColor: barColors,
          data: cantidad
        }]
      },
      options: {
        title: {
          display: false,
          text: "Cantidad de actividades totales según categoría"
        }

      }
    });

  }
}

xhr.open("GET", "./cgi-bin/grafico_torta.py",);
xhr.send();

console.log("grafico.js:" + temas);
console.log("grafico.js:" + cantidad);


// FIN AJAX =============================================


// grafico de barras #####################################################

let manhana;
let mediodia;
let tarde;

// AJAX ================================================
let xhr3 = new XMLHttpRequest();
xhr3.onreadystatechange = function () {
  if (xhr3.readyState === 4 && xhr3.status === 200) {
    let response = xhr3.responseText;
    response = JSON.parse(response);
    console.log("grafico.js:" + response);
    manhana = response[0]['manhana'];
    mediodia = response[0]['mediodia'];
    tarde = response[0]['tarde'];
    console.log("grafico.js:" + manhana);
    console.log("grafico.js:" + mediodia);
    console.log("grafico.js:" + (tarde));


    new Chart("barra", {
      type: "bar",
      data: {
        labels: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        datasets: [
          {
            label: "Mañana",
            backgroundColor: "rgba(116, 211, 174,1)",
            data: manhana
          },
          {
            label: "Mediodía",
            backgroundColor: "rgba(122, 156, 198,1)",
            data: mediodia
          },
          {
            label: "Tarde",
            backgroundColor: "rgba(244, 156, 187,1.0)",
            data: tarde
          }
        ]
      },
      options: {
        legend: { display: true },
        title: {
          display: false,
          text: "Total de actividades mensuales según horario"
        },
        scales: {
          yAxes: [
            {
              ticks: {
                min: 0, // it is for ignoring negative step.
                beginAtZero: true,
                stepSize: 1
              }
            }
          ]
        }
      }
    });

  }
}

xhr3.open("GET", "./cgi-bin/grafico_barra.py",);
xhr3.send();

console.log("grafico.js:" + manhana);
console.log("grafico.js:" + tarde);
console.log("grafico.js:" + (mediodia))

