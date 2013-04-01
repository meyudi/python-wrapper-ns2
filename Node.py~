from string import lower

from Agent import Agent
from Traffic import Traffic

class Node:
 
 def __init__(self,id_,type_,agent_,processing_delay_):
  self.id = id_
  self.type = type_
  self.processing_delay = processing_delay_
  self.agent = agent_ # list of agents

 def __repr__ (self):
  agent_id = lower(self.type) + '_' + self.id 
  return agent_id

 def getId(self):
  return self.id

 def getType(self):
  return self.type

 def getProcessingDelay(self):
  return self.processing_delay
 
