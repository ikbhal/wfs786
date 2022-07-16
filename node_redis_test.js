var redis = require('redis');


var client = redis.createClient();

client.on('error', (err) => console.log('Redis Client Error', err));

// await client.connect();
// client.on('')
client.connect().then(()=> console.log('connect successfully'));

client.set('allah', '786');
const value = client.get('allah');
console.log("value:" + value);