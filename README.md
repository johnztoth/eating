# eating

Read in an environment grid (list of lists) from an external file, in.txt. 
Create a number of Agents, each with a random x and y coordinate.
Cycle through a number of iteration steps.
For each iteration randomly move the agent by +/- 1 unit in each direction.
The agent must stay within the bounds of the environment.
As the agent moves it eats the environment, 10 units at a time.
If there are less than 10 environment units left the agent eats them all.
If the agent eats more than 100 units it sicks them up where it is.
Plot the final agent positions and the environment data.
