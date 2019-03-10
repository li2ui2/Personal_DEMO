import socket


def main():
    # 1.创建tcp的套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.链接服务器
    #t cp_client_socket.connect(("10.180.144.106",8080))
    server_ip = input("请输入要链接的服务器的ip：")
    server_port = input("请输入要链接的服务器的port：")
    server_addr = (server_ip, int(server_port))
    tcp_client_socket.connect(server_addr)
    # 3.发送数据/接收数据
    send_data = input("请输入要发送的数据：")
    tcp_client_socket.send(send_data.encode("gbk"))
    # 4.关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
