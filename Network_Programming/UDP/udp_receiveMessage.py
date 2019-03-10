import socket
def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定一个本地信息,如果一个网络程序不绑定，则系统会随机分配
    localaddr = ("", 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    udp_socket.bind(localaddr)
    # 3.接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接受的最大字节数
        # recv_data这个变量中存储的是一个元组（接收到的数据，（发送方的ip, port））
        recv_msg = recv_data[0]  # 存储接收的数据
        send_addr = recv_data[1]  # 存储发送方的地址信息
        # 4.打印接收到的数据
        print("%s: %s" % (str(send_addr),recv_msg.decode('gbk')))  # 5.关闭套接字
    udp_socket.close()
if __name__ == "__main__":
    main()