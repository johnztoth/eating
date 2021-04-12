# eating

This model extends the functionality of the Agents model. This time an environment grid is initially read-in from the in.txt file. As an agent moves it eats the environment where it lands, 10 units at a time. If there are less than 10 environment units left when the agent lands it eats them all. Each agent also stores the value of how much it has eaten. If the agent eats more than 100 units it sicks them up where it is.

The final environment data (after it has been eaten by the agents) is written to a comma separated file called environment.txt.

Another file is written, store.txt, which shows the total amount eaten by all the agents. This file is appended to every time the model is run.

The print command for agents is overridden so that when you type "print(agents[x])" the agent location and store is printed.

Each agent now determines the size of the environment and makes sure it stays within that area.

The program plots the final agent positions after all the iterations and the final environment data.

The main program is in eating.py. The module containing the Agent class is in agentframework.py
