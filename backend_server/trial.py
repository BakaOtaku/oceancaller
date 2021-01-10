import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("15.207.107.146", 80))
    # s.sendall(b"GET http://15.207.107.146:80/sm/reading/ HTTP/1.1\r\nHost: 15.207.107.146:80")
    s.sendall(b"GET /?1235;05-01-2021;9876;12345678;12678; HTTP/1.1\r\nHost: 15.207.107.146\r\n\r\n")
    print(str(s.recv(4096), 'utf-8'))

    # 15.207
    # .107
    # .146 / sm / reading /

