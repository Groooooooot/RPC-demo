import thriftpy2 as thriftpy

pingpong_thrift = thriftpy.load("pingpong.thrift", module_name="pingpong_thrift")

from thriftpy.rpc import make_server

# 用于分发任务
class Dispatcher(object):
    def ping(self):
        print('Pong')
        return 'pong'

server = make_server(pingpong_thrift.PingPong, Dispatcher(), '127.0.0.1', 9999)
print('Start serving.')
server.serve()