from __future__ import print_function

import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Intf
from mininet.node import Controller

import networkx as nx
import matplotlib.pyplot as plt

class NetworkTopo(Topo):
    # Builds network topology
    def build(self, **_opts):

        # s1 = self.addSwitch('s1', failMode='standalone')
        s2 = self.addSwitch('s2', failMode='standalone')

        #
        # # Adding hosts
        # d1 = self.addHost('d1', ip='192.168.0.1/28')
        # d2 = self.addHost('d2', ip='192.168.0.2/28')
        # d3 = self.addHost('d3', ip='192.168.0.3/28')
        # d4 = self.addHost('d4', ip='192.168.0.9/28')
        # d5 = self.addHost('d5', ip='192.168.0.10/28')
        # d6 = self.addHost('d6', ip='192.168.0.11/28')
        #
        # d7 = self.addHost('d7', ip='192.168.0.12/28')
        # self.addLink(d7, s2)
        #
        # # Connecting hosts to switches
        # for d, s in [(d1, s1), (d2, s1), (d3, s1)]:
        #     self.addLink(d, s)
        # for d, s in [(d4, s1), (d5, s1), (d6, s1)]:
        #     self.addLink(d, s)
        choice = 0
        switch_list = []

        while choice != 5:
            print("\nWhat do you want to do?\n"
                  "Add switch? Type 1\n"
                  "Add hosts? Type 2\n"
                  "Add link between switch? Type 3\n"
                  "Visualize topology? Type 4\n"
                  "Exit? Type 5\n")

            choice = int(input("Choice: "))

            if choice == 1:
                switch_name = input("Input name of switch: ")
                switch_list.append([self.addSwitch(f"{switch_name}", failMode='standalone'), 0])

            if choice == 2:
                count_of_hosts = 0
                while count_of_hosts == 0:

                    hosts = int(input("How many hosts do you want to add? range between 1-254: "))
                    if 1 <= hosts <= 254:
                        count_of_hosts = hosts

                for i, switch in enumerate(switch_list):
                    print(f"Index: [{i}] - Switch Name and hosts: {switch}")

                user_switch_choice = int(input("Type index of switch are you interested in: "))

                user_switch_hosts = switch_list[user_switch_choice][1]
                user_switch = switch_list[user_switch_choice][0]

                if count_of_hosts + user_switch_hosts >= 255:
                    print("Sorry but we cant add more hosts to this IP")

                else:

                    switch_list[user_switch_choice][1] = int(count_of_hosts) + int(user_switch_hosts)

                    hosts_ip = [f"192.168.0.{x}/28" for x in range(count_of_hosts)]
                    hosts_list = [self.addHost(f"{str(user_switch)}_d{index}", ip=f"{ip}") for index, ip in enumerate(hosts_ip)]

                    for h in hosts_list:
                        self.addLink(user_switch, h)

                    print(f"\nLinked {count_of_hosts} hosts to switch '{user_switch}'")

            if choice == 3:
                for i, switch in enumerate(switch_list):
                    print(f"Index: [{i}] - Switch Name and hosts: {switch}")

                switch_1 = switch_list[int(input("Type index of switch 1 are you interested in: "))][0]
                switch_2 = switch_list[int(input("Type index of switch 2 are you interested in:"))][0]
                self.addLink(switch_1, switch_2)
                print(f"Added link between {switch_1} and {switch_2}")

            if choice == 4:
                topo_links = self.links()
                graph = nx.Graph()
                graph.add_edges_from(topo_links)

                # Saving graph to file
                file_name = input("Type filename: ")
                nx.draw(graph, with_labels=True)
                plt.savefig(f"{file_name}.jpg", dpi=300)

def run():
    topo = NetworkTopo()

    # choice = input("Visualize topology to jpg? (y/n): ")
    # if choice.lower() == "y":
    #     # Exporting mininet topology to list of edges by .links() function, and creating it in NetworkX
    #     # https://github.com/bigswitch/mininet/blob/master/mininet/topo.py
    #
    #     topo_links = topo.links()
    #     graph = nx.Graph()
    #     graph.add_edges_from(topo_links)
    #
    #     # Saving graph to file
    #     file_name = input("Type filename: ")
    #     nx.draw(graph, with_labels=True)
    #     plt.savefig(f"{file_name}.jpg", dpi=300)

    # To run Mininet uncomment below code.

    # net = Mininet(topo=topo, controller=None)
    # net.start()


    # Make Switch act like a normal switch
    # net['s1'].cmd('ovs-ofctl add-flow s1 action=normal')
    # Make Switch act like a hub
    # net['s1'].cmd('ovs-ofctl add-flow s1 action=flood')

    # CLI(net)
    # net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
