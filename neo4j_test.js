const neo4j = require('neo4j-driver')


var uri = "neo4j://localhost:7687"
var user = "neo4j"
var password = "neo4j"

const driver = neo4j.driver(uri, neo4j.auth.basic(user, password))
const session = driver.session()
const personName = 'Alice'

try {
  session.run(
    'CREATE (a:Person {name: $name}) RETURN a',
    { name: personName }
  ).then((result=>{
    const singleRecord = result.records[0]
    const node = singleRecord.get(0)
  
    console.log(node.properties.name)
  }));

  
} finally {
  session.close().then(()=>{
    console.log("close session ");
    driver.close();
  });
}

// on application exit:
