odoo.define('queue_dashboard.dashboard_action', function (require){
"use strict";
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');
    var QueueDashBoard = AbstractAction.extend({
       template: 'QueueDashBoard',
       events: {
        'click #pie_chart': 'pie_chart',
        'click #line_chart': 'line_chart',
       },
       start: function() {
          rpc.query({
            route: '/dashboard',
            params: {},
            }).then(function (result) {
                console.log(result)
          })
          google.charts.load('current', {'packages':['corechart']});
          google.charts.setOnLoadCallback(drawPieChart);
          function drawPieChart() {
            var data = google.visualization.arrayToDataTable([
              ['Task', 'Hours per Day'],
              ['Work',     11],
              ['Eat',      2],
              ['Commute',  2],
              ['Watch TV', 2],
              ['Sleep',    7]
            ]);
            var options = {
              title: 'My Daily Activities'
            };
            var chart = new google.visualization.PieChart(document.getElementById('sample'));
            chart.draw(data, options);
          }
       },
        pie_chart: function(e) {
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawPieChart);
              function drawPieChart() {
                var data = google.visualization.arrayToDataTable([
                  ['Task', 'Hours per Day'],
                  ['Work',     11],
                  ['Eat',      2],
                  ['Commute',  2],
                  ['Watch TV', 2],
                  ['Sleep',    7]
                ]);
                var options = {
                  title: 'My Daily Activities'
                };
                var chart = new google.visualization.PieChart(document.getElementById('sample'));
                chart.draw(data, options);
              }
        },
        line_chart: function(e) {
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(drawLineChart);
            function drawLineChart() {
                var data = google.visualization.arrayToDataTable([
                  ['Year', 'Sales', 'Expenses'],
                  ['2004',  1000,      400],
                  ['2005',  1170,      460],
                  ['2006',  660,       1120],
                  ['2007',  1030,      540]
                ]);
                var options = {
                  title: 'Company Performance',
                  curveType: 'function',
                  legend: { position: 'bottom' }
                };
                var chart = new google.visualization.LineChart(document.getElementById('sample'));
                chart.draw(data, options);
              }
        },
    })
core.action_registry.add('queue_dashboard', QueueDashBoard);
return QueueDashBoard;
})