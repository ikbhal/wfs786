//https://blog.risingstack.com/graphs-graphdbs-and-javascript-exploring-trumpworld/
// not working neo4j.auth failing
const database = 'bolt://localhost';
const neo4j = require('neo4j-driver').v1;
// const auth = neo4j.auth.basic('neo4j', 'omega16');
const driver = neo4j.driver(database, auth);


driver.onError = (error) => {
  console.log('Driver instantiation failed', error);
};