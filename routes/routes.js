'use strict';
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res) {
    // get groups
    var request_url = "";
    var groups = [
        { name: "BroFinder", password: "Password1" },
        { name: "EECS 441", password: "Password2" }
    ];
    
    res.render('home', { page: 'BroFinder', menuId: 'home', groups: groups });
});

/* GET group page. */
router.get('/group/*', function (req, res) {
    var name = req.url.slice(-1)[0];
    var groupMembers = [
        { name: "Nathan Ritsema", initials: "NR" },
        { name: "Julian Tran", initials: "JT" },
        { name: "Tom Wilcox", initials: "TW" }
    ];

    res.render('group', { page: 'Group Page', menuId: 'group', groupName: name, groupMembers: groupMembers });
});

module.exports = router;
