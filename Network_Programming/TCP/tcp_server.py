import socket


def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入手机卡（绑定本地信息）
    tcp_server_socket.bind(("", 7788))

    # 3.将手机设置为正常的响铃模式（让默认的套接字由主动变为被动 listen）
    # 监听套接字负责等待有新的客户端进行链接
    tcp_server_socket.listen(128)

    while True:
        print("等待一个客户端的到来...")
        # 4.等待别人的
        # 电话到来（等待客户端的链接 accept）
        # accept产生的新的套接字用来为客户端服务
        client_socket, client_addr = tcp_server_socket.accept()

        print("一个新的客户端已经到来%s" % str(client_addr))

        # 接收客户端发送过来的请求
        recv_data = client_socket.recv(1024)
        print("客户端发送过来的请求是：%s" % recv_data.decode("gbk"))

        # 回送一部分数据给客户端
        client_socket.send("GetIt".encode(("gbk")))

        # 关闭套接字
        # 关闭accept返回的套接字 意味着不会在位这个客户端服务
        client_socket.close()
        print("已经服务完毕")

    # 如果将监听套接字关闭了，那么会导致不能再次等待新客户端的到来，即xxx.accept就会失败
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
