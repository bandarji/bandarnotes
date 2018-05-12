# TCP Project


## CPAN

```
Linux::Proc::Net::TCP
Decoding the data in /proc/net/tcp:

Linux 5.x  /proc/net/tcp
Linux 6.x  /proc/PID/net/tcp

Given a socket:

$ ls -l  /proc/24784/fd/11
lrwx------ 1 jkstill dba 64 Dec  4 16:22 /proc/24784/fd/11 -> socket:[15907701]

Find the address

$ head -1 /proc/24784/net/tcp; grep 15907701 /proc/24784/net/tcp
  sl  local_address rem_address   st  tx_queue  rx_queue tr tm->when  retrnsmt   uid  timeout inode
  46: 010310AC:9C4C 030310AC:1770 01 0100000150:00000000  01:00000019 00000000  1000 0 54165785 4 cd1e6040 25 4 27 3 -1

46: 010310AC:9C4C 030310AC:1770 01 
|   |         |   |        |    |--> connection state
|   |         |   |        |------> remote TCP port number
|   |         |   |-------------> remote IPv4 address
|   |         |--------------------> local TCP port number
|   |---------------------------> local IPv4 address
|----------------------------------> number of entry

00000150:00000000 01:00000019 00000000 
|        |        |  |        |--> number of unrecovered RTO timeouts
|        |        |  |----------> number of jiffies until timer expires
|        |        |----------------> timer_active (see below)
|        |----------------------> receive-queue
|-------------------------------> transmit-queue

1000 0 54165785 4 cd1e6040 25 4 27 3 -1
|    | |        | |        |  | |  |  |--> slow start size threshold, 
|    | |        | |        |  | |  |       or -1 if the treshold
|    | |        | |        |  | |  |       is >= 0xFFFF
|    | |        | |        |  | |  |----> sending congestion window
|    | |        | |        |  | |-------> (ack.quick<<1)|ack.pingpong
|    | |        | |        |  |---------> Predicted tick of soft clock
|    | |        | |        |               (delayed ACK control data)
|    | |        | |        |------------> retransmit timeout
|    | |        | |------------------> location of socket in memory
|    | |        |-----------------------> socket reference count
|    | |-----------------------------> inode
|    |----------------------------------> unanswered 0-window probes
|---------------------------------------------> uid


timer_active:
0 no timer is pending
1 retransmit-timer is pending
2 another timer (e.g. delayed ack or keepalive) is pending
3 this is a socket in TIME_WAIT state. Not all field will contain data.
4 zero window probe timer is pending

==========================================
Perl script to decode the address

#!/usr/bin/perl

my $hexip=$ARGV[0];
my $hexport=$ARGV[1];

print "hex: $hexip\n";

my @ip = map hex($_), ( $hexip =~ m/../g );

my $ip = join('.',reverse(@ip));

my $port = hex($hexport);

print "IP: $ip  PORT: $port\n";

==========================================

$ hexip.pl 030310AC 1770
hex: 030310AC
IP: 172.16.3.3  PORT: 6000

```

## States

```c
enum {
    TCP_ESTABLISHED = 1,             /* 0x01 */
    TCP_SYN_SENT,                    /* 0x02 */
    TCP_SYN_RECV,                    /* 0x03 */
    TCP_FIN_WAIT1,                   /* 0x04 */
    TCP_FIN_WAIT2,                   /* 0x05 */
    TCP_TIME_WAIT,                   /* 0x06 */
    TCP_CLOSE,                       /* 0x07 */
    TCP_CLOSE_WAIT,                  /* 0x08 */
    TCP_LAST_ACK,                    /* 0x09 */
    TCP_LISTEN,                      /* 0x10 */
    TCP_CLOSING,    /* Now a valid state */
    TCP_MAX_STATES  /* Leave at the end! */
};
```
