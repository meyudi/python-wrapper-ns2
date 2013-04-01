from Node import Node


class Link:

	def  __init__(self,id_,src_,dest_,bw_,p_delay_,q_principal_,q_length_):
		self.id = id_
		self.tail =  src_
		self.head = dest_
		self.bw = bw_
		self.p_delay = p_delay_
		self.q_prinicpal = q_principal_
		self.q_length = q_length_

	def __repr__(self):
		agent_id = 'link_' + self.id 
  		return agent_id

  	def getId(self):
  		return self.id

  	def getSource(self):
  		return self.tail

  	def getDestination(self):
  		return self.head

  	def getBw(self):
  		return self.bw

  	def getPropagationDelay(self):
  		return self.p_delay

  	def getQPrinciple(self):
  		return self.q_principal

  	def getQLength(self):
  		return self.q_length





		