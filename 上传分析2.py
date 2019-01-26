UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
文件名
文件大小
X-Upos-Auth = 返回1:auth = "os=upos&cdn=upcdnws&uid=14009112&net_state=4&device=&build=&os_version=&ak=1494471752&timestamp=1548162120&sign=c27a2457f3303b08746e215058e6eca9"
biz_id = 返回1:biz_id = 72742744
chunk_size = 返回1:chunk_size = 4194304#分块大小
endpoint: 返回1:endpoint = "//upos-sz-upcdnws.acgvideo.com"#上传地址1
threads: 返回1:threads = 2#上传线程数
upos_uri: 返回1:upos_uri = "upos://ugc/m190122wscdly8hkx1nrc225u45pnss2.flv"#上传地址2
上传地址 = "https:"+endpoint+"/"+upos_uri[6:]
key = 返回2:key = "/m190122wscdly8hkx1nrc225u45pnss2.flv"#文件名
upload_id = 返回2:upload_id = "c53aa79cfcd89175c3efcd18bbd4cab7"



get https://member.bilibili.com/video/upload.html
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8
Connection: keep-alive
Cookie: [cookie]
DNT: 1
Host: member.bilibili.com
Upgrade-Insecure-Requests: 1
User-Agent: [UA]



get https://member.bilibili.com/preupload?name=[文件名]&size=[文件大小]&r=upos&profile=ugcupos%2Fbup&ssl=0&os=upos&upcdn=ws&version=2.4.2
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8
Connection: keep-alive
Cookie: [cookie]
DNT: 1
Host: member.bilibili.com
Referer: https://member.bilibili.com/video/upload.html
User-Agent: [UA]


返回1
OK: 1
auth: "os=upos&cdn=upcdnws&uid=14009112&net_state=4&device=&build=&os_version=&ak=1494471752&timestamp=1548162120&sign=c27a2457f3303b08746e215058e6eca9"
biz_id: 72742744
chunk_retry: 200
chunk_retry_delay: 3
chunk_size: 4194304
endpoint: "//upos-sz-upcdnws.acgvideo.com"
endpoints: ["//upos-sz-upcdnws.acgvideo.com", "//upos-sz-upcdnws.acgvideo.com"]
0: "//upos-sz-upcdnws.acgvideo.com"
1: "//upos-sz-upcdnws.acgvideo.com"
threads: 2
timeout: 900
uip: "121.69.87.246"
upos_uri: "upos://ugc/m190122wscdly8hkx1nrc225u45pnss2.flv"



options [上传地址]?uploads&output=json
Access-Control-Request-Headers: x-upos-auth
Access-Control-Request-Method: POST
DNT: 1
Origin: https://member.bilibili.com
User-Agent: [UA]



post [上传地址]?uploads&output=json
DNT: 1
Origin: https://member.bilibili.com
Referer: https://member.bilibili.com/video/upload.html
User-Agent: [UA]
X-Upos-Auth: [X-Upos-Auth]

返回2
OK: 1
bucket: "ugc"
key: "/m190122wscdly8hkx1nrc225u45pnss2.flv"
upload_id: "c53aa79cfcd89175c3efcd18bbd4cab7"



options [上传地址]?partNumber=[1,2...]&uploadId=[upload_id]&chunk=[partNumber-1]&chunks=[math.ceil(文件大小/chunk_size)]&size=4194304&start=[0,4194304...]&end=[4194304,8388608...]&total=[文件大小]

Access-Control-Request-Headers: x-upos-auth
Access-Control-Request-Method: PUT
DNT: 1
Origin: https://member.bilibili.com
User-Agent: [UA]



put [上传地址]?partNumber=[1,2...]&uploadId=[upload_id]&chunk=[partNumber-1]&chunks=[math.ceil(文件大小/chunk_size)]&size=4194304&start=[0,4194304...]&end=[4194304,8388608...]&total=[文件大小]

上传数据二进制

DNT: 1
Origin: https://member.bilibili.com
Referer: https://member.bilibili.com/video/upload.html
User-Agent: [UA]
X-Upos-Auth: [X-Upos-Auth]



