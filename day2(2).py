'''
为了请求特定数据，我们需要在URL的查询字符串中加入某些数据。如果你是自己构建URL，那么数据一般会跟在一个问号后面
,并以键值的形式储存在URL当中。如 http://httpbin.org/get?key1=value1
'''
import requests
key_dict={'key1':'value1','key2':'value2'}
r=requests.get('http://httpbin.org/get',params=key_dict)
print(r.url)
print(r.text)
'''
    运行结果
{
  "args": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "origin": "124.76.90.178", 
  "url": "http://httpbin.org/get?key1=value1&key2=value2"
}
'''