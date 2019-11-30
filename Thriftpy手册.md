# Thriftpy手册

#### Thriftpy服务器创建

- 调用thriftpy.load方法对thrift文件进行解析，并在内存中构建相应的module
- 使用make_server将上一步构建的module和完成具体业务功能的class绑定，同时完成传输层和协议层的设置，生成thrift服务器端
- 调用server.serve启动服务器

```python
# -*- coding: utf-8 -*-
import time
import thriftpy
from thriftpy.rpc import make_server

# 根据sleep.thrift文件，在内存中动态构建一个名为"sleep_thriftpy"的module
# 该module中包含了名为Sleep的一个object
sleep_thrift = thriftpy.load("sleep.thrift", module_name="sleep_thrift")

# 官方代码中该Class名称为Dispatcher
# 修改为Sleep只是为了方便读者和sleep.thrift文件中的Sleep服务相对应
class Sleep(object):
    # 该方法对应sleep.thrift文件中的oneway void sleep(1: i32 seconds)
    def sleep(self, seconds):
        print("I'm going to sleep %d seconds" % seconds)
        time.sleep(seconds)
        print("Sleep over!")

def main():
    # 创建一个服务，在127.0.0.1的6000端口进行监听
    # 将class Sleep和module sleep_thrift中名为Sleep的Object绑定
    server = make_server(sleep_thrift.Sleep, Sleep(),
                         '127.0.0.1', 6000)
    print("serving...")
    # 启动服务
    server.serve()

if __name__ == '__main__':
    main()
```

#### Thriftpy客户端创建

- 调用thriftpy.load方法对thrift文件进行解析，在内存中构建对应的module
- 根据上一步结果，叫用make_client绑定上一步构建的module，并完成传输层与协议层设置，生成Thrift客户端
- 根据上一步的客户端调用响应接口

```python
# -*- coding: utf-8 -*-
import thriftpy
from thriftpy.rpc import make_client

# 根据sleep.thrift文件，动态生成一个名为"sleep_thriftpy"的module
# 该module中包含了名为Sleep的一个object
sleep_thrift = thriftpy.load("sleep.thrift", module_name="sleep_thrift")

def main():
    # 创建一个客户端，该客户端连接127.0.0.1的6000端口
    # 并将该客户端和服务器端的Sleep服务进行绑定
    client = make_client(sleep_thrift.Sleep, '127.0.0.1', 6000)
    # 绑定完成后即可直接调用服务器端相应的方法
    client.sleep(1)

if __name__ == '__main__':
    main()
```

