from socket import *
from multiprocessing import Process
import re

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"


class HttpServer(object):
    def __init__(self):
        # 建立一个tcp socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)

        # 服务器重新链接
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def start_server(self):
        # 建立监听(创建被动连接)
        self.serverSocket.listen(128)
        while True:
            # 接受客户端连接
            client_socket,dest_addr = self.serverSocket.accept()
            # print("[%s,%s]用户连接上了"%(dest_addr[0],dest_addr[1]))
            print("[%s,%s]用户连接上了" % dest_addr)

            p = Process(target=self.fun, args=(client_socket,))
            p.start()
            client_socket.close()

    def fun(self, client_socket):
        """处理客户端请求"""
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print(request_data)

        # splitlines按照行来分割
        request_lines = request_data.splitlines()
        for reques_line in request_lines:
            print(reques_line)

        # 获取起始行 ‘GET / HTTP/1.1'  解析请求报文
        request_start_line = request_lines[0]
        # 提取用户请求名
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        if '/' == file_name:
            file_name = "/index.html"

        print("123:", request_start_line)
        # 打开文件，读取内容
        try:
            file = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server:My server\r\n"
            response_body = "The file is not found!"
        else:
            file_data = file.read()
            file.close()

            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server:My server\r\n"
            response_body = file_data.decode("utf-8")

        response = response_start_line + response_headers + "\r\n" + response_body
        print("response_data:", response)

        # 向客户端发送响应数据
        client_socket.send(bytes(response, "utf-8"))

        # 关闭客户端连接
        client_socket.close()

    def bind(self,port):
        self.serverSocket.bind(("", port))


def main():
    http_server = HttpServer()
    http_server.bind(8989)
    http_server.start_server()

if __name__ == '__main__':
    main()
