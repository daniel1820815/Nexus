#! /usr/bin/env python
"""

add-vlan.py
Illustrate the following concepts:
- Input vlan ID and name
- Compare new vlan with existing vlans
- Abort program if new vlan already exists and print error message
- Add new vlan if it does not exists
"""

__author__ = "Daniel Kuhl"
__author_email__ = "kuhl@nscon.de"
__copyright__ = "Copyright (c) 2018 NSCON Network Services & Consulting GmbH"

import sys

# List of existing vlans // Needs to be exported from configuration later or put in a separate file
vlans = {"101":"Client1","102":"Client2"}

# Entry point for the programm
if __name__ == '__main__':
    print("The current vlans are")
    for vlan in vlans:
        print(vlan)
    print("")
    
    # Add new vlan and check if new vlan already exists
    new_vlan = input("Add new vlan ID: ")
    if new_vlan not in vlans:
        print("# That's a new vlan, adding to the configuration")
        print("cli(conf t)")
        print("cli(vlan "+new_vlan+")")
        print("cli(end)")
        print("")
    else: 
        print("Error - vlan " +new_vlan+ " already exists!")
        print("")