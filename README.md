# Bucket Catch Game (Client-Server Edition)
This project is a simple multiplayer "Bucket Catch" game built using Python's pygame, socket, and keyboard libraries. It was developed as a client-server application where one player controls a bucket from the client side, and the server handles the game rendering and logic.

## Game Concept
The objective of the game is to catch as many falling objects as possible using a circular "bucket" that can move in four directions using WASD keys on the client's keyboard. The player controls the bucket using the keyboard, and the game ends once any object reaches the bottom of the screen without being caught.

## How to Run
On Computer A (the game host):

```python GameServer.py```

On Computer B (the controller):

Edit gameClient.py and replace host = "10.22.48.160" with the actual IP address of the host machine running the server.

Then run:

```python gameClient.py```

Control the bucket using:

```W```: Move up

```A```: Move left

```S```: Move down

```D```: Move right

```Q```: Quit the client program

## Gameplay Rules
Falling balls appear at random x-axis positions at the top of the screen.

The bucket must catch the balls before they hit the bottom.

Each successful catch increases your score by 1.

The speed of falling balls increases with your score.

If a ball touches the bottom of the screen, it's Game Over.

You will be prompted to restart (Y) or quit (N).

## Contributors
Ethan Temple

Isha Gupta
