# wfs783


---
alternative 
  free opensource graph db 
    explore here https://en.wikipedia.org/wiki/Graph_database

---
trying other database

redis graph
---

https://redis.io/docs/stack/graph/


docker
docker run -p 6379:6379 -it --rm redislabs/redisgraph

PS D:\git_tauqeer\wfs786> docker run -p 6379:6379 -it --rm redislabs/redisgraph
docker: error during connect: This error may indicate that the docker daemon is not running.: Post "http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/containers/create": open //./pipe/docker_engine: The system cannot find the file specified.
See 'docker run --help'.

uninstall docker desktop
install docker desktop


---
redis-cli

127.0.0.1:6379> GRAPH.QUERY MotoGP "CREATE (:Rider {name:'Valentino Rossi'})-[:rides]->(:Team {name:'Yamaha'}), (:Rider {name:'Dani Pedrosa'})-[:rides]->(:Team {name:'Honda'}), (:Rider {name:'Andrea Dovizioso'})-[:rides]->(:Team {name:'Ducati'})"
1) 1) "Labels added: 2"
   2) "Nodes created: 6"
   3) "Properties set: 6"
   4) "Relationships created: 3"
   5) "Cached execution: 0"
   6) "Query internal execution time: 0.399000 milliseconds"

---

Now that our MotoGP graph is created, we can start asking questions. For example: Who's riding for team Yamaha?

127.0.0.1:6379> GRAPH.QUERY MotoGP "MATCH (r:Rider)-[:rides]->(t:Team) WHERE t.name = 'Yamaha' RETURN r.name, t.name"
1) 1) "r.name"
   2) "t.name"
2) 1) 1) "Valentino Rossi"
      2) "Yamaha"
3) 1) "Cached execution: 0"
   2) "Query internal execution time: 0.625399 milliseconds"

---
python example
import redis

r = redis.Redis()
reply = r.graph("social").query("MATCH (r:Rider)-[:rides]->(t:Team {name:'Ducati'}) RETURN count(r)")

---
https://redis.io/docs/clients/

rebridge
----
node-redis
A high-performance Node.js Redis client.

---

https://www.npmjs.com/package/redisgraph.js

---
https://www.npmjs.com/package/redisgraph.js
https://redis.io/commands/graph.query/
