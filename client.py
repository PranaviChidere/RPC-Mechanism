import socket
from student import StudentProfile
from marshalling import marshal

profile = StudentProfile("Pranavi", 101, [80,90,85])

data = marshal(profile)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

client.send(data.encode())

result = client.recv(4096).decode()
print("Server Response:", result)

client.close()
