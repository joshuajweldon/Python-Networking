#Python-Networking

Networking is a powerful tool, and with social gaming on the rise, it is important to learn the basics of networking. Whether you are playing clash-of-clans or a sending a snapchat, networking is deeply rooted in today's applications. 


<p align="center"><img src="" width="40%" height="40%"></img></p>

###Objective
Create a simple ASCII game you can play online with your friends using some basic networking in Python!!!

###Prerequisites
* Python basics (ie. variable declarations, conditionals, loops)
* Python methods

###Requirements
* Python
* Text Editor
* Network Connection

###Desired Outcomes
Upon finishing this project, students should:
* Understand basic networking in Python

###Your Challenge
Get started:

1. Fork and Clone this repo
2. Read, understand, and play with the existing server.py and client.py files. 
3. On paper, imagine a simple 2-player turn-based game (one that can be shown in ascii is preferred.)
2. Create player1.py and player2.py files using server.py and client.py as a blueprint.

####Step 2 - Read, Understand, and Play
1. Get with a partner, label yourselves as either client or server.
2. The person labeled server will run their program first (`python server.py <port>` NOTE: you may choose any integer for your port as long as its not being used by another service, I find 8080 works fine)
3. The person labeled client will run their program next (`python client.py <server IP> <port>` NOTE: if you are on the same local network, put in the server’s local IP address)
4.  Follow the instruction on the screen, to send a single message to each other.

#####Sockets
For simplicity, lets just imagine a socket as a house (IP Address) and door (port). There are many doors for a house, but we are going to use a particular door for each particular task. Car go through a garage door, and guest arrive at the front door. For networking, website servers (HTTP) use port 80 and file transfer services (FTP) use port 21. There are ports for all different kinds of server applications, from email servers to database servers. Its a good way for computers to connect to the right applications and prevent confusion, for you wouldn't want a guest to arrive and knock at your bedroom window.

#####server.py
All servers do basically the same thing, `bind()`, `listen()`, and `accept()` with a socket.

In order to prepare itself, a server application needs to `bind()` to the computer’s address and port. Once it has reserved its port, it must begin to `listen()` for any client to arriving. Last, once a client has arrived, it can `accept()` the client to connect to its application. 

>Trace the `server.py` source code and see if you can find the `bind()`, `listen()`, and `accept()` methods. Each method should be using the socket variable. 

#####client.py
The clients job is much easier. If you know the address and port you wish to connect to, you just need to create a socket with such information, and `connect()` to it.

> Trace the `client.py` source code and see if you can locate the `connect()` method.

#####Connections 
Once the connection is made, both the client and server can now `recv()` and `sendall()` data back and forth. But make sure you alway `close()` a connection when finished. This can prevent hacks and unnecessary problems with your ports.

> Try to locate `recv()` and `sendall()` in both `server.py` and `client.py`. Notice anything about the order of `recv()` and `sendall()`. If both applications tried to `recv()` at the same time, what do you think would happen? Try to imagine two friends both wait for a message to come to their house. If both are **waiting** will they ever move?

> Also, try to find `close()` in both `server.py` and `client.py`. 

#####Play
Feel free to change these programs to do anything you wish, such as:
* Add for loops to the `recv()` and `sendall()` so you can have a continues chat (How would you end the loop to close the connection)


####Step 3 - Draw out a game

Ok, I think you are ready. Knowing what you are capable of think up a game where the players take turns. Draw it out on paper. Who goes first? How do you communicate moves? How do you win? 

> It will help to keep it really simple, you can alway go back and build upon the game later.

####Step 4 - Create the game

Create the `player1.py` and `player2.py`. Let `player1.py` be the server and `player2.py` be the client. These two applications should communicate with each other until there is a winner.

> It would help to have the following methods: 
>`printGameBoard()`
>`movePlayer1()`
>`movePlayer2()`
>`checkGameStatus()` Did someone win?

> Don’t forget to `close()` before you exit the application.

####Stretch
If you are happy with you game, can you create a 3rd player? How would you do it?

###Resources
* [Python: sockets](https://docs.python.org/2/library/socket.html)
* [TechCrunch: six ASCII games](https://techcrunch.com/2009/02/06/ascii-based-games-roundup/)
