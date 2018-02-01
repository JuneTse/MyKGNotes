#coding:utf-8
import requests
import json

'''
1. 启动Virtuoso服务：virtuoso-t -f
2. 使用http请求获取查询数据
    * 配置查询参数
    * 查询语句: 
        * LIMIT： 限制结果个数
        * OFFSET: 从第几个开始
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
        #'query':'select ?s ?p ?o where {?s ?p ?o .} LIMIT 100'
        }
def query_results(query):
    '''查询
    '''
    params['query']=query
    #发送请求
    r=requests.post(url,params)
    
    #结果处理
    res=json.loads(r.text)
    #keys: ['head', 'results']
    #heads=res['head']
    results=res['results']
    
    #keys: ['ordered', 'bindings', 'distinct']
    results=results['bindings']
    keys=results[0].keys()
    results=[[r[k]['value'] for k in keys] for r in results]
    return results
        
def query_triples(limit=10000,offset=0):
    '''查询，返回三元组
    '''
    query="select ?sn ?p ?on where \
                {?s ?p ?o . \
                 ?s <type.object.name> ?sn .\
                 ?o <type.object.name> ?on .\
                } LIMIT %s OFFSET %s" %(limit,offset)
    params['query']=query
    #发送请求
    r=requests.post(url,params)
    
    #结果处理
    res=json.loads(r.text)
    #keys: ['head', 'results']
    #heads=res['head']
    results=res['results']
    
    #keys: ['ordered', 'bindings', 'distinct']
    triples=results['bindings']
    
    '''
    triples是个list,里面元素格式为：
    {'o': {'type': 'uri', 'value': 'm.02pqrdr'},
     'p': {'type': 'uri', 'value': 'amusement_parks.park.rides'},
     's': {'type': 'uri', 'value': 'm.0c73k8'}}
    '''
    triples=[(t['sn']['value'],t['p']['value'],t['on']['value']) for t in triples]
    return triples
    
if __name__=="__main__":
    query="select COUNT(*) where {?s ?p ?o .}"
    count=query_results(query)[0][0]
    count=int(count)
    

    
    triples=query_triples(limit=10,offset=10)
