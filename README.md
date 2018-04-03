# DoS_Attack
Denial of Service Attack   

A simple denial of service implementation using python.
A socket is created and a connection is created with a SOCK_STREAM which is a connection-based protocol. 
The connection is established and the two parties have a conversation until the connection is terminated
by one of the parties or by a network error. 
A loop will run first connecting to an address, then sending some data, finally closing the connection.

The attack was tested on a Xender server. It does crash the service and then crash the App.
