"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _express = _interopRequireDefault(require("express"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

// var express = require('express');
var router = _express["default"].Router();
/* GET users listing. */


router.get('/', function (req, res, next) {
  res.send('respond with a resource');
}); // router.get('redis_test', function(req,res, next){
//   const client = createClient();
//   client.on('error', (err) => console.log('Redis Client Error', err));
//   await client.connect();
//   await client.set('allah', '786');
//   const value = await client.get('allah');
//   console.log("value retrieved from redis ", value);
//   res.send("value retrieved from redis "+ value);
// });
// module.exports = router;

var _default = router;
exports["default"] = _default;