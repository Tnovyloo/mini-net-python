# mini-net-python
Python mininet project

# Running project locally

## Visualize topology to graph in jpg.

First of all we have to set up our python virtual environment, make sure that you are in the base directory of project (in command prompt).
Enter the command below.
```pycon
python3 -m venv venv
```

Then we have to activate created virtual environment.
```commandline
source venv/bin/activate
```

On left side of command prompt line there will be shown a "(venv)" text. That means we are activated virtual environment.

Next step is installing required libraries for project.
```pycon
pip install -r requirements.txt
```

Then run:
```pycon
python3 test.py
```
And have fun of creating networks.

Program service three ways of visualize network.

1. From builtin by us python CLI (Creating network in real time)
2. From test.py class NetworkTopoPythonAPI, where we could add hosts and switches statically
3. From Text file (MininetLinks.txt) where we put MININET LINKS output.
