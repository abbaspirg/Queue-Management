odoo.define('queue_dashboard.dashboard_action', function (require){
"use strict";
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');
    var QueueDashBoard = AbstractAction.extend({
       template: 'QueueDashBoard',
    })
core.action_registry.add('queue_dashboard', QueueDashBoard);
return QueueDashBoard;
})