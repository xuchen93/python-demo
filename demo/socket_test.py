import socket
import json


def main():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = 'localhost'
	port = 5000
	server_socket.bind((host, port))
	# 设置最大连接数，超过后排队
	server_socket.listen(1)
	print(host)
	print(port)
	print("服务器启动成功，等待连接...")
	client_socket, addr = server_socket.accept()
	print("从", str(addr), "收到连接")
	while True:
		data = input()
		print(data)
		client_socket.sendall(data.encode('utf-8'))
		if 'bye' == data:
			client_socket.close()


if __name__ == '__main__':
	main()
