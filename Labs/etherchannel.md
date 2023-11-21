# Etherchannel

Etherchannel uses **Port Aggregation**, in which multiple ports in a switch are grouped together to form a single logical link. 

### Uses:
* Increased Bandwidth
* Redundancy
* Fault Tolerance

Channelling can be achieve through,
1. Manual configuration using the command: `channel-group 1 mode on`
2. PAgP (Port Aggregation Protocol) - `channel-group 1 mode auto/desirable`
3. LACP - `channel-group 1 mode active/passive`

## Lab Image:
![etherchannel](https://github.com/k1r4nkv/Networks/assets/70469550/7cfd76a8-35b4-4d3c-8c09-a03d8f89009c)
