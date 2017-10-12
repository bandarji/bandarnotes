# Use iptables Instead of firewalld

CentOS 7, for example, uses firewalld for network access controls. If you
want to revert to using iptables, disable the new system with this command.

```bash
systemctl stop firewalld
systemctl mask firewalld
yum install iptables-services
systemctl enable iptables
systemctl start iptables
```

## A Few Example Rules, Just Because

```bash
iptables -A INPUT -i eth1 -p tcp --dport 80 -d 1.2.3.4 -j ACCEPT # append
iptables -A OUTPUT -o eth1 -p tcp --sport 80 -j ACCEPT
iptables -I INPUT 3 -i eth1 -p udp -j ACCEPT # insert
iptables -I INPUT 4 -i eth1 -p udp --dport 80 -j DROP
iptables -L INPUT # list
iptables -L INPUT --line-numbers
iptables -L INPUT -n --line-numbers
iptables -D INPUT -i eth1 -p tcp --dport 80 -d 1.2.3.4 -j ACCEPT # delete
iptables -D INPUT 2
iptables -F INPUT # flush
iptables -R INPUT 1 -i eth1 -p tcp --dport httpht -d 1.2.3.4 -j ACCEPT # replace
iptables -L -t nat # specific table
iptables -N MY_CHAIN # new chain
iptables -E MY_CHAIN NEW_CHAIN # rename
iptables -X NEW_CHAIN # delete
iptables -A INPUT -p icmp -j MY_CHAIN # jump
iptables -P INPUT DROP # default policy
iptables -A INPUT -i eth0 -p tcp --syn -m limit --limit 10/second -j ACCEPT # SYN flood
iptables -A INPUT -m state --state INVALID -j DROP # drop invalid state packets
iptables -A INPUT -f -j DROP # drop fragments
```

## Saving Rules

```bash
iptables-save > /etc/sysconfig/iptables # Red Hat
service iptables save # CentOS 7
iptables-save -t filter # single table
# iptables-restore to, well, restore
```
