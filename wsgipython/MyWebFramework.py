import time
from MyServer import HttpServer

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"


class Application(object):
    """框架的核心部分，也就是框架的主体框架，框架是通用的"""

    def __init__(self, urls):
        # 设置路由信息
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        # /static/index.html
        if path.startwith("/static"):
        # 要访问静态文件
            file_name = path[7:]
        try:
            file = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            # 代表未找到路由信息，404错误
            status = "404 Not Found"
            headers = []
            start_response("404 Not Found")
            return "not found"
        else:
            file_data = file.read()
            file.close()

            status = "200 OK"
            headers = []
            start_response(status, headers)
            return file_data.decode("utf-8")

        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)


def show_ctime(env, start_response):
    urls = [
        ("/", show_ctime),
        ("/ctime", show_ctime),
        ("/sayhello", say_hello)
    ]

    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]

    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    urls = [
        ("/ctime", show_ctime),
        ("/sayhello", say_hello)
    ]

    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]

    start_response(status, headers)
    return time.ctime()


if __name__ == '__main__':
    urls = [
        ("/ctime", show_ctime),
        ("/sayhello", say_hello)
    ]

    app = Application(urls)
    http_server = HttpServer(app)
    http_server.bind(8000)
    http_server.start()
