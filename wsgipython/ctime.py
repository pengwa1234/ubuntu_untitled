import time


def application(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    # 处理status和headers
    start_response(status, headers)
    return time.ctime()
