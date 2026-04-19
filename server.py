import socket, cv2, pickle, struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("Waiting...")
conn, addr = server.accept()
print("Connected!")
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    data = pickle.dumps(frame)
    conn.sendall(struct.pack('>I', len(data)) + data)
