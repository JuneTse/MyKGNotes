#coding:utf-8
import requests
import json

'''
1. 启动Virtuoso服务：virtuoso-t -f
2. 使用http请求获取查询数据
    * 配置查询参数
    * 查询语句
    * url
3. 处理查询结果
'''

url='http://localhost:8890/sparql'

#查询参数配置
params={'default-graph-uri':'http://fb2m.com',
#        'format':'text/html',
        'format':'json', #返回结果类型为json
        'timeout':0,
        'debug':'on',
        'query':'select ?s ?p ?o where {?s ?p ?o .} LIMIT 100'
        }
#发送请求
r=requests.post(url,params)

#结果处理
res=json.loads(r.text)
#keys: ['head', 'results']
heads=res['head']
results=res['results']

#keys: ['ordered', 'bindings', 'distinct']
triples=results['bindings']

'''
triples是个list,里面元素格式为：
{'o': {'type': 'uri', 'value': 'm.02pqrdr'},
 'p': {'type': 'uri', 'value': 'amusement_parks.park.rides'},
 's': {'type': 'uri', 'value': 'm.0c73k8'}}
'''
triples=[(t['s']['value'],t['p']['value'],t['o']['value']) for t in triples]
print(triples)