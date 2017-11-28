import requests
r=requests.get('http://www.santostang.com/')
print("文本编码：",r.encoding)
print("相应状态码：",r.status_code)
print("字符串方式的响应体：",r.text)
'''
运行结果：
文本编码： UTF-8
相应状态码： 200   --->200为响应正常 400为异常情况
字符串方式的响应体： <!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>大数据分析@唐松</title>
<meta name="description" content="唐松的个人博客，分享大数据分析和 Python 网络爬虫的思考。" />
<meta name="keywords" content="唐松, Santos, 博客" />
'''
