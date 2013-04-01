from Node import Node 
from Agent import Agent
from Traffic import Traffic
from Link import Link

from string import split
import re

traffic_gen_list = [] # traffic generators list
agent_list = [] # list of agents in the communication network
node_list = [] # list of nodes in the network
link_list = [] # list of links in the network

def createTraffic(id_,type_,fid_,rate_,packetSize_):
 ''' creates the traffic object and returns it'''
 traffic = Traffic(id_,type_,fid_,rate_,packetSize_)
 return traffic 

def createAgent(id_,type_,traffic_): 
 ''' creates agent, attaches to it a specific traffic and returns it '''
 traffic_gen = getTrafficGenerator(traffic_) # returns Traffic object with unique traffic_ id
 agent = Agent(id_,type_,traffic_gen)
 return agent

def createNode(id_,type_,agent_,processing_delay_):
 ''' create a node, attaches an agent and returns it '''
 agents = getAgent(agent_) # list of agents attached to the node
 node = Node(id_,type_,agents,processing_delay_)
 return node 

def createLink(id_,src_,dest_,bw_,p_delay_,q_principle_,q_length_):
 ''' create a link between the source and destination and returns it '''
 source = getNode(src_)
 destination = getNode(dest_)
 link = Link(id_,source, destination,bw_,p_delay_,q_principle_,q_length_)
 return link
 

def getNode(number):
 ''' returns the node with the given number '''
 node_list_len = len(node_list)
 for i in range(node_list_len):
  if int(number) == int(node_list[i].getId()) : return node_list[i]
   

def getAgent(number): # number is given as a list 
 ''' returns agent object with the given identifier '''
 attached_agents = []
 agent_list_len = len(agent_list)
 number_len = len(number)
 for i in range(number_len):
  for j in range(agent_list_len) : 
   if int(number[i]) == int(agent_list[j].getId()) : attached_agents.append(agent_list[j])    
 return attached_agents

def getTrafficGenerator(number):
 ''' returns traffic object with given identifier'''
 traffic_gen_list_len = len(traffic_gen_list)
 for i in range(traffic_gen_list_len):  
  if int(number) == int(traffic_gen_list[i].getId()): return traffic_gen_list[i]
  else : return None     

def cleanAgentList(data):
 ''' clean the data and get the agents '''
 only_agents = []
 temp_agents = re.split('[\[;\]]',data)
 for i in range(len(temp_agents)):
  if temp_agents[i] != '':
   only_agents.append(temp_agents[i])
 
 return only_agents


def readInput(filename):
 ''' reads the input file line by line and creates the objects ''' 
 with open(filename) as f_:
  for line in f_:
   #print line
   object_type,parameters = line.split(':')
   par_list = parameters.split(',')  
   par_list_len = len(par_list)
 
   if object_type == 'traffic' : 
    traffic_gen_list.append(createTraffic(par_list[0],par_list[1],par_list[2],par_list[3],par_list[4]))
   elif object_type == 'agent':
    agent_list.append(createAgent(par_list[0],par_list[1],par_list[2]))
   elif object_type == 'node':
    agents = cleanAgentList(par_list[2])
    node_list.append(createNode(par_list[0],par_list[1],agents,par_list[3]))
   elif object_type == 'link':
    link_list.append(createLink(par_list[0],par_list[1],par_list[2],par_list[3],par_list[4],par_list[5],par_list[6]))





if __name__ == '__main__':

 filename = 'input.txt'
 readInput(filename)

 for i in range(len(agent_list)):
  try :
   print agent_list[i],agent_list[i].type,agent_list[i].traffic
   print agent_list[i].traffic,agent_list[i].traffic.type,agent_list[i].traffic.rate
  except AttributeError:
   pass
 print '\n'
 for i in range(len(node_list)):
  try:
   print node_list[i],node_list[i].type,node_list[i].processing_delay,node_list[i].agent
  except AttributeError:
   pass
 print '\n'
 for i in range(len(link_list)):
  try:
   print link_list[i].id,link_list[i].tail,link_list[i].head,link_list[i].bw
  except AttributeError:
   pass

