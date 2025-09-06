PINGPONG TCP/UDP PHASE 2

OVERVIEW
Multithreaded TCP and UDP client-server ping-pong system using Python sockets. Supports multiple clients simultaneously. TCP port 65432, UDP port 65433.

FILES

tcpserver.py : Multithreaded TCP server.

tcpclient.py : TCP client.

udpserver.py : Multithreaded UDP server.

udpclient.py : UDP client.

Dockerfile : Docker image.

DOCKER SETUP

Build image:
docker build -t pingpong .

Create Docker network:
docker network create pingpong-net

RUNNING TCP

Start TCP server interactively (prints PING messages directly):
docker run --rm -it --name tcpserver --network pingpong-net pingpong python tcpserver.py

Run TCP client(s):
docker run --rm --network pingpong-net pingpong python tcpclient.py

RUNNING UDP

Start UDP server interactively (prints PING messages directly):
docker run --rm -it --name udpserver --network pingpong-net pingpong python udpserver.py

Run UDP client(s):
docker run --rm --network pingpong-net pingpong python udpclient.py

RUNNING MULTIPLE CLIENTS SIMULTANEOUSLY
You can open multiple terminals or run multiple clients in the background to test multithreading:

TCP Example:
docker run --rm --network pingpong-net pingpong python tcpclient.py &
docker run --rm --network pingpong-net pingpong python tcpclient.py &

UDP Example:
docker run --rm --network pingpong-net pingpong python udpclient.py &
docker run --rm --network pingpong-net pingpong python udpclient.py &

You will see the server printing PING messages from all clients in real time.

NOTES

Start servers before clients.

Use -it to see live server output.

Clean up containers/networks if needed:
docker rm -f tcpserver udpserver
docker network rm pingpong-net