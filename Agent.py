from string import lower


from Traffic import Traffic

class Agent:
 
 def __init__(self,id_,type_,traffic_):
  self.id = id_
  self.type = type_
  self.traffic = traffic_


 # used to print the object representation
 def __repr__ (self):
  agent_id = lower(self.type) + '_' + self.id 
  return agent_id
  
 def getId(self):
  ''' get the object id '''
  return self.id

 def getType(self):
  ''' get the object type '''
  return self.type

 def getTrafficObject(self):
  ''' get the traffic Object '''
  return self.traffic
 
