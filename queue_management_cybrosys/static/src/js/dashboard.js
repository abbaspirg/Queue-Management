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
        'click #today_queue': 'today_queue',
        'click #today_missed': 'today_missed',
        'click #today_served': 'today_served',
        'click #today_left': 'today_left',
       },
       start: function() {
          rpc.query({
            route: '/dashboard',
            params: {},
            }).then(function (result) {
               result.forEach(function(rec){
                  document.getElementById("one").innerHTML = rec['1'];
                  document.getElementById("two").innerHTML = rec['2'];
                  document.getElementById("three").innerHTML = rec['3'];
                  document.getElementById("four").innerHTML = rec['4'];
                  document.getElementById("five").innerHTML = rec['5'];
                  document.getElementById("six").innerHTML = rec['6'];
                  document.getElementById("seven").innerHTML = rec['7'];
                  document.getElementById("eight").innerHTML = rec['8'];
                  document.getElementById("nine").innerHTML = rec['9'];
                  document.getElementById("ten").innerHTML = rec['10'];
             })
          })
          rpc.query({
            route: '/at_top',
            params: {},
            }).then(function (result) {
                result.forEach(function(rec){
                    $("#at_top_details").append("<tr><td class='text-center'>"+rec['name']+"</td><td class='text-center'>"+rec['served']+"</td><td class='text-center'>"+rec['cancelled']+"</td></tr>")
                })
          })
          google.charts.load('current', {'packages':['corechart']});
          google.charts.setOnLoadCallback(drawPieChart);
          function drawPieChart() {
            var data = google.visualization.arrayToDataTable([
              ['Task', 'Hours per Day'],
              ['Missed', 70],
              ['Served',  70],
              ['Left', 60]
            ]);
            var options = {
              title: ''
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
                  ['Missed',      70],
                  ['Served',  70],
                  ['Left', 60]
                ]);
                var options = {
                  title: ''
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
                  ['Year', 'Missed', 'Served', 'Left'],
                  ['1',  30,      100,   30],
                  ['2',  20,      120,   10],
                  ['3',  10,      110,   20],
                  ['4',  10,      130,   10],
                  ['5',  30,      100,   30],
                  ['6',  20,      120,   10],
                  ['7',  10,      140,   0],
                ]);
                var options = {
                  title: '',
                  curveType: 'function',
                  legend: { position: 'bottom' }
                };
                var chart = new google.visualization.LineChart(document.getElementById('sample'));
                chart.draw(data, options);
              }
        },
        today_queue: function(){
            this.do_action({
                    name: "Today Queue",
                    type: 'ir.actions.act_window',
                    res_model: 'tokens',
                    view_mode: 'tree,form',
                    views: [[false, 'list'],[false, 'form']],
                    domain: [],
                    target: 'current',
                })
        },
        today_missed: function(){
            this.do_action({
                    name: "Today Missed",
                    type: 'ir.actions.act_window',
                    res_model: 'tokens',
                    view_mode: 'tree,form',
                    views: [[false, 'list'],[false, 'form']],
                    domain: [['state', '=', 'cancelled']],
                    target: 'current',
                })
        },
        today_served: function(){
            this.do_action({
                    name: "Today Served",
                    type: 'ir.actions.act_window',
                    res_model: 'tokens',
                    view_mode: 'tree,form',
                    views: [[false, 'list'],[false, 'form']],
                    domain: [['state', '=', 'done']],
                    target: 'current',
                })
        },
        today_left: function(){
            this.do_action({
                    name: "Today Left",
                    type: 'ir.actions.act_window',
                    res_model: 'tokens',
                    view_mode: 'tree,form',
                    views: [[false, 'list'],[false, 'form']],
                    domain: [['state', '=', 'draft']],
                    target: 'current',
                })
        },
    })
core.action_registry.add('queue_dashboard', QueueDashBoard);
return QueueDashBoard;
})