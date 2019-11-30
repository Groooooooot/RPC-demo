import thriftpy2 as thriftpy

pingpong_thrift = thriftpy.load("pingpong.thrift", module_name="pingpong_thrift")

from thriftpy.rpc import make_client

client = make_client(pingpong_thrift.PingPong, '127.0.0.1', 9999)
client.ping()