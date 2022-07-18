"use strict";

var _redis = require("redis");

var client = (0, _redis.createClient)();
client.on('error', function (err) {
  return console.log('Redis Client Error', err);
});
await client.connect();
await client.set('key', 'value');
var value = await client.get('key');