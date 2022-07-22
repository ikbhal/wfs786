import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
print("get value of foo key", r.get('foo'))
# b'bar'
print ("redis connect start")
r = redis.Redis()
# r.graph("social
# reply = r.graph("social").query("MATCH (r:Rider)-[:rides]->(t:Team {name:'Ducati'}) RETURN count(r)")