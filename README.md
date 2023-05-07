# mini-net-python
Python mininet project

# Running project locally

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

To run python mininet script type:
```commandline
sudo python3 test.py
```

Then type:
mininet> dump
mininet> links

and put it on this website to visualize this Topology.

http://demo.spear.narmox.com/app/?apiurl=demo#!/mininet
