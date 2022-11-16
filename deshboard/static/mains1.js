// var socket = new WebSocket("ws://localhost:8000/ws/graph");

// socket.onmessage= function(e){
//     var djangoData = JSON.parse(e.data);
//     console.log(djangoData);
//     document.querySelector("#app").innerText = djangoData.value;
// }

const ctx = document.getElementById('myChart').getContext('2d');

var graphData = {
    type: 'line',
    data: {
        labels: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
        datasets: [{
            label: 'Temperature',
            data: [56,76,83,74,75,46,77,78,89,80,71,12,13,14,15,16,17,18,19,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,37,38,39,40,41,42,43,44,45,46,47,48],
            options: {

                responsive: false
            },
 
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
      
            ],
            borderWidth: 1
        }]
    },
    options: {}
}
var myChart = new Chart(ctx, graphData );  




var socket = new WebSocket("ws://127.0.0.1:8000/ws/graph/")
socket.onmessage = function(e){
    var djangoData=JSON.parse(e.data);
    console.log(djangoData);
    document.querySelector("#app").innerText = djangoData.value;
    var newGraphData = graphData.data.datasets[0].data;
    newGraphData.shift();
    newGraphData.push(djangoData.value);
    graphData.data.datasets[0].data = newGraphData;
    myChart.update();

    
}



const ctx1 = document.getElementById('myChart1').getContext('2d');

var graphData1 = {
    type: 'bar',
    data: {
        labels: ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'],
        datasets: [{
            label: 'Noise',
            data: [12, 19, 3, 5, 2, 3,23,43,34,12, 19, 3, 5, 2, 3,23,43,34,10,11,12,13,14,15,16,17,18],
            options: {

                responsive: false
            },
 
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(232, 152, 92, 0.9)',
                'rgba(253, 180, 255, 0.9)',
                'rgba(205, 119, 24, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(232, 152, 92, 0.9)',
                'rgba(253, 180, 255, 0.9)',
                'rgba(205, 119, 24, 0.9)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
      
            ],
            borderWidth: 1
        }]
    },
    options: {}
}
var myChart1 = new Chart(ctx1, graphData1 );  

var socket = new WebSocket("ws://127.0.0.1:8000/ws/graph1/")
socket.onmessage = function(e){
    var djangoData1=JSON.parse(e.data);
    console.log(djangoData1);
    document.querySelector("#app1").innerText = djangoData1.value;
    console.log(djangoData1);
    var newGraphData1 = graphData1.data.datasets[0].data;
    newGraphData1.shift();
    newGraphData1.push(djangoData1.value);
    graphData1.data.datasets[0].data = newGraphData1;
    myChart1.update();

    
}











const ctx2 = document.getElementById('myChart2').getContext('2d');

var graphData2 = {
    type: 'line',
    data: {
        labels: ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'],
        datasets: [{
            label: 'Vibration X_axis',
            data: [12, 19, 3, 5, 2, 3,23,43,34,12, 19, 3, 5, 2, 3,23,43,34,10,11,12,13,14,15,16,17,18],
            options: {

                responsive: false
            },
 
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(232, 152, 92, 0.9)',
                'rgba(253, 180, 255, 0.9)',
                'rgba(205, 119, 24, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(232, 152, 92, 0.9)',
                'rgba(253, 180, 255, 0.9)',
                'rgba(205, 119, 24, 0.9)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
      
            ],
            borderWidth: 1
        }]
    },
    options: {}
}
var myChart2 = new Chart(ctx2, graphData2 );  

var socket = new WebSocket("ws://127.0.0.1:8000/ws/graph2/")
socket.onmessage = function(e){
    var djangoData2=JSON.parse(e.data);
    console.log(djangoData2);
    document.querySelector("#app2").innerText = djangoData2.value;
    console.log(djangoData2);
    var newGraphData2 = graphData2.data.datasets[0].data;
    newGraphData2.shift();
    newGraphData2.push(djangoData2.value);
    graphData2.data.datasets[0].data = newGraphData2;
    myChart2.update();

    
}


const ctx3 = document.getElementById('myChart3').getContext('2d');

