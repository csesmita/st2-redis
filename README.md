# st2-redis

This pack is an effort to interface with Redis Server.

### Assumption
Redis Server is installed and running at the host and port provided.

### Usage

----------
$ st2 run st2_redis.myredis var='Class' value='Omega'

.

id: 59678718d9d3e909478bac21

status: succeeded

parameters: 

  value: Omega
  
  var: Class

result: 
  
  exit_code: 0
  
  result: "+OK

"
  
  stderr: ''
  
  stdout: "+OK


"
----------
$ st2 run st2_redis.myredis var='Class'
.

id: 59678723d9d3e909478bac24

status: succeeded

parameters: 
  
  var: Class

result: 
  
  exit_code: 0
  
  result: "$5

Omega

"
  
  stderr: ''
  
  stdout: "$5

Omega


"

### To Do 
1. Support GET/SET timer properties
2. Support List Operations
3. Support Sorted Lists Operations
4. Support SAVE 
5. Support DB initialization from an input file
