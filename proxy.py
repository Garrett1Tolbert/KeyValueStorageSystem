"""A proxy server that forwards requests from one port to another server.

To run this using Python 2.7:

% python proxy.py

It listens on a port (`LISTENING_PORT`, below) and forwards commands to the
server. The server is at `SERVER_ADDRESS`:`SERVER_PORT` below.
"""

# This code uses Python 2.7. These imports make the 2.7 code feel a lot closer
# to Python 3. (They're also good changes to the language!)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import library
import socket
import time

# Where to find the server. This assumes it's running on the smae machine
# as the proxy, but on a different port.
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 7777

# The port that the proxy server is going to occupy. This could be the same
# as SERVER_PORT, but then you couldn't run the proxy and the server on the
# same machine.
LISTENING_PORT = 8888

# Cache values retrieved from the server for this long.
MAX_CACHE_AGE_SEC = 60.0  # 1 minute


def ForwardCommandToServer(command, server_addr, server_port):
# Opens a TCP socket to the server, sends a command, and returns response.
#
# Args:
# command: A single line string command with no newlines in it.
# server_addr: A string with the name of the server to forward requests to.
# server_port: An int from 0 to 2^16 with the port the server is listening on.
# Returns:
# A single line string response with no newlines.


    ###################################################
    #TODO: Implement Function: WiP
    ###################################################
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_addr, server_port))
    s.sendall(command)
    data = s.recv(256)

    return data


def CheckCachedResponse(command_line, cache):
    cmd, name, text = library.ParseCommand(command_line)

    # Update the cache for PUT commands but also pass the traffic to the server.
    ##########################
    #TODO: Implement section
    ##########################
    # if cmd == "PUT":
    #     cache.StoreValue(name,text)

    # GET commands can be cached.
    ############################
    #TODO: Implement section
    ############################

    if cmd == "GET":
        # return None
        # print("Checking cache for GET command")
        #
        if name in cache.datastore:
            print("Name is in cache")
            return cache.GetValue(name,MAX_CACHE_AGE_SEC)
        else:
            print("Name is NOT in cache")
            return None

    # return None

def ProxyClientCommand(sock, server_addr, server_port, cache):
# """Receives a command from a client and forwards it to a server:port.
#
# A single command is read from `sock`. That command is passed to the specified
# `server`:`port`. The response from the server is then passed back through
# `sock`.
#
# Args:
# sock: A TCP socket that connects to the client.
# server_addr: A string with the name of the server to forward requests to.
# server_port: An int from 0 to 2^16 with the port the server is listening on.
# cache: A KeyValueStore object that maintains a temorary cache.
# max_age_in_sec: float. Cached values older than this are re-retrieved from
#   the server.
# """

    ###########################################
    #TODO: Implement ProxyClientCommand
    ###########################################
    command = ""
    data = ""
    while not command or command[-1] != '\n':
        command += sock.recv(256)


    # check to see if command is in proxy cache
    # if it is, isCache will return None or a command(data)
    isCache = CheckCachedResponse(command,cache)
    print(isCache)
    # if true(when isCache is None), it will get data from server and send it
    if isCache is None:
        cmd, name, text = library.ParseCommand(command)
        print("isCache is None...Looking to server")
        data = ForwardCommandToServer(command,server_addr,server_port)
        if cmd == "GET":
            cache.datastore[name] = (data,time.time())
    sock.sendall(data)
    #
    #     # parse data from server to get key/value
    #     cmd, name, text = library.ParseCommand(data)
    #     # update cache with data from server
    #     cache.StoreValue(name, text)
    # else:
    #     print("Found value in cache...")
    #     sock.sendall(isCache)

    # close the client socket
    sock.close()

def main():
    # Listen on a specified port...
    server_sock = library.CreateServerSocket(LISTENING_PORT)
    cache = library.KeyValueStore()
    # Accept incoming commands indefinitely.
    while True:
        # Wait until a client connects and then get a socket that connects to the
        # client.
        client_sock, (address, port) = library.ConnectClientToServer(server_sock)
        print('TEST:Received connection from %s:%d' % (address, port))
        ProxyClientCommand(client_sock, SERVER_ADDRESS, SERVER_PORT,
                           cache)

    #################################
    #TODO: Close socket's connection
    #################################
    server_sock.close()

main()
