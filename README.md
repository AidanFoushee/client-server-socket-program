# Overview

I started creating this project to further my learning about networking and to see what I can create.

I wrote 2 programs, one for the server and one for the client. The program works by running the server and then connecting the clients to it. You can do this by navigating in the terminal to the directory where the server/client program is, and then running the command 'python3 server.py' or 'python3 client.py' to run the corrosponding programs. The server needs to be running before the client, so that the client can connect to the server. You will know that the client is connected to the server when you see 'Connection Established' printed in the server terminal. The software is a story making game, where 2 clients can alternate sending words to the server to make a story.

My purpose for writing this software is to demonstrate my ability to learn something new and to further my learning and expand my knowledge.

[Software Demo Video](https://youtu.be/gmG4C-htNL8)

# Network Communication

client/server

I am using TCP using port number 1234

The format of the message being sent back and forth are just strings

# Development Environment

VS Code

Python

Socket Library

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python Server Library](https://docs.python.org/3.6/library/socketserver.html)
* [Python Socket Library](https://docs.python.org/3.6/library/socket.html)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Fix story title problem
* Make it so more than one story can be saved at a time
* Add error handlers
* Incorporate a cloud database to store the stories