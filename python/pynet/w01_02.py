#!/usr/bin/env python

"""
Prompt a user to enter in an IP address from standard input. Read the IP 
address in and break it up into its octets. Print out the octets in 
decimal, binary, and hex.

Your program output should look like the following:

​$ python exercise2.py 
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in 
the column.
"""

import socket

def ask_ipv4_addr():
    while True:
        ip_addr = input('Enter IPv4 address: ')
        try:
            socket.inet_aton(ip_addr)
        except socket.error:
            print('Error, invalid address: {}. Try again.'.format(ip_addr))
        else:
            return ip_addr

def ipv4_breakdown(ip_addr):
    octets = [o for o in ip_addr.split('.')]
    row = '{:^15}{:^15}{:^15}{:^15}'
    print(row.format(*['Octet{}'.format(i) for i in range(1, 5)]))
    print(row.format(*['-' * 15 for _ in range(4)]))
    print(row.format(*octets))
    print(row.format(*[bin(int(o)) for o in octets]))
    print(row.format(*[hex(int(o)) for o in octets]))
    print(row.format(*['-' * 15 for _ in range(4)]))

def main():
    ip_addr = ask_ipv4_addr()
    ipv4_breakdown(ip_addr)

if __name__ == '__main__':
    main()