options [上传地址]?output=json&name=[文件名]&profile=ugcupos%2Fbup&uploadId=[upload_id]&biz_id=[biz_id]
Access-Control-Request-Headers: content-type,x-upos-auth
Access-Control-Request-Method: POST
DNT: 1
Origin: https://member.bilibili.com
User-Agent: [UA]



post [上传地址]?output=json&name=[文件名]&profile=ugcupos%2Fbup&uploadId=[upload_id]&biz_id=[biz_id]
Content-Type: application/json; charset=UTF-8
DNT: 1
Origin: https://member.bilibili.com
Referer: https://member.bilibili.com/video/upload.html
User-Agent: [UA]
X-Upos-Auth: [X-Upos-Auth]

data
s = json.dumps({'key1': 'value1', 'key2': 'value2'})
{"parts":[{"partNumber":4,"eTag":"etag"},{"partNumber":5,"eTag":"etag"},{"partNumber":1,"eTag":"etag"},{"partNumber":2,"eTag":"etag"},{"partNumber":3,"eTag":"etag"}]}#options请求顺序(891234567,threads=2)

返回3
OK: 1
bucket: "ugc"
etag: "17956877"
key: "/m190122wscdly8hkx1nrc225u45pnss2.flv"
location: "ugc/m190122wscdly8hkx1nrc225u45pnss2.flv"



get https://member.bilibili.com/x/geetest/pre/add
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8
Connection: keep-alive
Cookie: [cookie]
DNT: 1
Host: member.bilibili.com
Referer: https://member.bilibili.com/video/upload.html
User-Agent: [UA]



post https://member.bilibili.com/x/vu/web/add?csrf=[bili_jct in cookie]
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8
Connection: keep-alive
Content-Length: 432###############
Content-Type: application/json;charset=UTF-8
Cookie: [cookie]
DNT: 1
Host: member.bilibili.com
Origin: https://member.bilibili.com
Referer: https://member.bilibili.com/video/upload.html
User-Agent: [UA]

data
s = json.dumps({'key1': 'value1', 'key2': 'value2'})
{"copyright":2,"videos":[{"filename":"key[1:4]","title":"文件名[:4]","desc":""}],"source":"https://live.bilibili.com/104","tid":173,"cover":"","title":"【live/104】毛毛的雀魂","tag":"雀魂","desc_format_id":42,"desc":"测试。这里是简介","dynamic":"#雀魂#","subtitle":{"open":0,"lan":""}}
copyright: 2#转载
cover: "//upos-videocovers.acgvideo.com/m190122wscdly8hkx1nrc225u45pnss2_0001.jpg"#封面
desc: "测试。这里是简介"#简介
desc_format_id: 38#未知，数据来自推荐标签
dtime: 1548874260#定时发布
dynamic: "#雀魂##dota#"#动态
porder: {flow_id: 1, industry_id: 1, official: 0, show_type: ""}#商业声明
source: "https://live.bilibili.com/104"#转载来源
subtitle: {open: 0, lan: "zh-CN"}#更多选项
lan: "zh-CN"#字幕语言
open: 0#观众投字幕，0=F，1=T
tag: "dota"#标签
tid: 171#分区
title: "【live/104】毛毛打dota"#标题
videos: [{filename: "m190122wscdly8hkx1nrc225u45pnss2", title: "20180816_115821", desc: ""}]
0: {filename: "m190122wscdly8hkx1nrc225u45pnss2", title: "20180816_115821", desc: ""}#分p
desc: ""#未知
filename: "m190122wscdly8hkx1nrc225u45pnss2"#视频文件名
title: "20180816_115821"#分p标题

tid: 171	desc_format_id: 38	游戏>电子竞技
tid: 173	desc_format_id: 42	游戏>桌游棋牌
tid: 65	desc_format_id: 33	游戏>网络游戏

返回4
code: 0
data: {aid: 41428660}
aid: 41428660
message: "0"
ttl: 1



import requests
import json

headers = {'content-type': 'application/json'}
url = 'http://192.168.3.45:8080/api/v2/event/log'

data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

requests.post(url, params=params, data=json.dumps(data), headers=headers)