var graphData3 = {
    type: 'line',
    data: {
        labels: ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'],
        datasets: [{
            label: 'Vibration Y_asix',
            data: [12, 19, 3, 5, 2, 3,23,43,34,12, 19, 3, 5, 2, 3,23,43,34,10,11,12,13,14,15,16,17,18],
            options: {

                responsive: false
            },
 
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(232, 152, 92, 0.9)',
                'rgba(253, 180, 255, 0.9)',
                'rgba(205, 119, 24, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(232, 152, 92, 0.9)',
                'rgba(253, 180, 255, 0.9)',
                'rgba(205, 119, 24, 0.9)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
      
            ],
            borderWidth: 1
        }]
    },
    options: {}
}
var myChart3 = new Chart(ctx3, graphData3 );  

var socket = new WebSocket("ws://127.0.0.1:8000/ws/graph3/")
socket.onmessage = function(e){
    var djangoData3=JSON.parse(e.data);
    console.log(djangoData3);
    document.querySelector("#app3").innerText = djangoData3.value;
    console.log(djangoData3);
    var newGraphData3 = graphData3.data.datasets[0].data;
    newGraphData3.shift();
    newGraphData3.push(djangoData3.value);
    graphData3.data.datasets[0].data = newGraphData3;
    myChart3.update();

    
}




const ctx4 = document.getElementById('myChart4').getContext('2d');

var graphData4 = {
    type: 'line',
    data: {
        labels: ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'],
        datasets: [{
            label: 'Vibration Z_asix',
            data: [12, 19, 3, 5, 2, 3,23,43,34,12, 19, 3, 5, 2, 3,23,43,34,10,11,12,13,14,15,16,17,18],
            options: {

                responsive: false
            },
 
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(232, 152, 92, 0.9)',
                'rgba(253, 180, 255, 0.9)',
                'rgba(205, 119, 24, 0.9)',
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',
                'rgba(255, 159, 64, 0.9)',
                'rgba(232, 152, 92, 0.9)',
                'rgba(253, 180, 255, 0.9)',
                'rgba(205, 119, 24, 0.9)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
      
            ],
            borderWidth: 1
        }]
    },
    options: {}
}
var myChart4 = new Chart(ctx4, graphData4 );  

var socket = new WebSocket("ws://127.0.0.1:8000/ws/graph4/")
socket.onmessage = function(e){
    var djangoData4=JSON.parse(e.data);
    console.log(djangoData4);
    document.querySelector("#app4").innerText = djangoData4.value;
    console.log(djangoData4);
    var newGraphData4 = graphData4.data.datasets[0].data;
    newGraphData4.shift();
    newGraphData4.push(djangoData4.value);
    graphData4.data.datasets[0].data = newGraphData4;
    myChart4.update();

    
}











const ctx5 = document.getElementById('myChart5').getContext('2d');

var graphData5 = {
    type: 'bar',
    data: {
        labels: ['1', '2', '3', '4', '5'],
        datasets: [{
            label: 'Data Received in BG',
            data: [12,19,18,25,21],
            options: {

                responsive: false
            },
 
            backgroundColor: [
                'rgba(255, 99, 132, 0.9)',
                'rgba(54, 162, 235, 0.9)',
                'rgba(255, 206, 86, 0.9)',
                'rgba(75, 192, 192, 0.9)',
                'rgba(153, 102, 255, 0.9)',

            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
      
            ],
            borderWidth: 1
        }]
    },
    options: {}
}
var myChart5 = new Chart(ctx5, graphData5 );  

var socket = new WebSocket("ws://127.0.0.1:8000/ws/graph4/")
socket.onmessage = function(e){
    var djangoData5=JSON.parse(e.data);
    console.log(djangoData5);
    document.querySelector("#app5").innerText = djangoData5.value;
    console.log(djangoData5);
    var newGraphData5 = graphData5.data.datasets[0].data;
    newGraphData5.shift();
    newGraphData5.push(djangoData5.value);
    graphData5.data.datasets[0].data = newGraphData5;
    myChart5.update();

    
}