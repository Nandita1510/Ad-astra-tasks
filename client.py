import socket, cv2, pickle, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))

def recv_exact(sock, n):
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError
        buf.extend(chunk)
    return bytes(buf)

while True:
    msg_len = struct.unpack('>I', recv_exact(s, 4))[0]
    frame = pickle.loads(recv_exact(s, msg_len))
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
