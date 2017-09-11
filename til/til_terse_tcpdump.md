# Terse `tcpdump`

Sometimes, you only care about the source and destination information from
traffic dumps. A combination of `tcpdump` arguments and utilities will present
just that.

## Sample `tcdump`

    bandarbox:~ sje$ tcpdump -c 5 -n -r /tmp/a.pcap
    13:39:17.176005 IP 4.5.67.78.443 > 10.0.0.25.61812: Flags [P.], seq 3332420323:3332420334, ack 3871453152, win 42, options [nop,nop,TS val 850993550 ecr 216824716], length 11
    13:39:17.176123 IP 10.0.0.25.61812 > 4.5.67.78.443: Flags [.], ack 11, win 4095, options [nop,nop,TS val 216827628 ecr 850993550], length 0
    13:39:17.612647 IP6 fe80::200:caff:fe11:2233 > ff02::1: ICMP6, router advertisement, length 96
    13:39:17.613650 IP 8.9.10.11.443 > 10.0.0.25.61815: Flags [P.], seq 68423302:68423456, ack 2283575794, win 1216, options [nop,nop,TS val 3711286562 ecr 216826907], length 154
    13:39:17.613736 IP 10.0.0.25.61815 > 8.9.10.11.443: Flags [.], ack 154, win 4091, options [nop,nop,TS val 216828065 ecr 3711286562], length 0

## Less Information

    bandarbox:~ sje$ tcpdump -c 5 -t -n -q -r /tmp/a.pcap
    IP 4.5.67.78.443 > 10.0.0.25.61812: tcp 11
    IP 10.0.0.25.61812 > 4.5.67.78.443: tcp 0
    IP6 fe80::200:caff:fe11:2233 > ff02::1: ICMP6, router advertisement, length 96
    IP 8.9.10.11.443 > 10.0.0.25.61815: tcp 154
    IP 10.0.0.25.61815 > 8.9.10.11.443: tcp 0

## Least Information

    bandarbox:~ sje$ tcpdump -c 5 -tnqr /tmp/a.pcap | awk '{ print $2,$3,$4 }' | sed 's/:$//'
    4.5.67.78.443 > 10.0.0.25.61812
    10.0.0.25.61812 > 4.5.67.78.443
    fe80::222:aaff:fe22:2233 > ff02::1
    8.9.10.11.443 > 10.0.0.25.61815
    10.0.0.25.61815 > 8.9.10.11.443
