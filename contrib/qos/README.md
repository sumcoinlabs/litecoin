### Qos ###

<<<<<<< HEAD
This is a Linux bash script that will set up tc to limit the outgoing bandwidth for connections to the Litecoin network. It limits outbound TCP traffic with a source or destination port of 9333, but not if the destination IP is within a LAN.
=======
This is a Linux bash script that will set up tc to limit the outgoing bandwidth for connections to the Litecoin network. It limits outbound TCP traffic with a source or destination port of 9333, but not if the destination IP is within a LAN (defined as 192.168.x.x).
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5

This means one can have an always-on litecoind instance running, and another local litecoind/litecoin-qt instance which connects to this node and receives blocks from it.
