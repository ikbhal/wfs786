const database = 'bolt://localhost';
const neo4j = require('neo4j-driver').v1;

const auth = neo4j.auth.basic('neo4j', 'omega16');
const driver = neo4j.driver(database, auth);

console.log("START");
driver.onError = (error) => {
  console.log('Driver instantiation failed', error);
}

console.log("END");