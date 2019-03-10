import socket
def main():
    # 创建一个udp套接字，套接字是一个可以同时收发数据的
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # localaddr = ("", 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    # udp_socket.bind(localaddr)
    # 获取对方的IP/port
    dest_ip = input("请输入对方的ip：")
    dest_port= int(input("请输入对方的port："))

    # 从键盘获取数据
    send_data = input("请输入要发送的数据：")

    # 可以使用套接字收发数据
    # udp_socket.sendto("发送内容"， 对方的ip以及port)
    # udp_socket.sendto("hahahahah", ("10.180.144.106", 8080))
    udp_socket.sendto(send_data.encode('gbk'),(dest_ip,dest_port))

    # 接收回送过来的数据
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)

    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()