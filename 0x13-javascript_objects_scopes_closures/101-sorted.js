#!/usr/bin/node
// script that imports dictionary of occurrences by user id 
//and computes a dictionary of user ids by occurrence..

const dict = require('./101-data').dict;
const newDict = dict.map (function (key, userid) {
    return (key, userid);
});
console.log(newDict);