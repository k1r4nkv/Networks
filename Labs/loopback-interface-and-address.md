# Loopback interface
1. Used for routing protocols, reachability, and testing purposes.
2. OSPF uses loopback interfaces to determine their properties.

**Commmands**
To create a loopback interface:
```
interface loopback 0
ip add 11.0.0.1 255.0.0.0
```
To check interfaces:
`show ip interface brief`

# Loopback Address
It starts from 127.0.0.0 to 127.255.255.255  where the IP 127.255.255.255 is a broadcast IP.  
The loopback address are always accessible. Thus useful for trouble shooting.

# Lab
![image](https://github.com/k1r4nkv/Networks/assets/70469550/45e0bbb3-5062-479c-8866-fa8564717591)
