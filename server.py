import socket
from marshalling import unmarshal

def calculate_grade_average(profile):
    return sum(profile.grades) / len(profile.grades)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)
print("Server is listening...")

conn, addr = server.accept()
print("Connected to", addr)

data = conn.recv(4096).decode()

try:
    profile = unmarshal(data)
    result = calculate_grade_average(profile)
    conn.send(str(result).encode())
except TypeError as e:
    conn.send(f"Error: {str(e)}".encode())

conn.close()
