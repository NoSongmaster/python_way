#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import socketserver
#BaseRequestHandler 处理通讯
class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):   #必须实现handle方法，负责与客户端通讯
        print(self.request)
        print(self.client_address)
        while True:
            try:
                data=self.request.recv(1024)
                self.request.send(data.upper())
            except Exception:
                break


if __name__ == '__main__':
    #ThreadingTCPServer 处理链接
    s=socketserver.ThreadingTCPServer(('127.0.0.1',8080),FtpServer)
    s.serve_forever()       #链接循环--有了




