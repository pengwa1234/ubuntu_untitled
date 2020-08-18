from socket import *
from multiprocessing import Process

HTML_ROOT_DIR = ""

# 建立一个tcp socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# 绑定IP和端口
serverSocket.bind(("", 8881))

# 建立监听(创建被动连接)
serverSocket.listen(128)


def fun(client_socket):
    """处理客户端请求"""
    recvData = client_socket.recv(1024)
    print(recvData)
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server:My server\r\n"
    response_body = "hello itcast"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response_data:", response)

    # 向客户端发送响应数据
    client_socket.send(bytes(response, "utf-8"))

    # 关闭客户端连接
    client_socket.close()


while True:
    # 接受客户端连接
    client_socket, dest_addr = serverSocket.accept()
    # print("[%s,%s]用户连接上了"%(dest_addr[0],dest_addr[1]))
    print("[%s,%s]用户连接上了" % dest_addr)

    p = Process(target=fun, args=(client_socket,))
    p.start()
    client_socket.close()
