"""
Eating

Read in an environment grid (list of lists) from an external file, in.txt. 
Create a number of Agents, each with a random x and y coordinate.
Cycle through a number of iteration steps.
For each iteration randomly move the agent by +/- 1 unit in each direction.
The agent must stay within the bounds of the environment.
As the agent moves it eats the environment, 10 units at a time.
If there are less than 10 environment units left the agent eats them all.
If the agent eats more than 100 units it sicks them up where it is.
Plot the final agent positions and the environment data.
"""

import matplotlib.pyplot
import agentframework
import csv

""" create environment list and append the in.txt data """
f = open('in.txt', newline='')

environment=[]

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:     # A list of rows
    rowlist=[]
    for value in row:  # A list of value
        rowlist.append(value)
        #rowlist.append(100)  test environment
    environment.append(rowlist)
f.close() 

""" function to determine distance between two agents """
def distance_between(agents_row_a, agents_row_b):
    dy=agents_row_b.y-agents_row_a.y
    dx=agents_row_b.x-agents_row_a.x
    return((dx**2+dy**2)**0.5)  

""" define no. of agents and no. of iterations. define agents list """
num_of_agents = 10
num_of_iterations = 1000
agents = []

""" Make the agents using the Agent class """
for i in range(num_of_agents):        
    agents.append(agentframework.Agent(environment))

""" Move the agents using the move method and eat the environment """
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

""" plot the agents and the environment """
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color="red")
matplotlib.pyplot.show()

""" write the environment data as a space separated file """
f = open('environment.txt', 'w', newline='')
writer = csv.writer(f, delimiter=',')
for row in environment:
    writer.writerow(row) 
f.close()

""" write how much all the agents have eaten """
total=0.0
f=open("store.txt","a")
for agent in agents:
    total=total+agent.store    
print(total,file=f)
f.close()



