import redis


r = redis.StrictRedis(host='172.17.0.2', port=6379, db=0)
r.set('foo', 'bar')
value = r.get('foo')
print(value)
