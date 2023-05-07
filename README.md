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

Then type in mininet> :
```commandline
dump
```
And output of this command is:
```commandline
<Host d1: d1-eth0:192.168.0.1 pid=9217> 
<Host d2: d2-eth0:192.168.0.2 pid=9219> 
<Host d3: d3-eth0:192.168.0.3 pid=9221> 
<Host d4: d4-eth0:192.168.0.9 pid=9223> 
<Host d5: d5-eth0:192.168.0.10 pid=9225> 
<Host d6: d6-eth0:192.168.0.11 pid=9227> 
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None,s1-eth3:None,s1-eth4:None,s1-eth5:None,s1-eth6:None pid=9232> 
```
Then type this command:
```commandline
links
```
And the output of links is:
```commandline
d1-eth0<->s1-eth1 (OK OK) 
d2-eth0<->s1-eth2 (OK OK) 
d3-eth0<->s1-eth3 (OK OK) 
d4-eth0<->s1-eth4 (OK OK) 
d5-eth0<->s1-eth5 (OK OK) 
d6-eth0<->s1-eth6 (OK OK) 
```

Now we have to put our above data from mininet to this website to visualize this Topology.

http://demo.spear.narmox.com/app/?apiurl=demo#!/mininet
