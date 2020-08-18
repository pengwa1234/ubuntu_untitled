from socket import *
from multiprocessing import Process
import re
import sys

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"

WSGI_TPTHON_DIR = "./wsgipython"


class HttpServer(object):
    """构造函数，application指的是框架的application"""

    def __init__(self, application):
        # 建立一个tcp socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)

        # 服务器重新链接
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.app = application()

    def start_server(self):
        # 建立监听(创建被动连接)
        self.serverSocket.listen(128)
        while True:
            # 接受客户端连接
            client_socket, dest_addr = self.serverSocket.accept()
            # print("[%s,%s]用户连接上了"%(dest_addr[0],dest_addr[1]))
            print("[%s,%s]用户连接上了" % dest_addr)

            p = Process(target=self.handle_client, args=(client_socket,))
            p.start()
            client_socket.close()

    def start_response(self, status, headers):
        """ status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    """
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.response_headers = response_headers

    def handle_client(self, client_socket):
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
        method = re.match(r"(\w+) +/[^ ]* ", request_start_line.decode("utf-8")).group(1)

        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.app(env, self.start_response)
        response = self.response_headers + "\r\n" + response_body

        # 向客户端发送响应数据
        client_socket.send(bytes(response, "utf-8"))

        # 关闭客户端连接
        client_socket.close()

    def bind(self, port):
        self.serverSocket.bind(("", port))


def main():
    sys.path.insert(1, WSGI_TPTHON_DIR)
    if len(sys.argv)<2:
        sys.exit("python3 ")
    # python MyServer.py MyWebFramework:Application
    module_name, app_name = sys.argv[1].split(":")
    # module_name="MyWebFramework"
    # app_name="Application"
    m=__import__(module_name)
    app=getattr(m,app_name)
    http_server = HttpServer(app)
    http_server.bind(8976)
    http_server.start()


if __name__ == '__main__':
    main()
