import socket
from _thread import *
import sys


class Network:

  def __init__(self):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = "134.87.144.102"
    self.port = 5555
    self.addr = (self.server, self.port)
    self.id = self.connect()
    print(self.id)

  def connect(self):
    try:
      self.client.connect(self.addr)
      return self.client.recv(2048).decode()
    except:
      pass

  def send(self, data):
    try:
      self.client.send(str.encode(data))
      return self.client.recv(2048).decode()
    except socket.error as e:
      print(e)


server = "134.87.144.102"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((server, port))
except socket.error as e:
  str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn):
  conn.send(str.encode("Connected"))
  reply = ""
  while True:
    try:
      data = read_pos(conn.recv(2048).decode())
      reply = data
      if not data:
        print("Disconnected")
        break
      else:
        print("Received: ", reply)
        print("Sending : ", reply)
      conn.sendall(str.encode("hello"))
    except:
      break

  print("Lost connection")
  conn.close()


def read_pos(str):
  str = str.split(",")
  return int(str[0]), int(str[1])


while True:
  conn, addr = s.accept()
  print("Connected to:", addr)

  start_new_thread(threaded_client, (conn, ))
  n = Network()
  print(n.send("hello"))
  print(n.send("working"))
