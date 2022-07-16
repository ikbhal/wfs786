// var express = require('express');
import express from 'express';



var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('redis_test', function(req,res, next){

  const client = createClient();

  client.on('error', (err) => console.log('Redis Client Error', err));

  await client.connect();

  await client.set('allah', '786');
  const value = await client.get('allah');

  console.log("value retrieved from redis ", value);

  res.send("value retrieved from redis "+ value);
});

// module.exports = router;
export default router;
