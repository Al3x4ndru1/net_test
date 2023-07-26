#!/usr/bin/python

import sys
from Check_host_range import check_host_range
from Create_topology import Create_Topology

def mininet(ipBase,
            controller_ip,
            controller_port,
            switches_name_prefix,
            hosts_name_prefix,
            number_of_switches,
            number_of_hosts):
    try:
        
        if(controller_port != 0):
            if (check_host_range(ipBase,
                                    number_of_hosts,
                                    number_of_switches)):
                
                topology = Create_Topology(ipBase,
                                        controller_ip,
                                        controller_port,
                                        switches_name_prefix,
                                        hosts_name_prefix,
                                        number_of_switches,
                                        number_of_hosts)
                topology.create_topology()
                
            else:
                print ('''Too many hosts the specified base Ip \n 
    1) You can reduce number of hosts per device \n 
    2) You can increase the number of hosts in the network''')
                
        else:
            
            if (check_host_range(ipBase,hosts_name_prefix)):
                topology = Create_Topology(ipBase,
                                        controller_ip,
                                        6633,
                                        switches_name_prefix,
                                        hosts_name_prefix,
                                        number_of_switches,
                                        number_of_hosts)
                topology.create_topology()
            else:
                return "Too many hosts the specified base Ip"
                
    except Exception as e:
        return e
            
    return "Topology created"



if __name__ == '__main__':
    mininet(sys.argv[1],
            sys.argv[2],
            int(sys.argv[3]),
            sys.argv[4],
            sys.argv[5],
            int(sys.argv[6]),
            int(sys.argv[7]))
