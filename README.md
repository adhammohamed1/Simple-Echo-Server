# Simple-Echo-Server
Python echo server that receives a string from a client, processes it and returns it

## Table of Contents
- [Functionality](#functionality)
    + [What happens at the server side?](#what-happens-at-the-server-side)
    + [What happens at the client side?](#what-happens-at-the-client-side)
- [Packet Sniffing Using Wireshark](#packet-sniffing-using-wireshark)

## Functionality

### What happens at the server side?

- The server will take one line from the client each time.
- The server then receives the client's request then orders the characters of the string according to the operation specified by the first character and sends the ordered string back to the client.
- If the first character is:
    + ‘A’ then the order will be ascending.
    + ‘C’ the order will be preserved but all letters will be capitalized.
    + ‘D’ the order will be descending.
    + Else, the server will return the same message it receives.

### What happens at the client side?
- The client generates 5 random strings with the first character more likely to be 'A' , 'C' or 'D'.
- The client then sends the string to the server and awaits a response
- The client receives a response from the server and prints it on the terminal.

## Packet Sniffing Using Wireshark

Wireshark was used to catch packets from the communication session. The following screenshot shows an example:
