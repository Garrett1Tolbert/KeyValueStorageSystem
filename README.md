# KeyValueStorageSystem
Key-value storage system for Data Communications and Network Programming

Project 1: Key-Value Storage System 

Project Description

This project introduces the concept of client/server architecture and caching as discussed in class. Your task is to create a simple web and proxy server that stores and retrieves key-value pairs using socket programming interface. The server only permits commands such as GET PUT and DUMP in the request field followed by the key and value stored. GET returns the value of the key specified, PUT stores the key and a specified value on the server and DUMP lists all of the key value pairs contained in the server. When the client makes a GET request, this request is passed through the proxy server. If the server has made the same request using the same key, the key-value should be retrieved from the proxy server instead of the server. An example of how the commands are entered in the terminal are shown below: 


Screenshot showing a PUT request




Screenshot showing a DUMP request


Screenshot showing a GET request



Connecting to the Server via a Client
To establish a connection with the server:
Install  telnet . 
Ensure that your server/proxy server program is running. 
Open a terminal and connect to the client using the command  telnet <ip address> <port #>  

Code
To help you get started, we have included partial implementations to a proxy server and server. You are to complete the implementation and ensure proper functionality. The places where you need to fill in code are marked with #TODO. Each place may require one or more lines of code. 

Note: You are not mandated to use the implementation code provided and can write your own proxy server and server from scratch as needed.

What to Hand in
All code must be turned in through a version control system (e.g github). Provide a link to your repository in classroom/blackboard.

Requirement Summary
Implement GET and PUT commands on the server 
Implement the DUMP command on the server
Implement a proxy server that forwards requests from the client to the server
Implement caching that returns the value of a GET command if it has been previously requested by the client
Extra Credit: Create a time value in the cache so that values older than 60 seconds are deleted from the cache.


Additional Resources
Github
Github Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
A crash course on Github: https://www.youtube.com/watch?v=0fKg7e37bQE

Python Resource
Python Socket Tutorial
Creating a Proxy Server
