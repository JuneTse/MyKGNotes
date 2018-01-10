文档:http://docs.openlinksw.com/virtuoso/fn_ttlp_mt/

1. 文件转换成字符串
`file_to_string_output('path')`
2. 加载Turtle、N-Triple数据
`DB.DBA.TTLP_MT`
```
DB.DBA.TTLP_MT (    in strg any ,  //文件里的字符串
    in base varchar ,   //base IRI to resolve relative IRIs to absolute
    in graph varchar ,  //target graph IRI, 解析的triple存放其中
    in flags integer ,
    in log_mode integer ,
    in threads integer ,
    in transactional integer );
```
```
flags:

  1 - Single quoted and double quoted strings may with newlines.
  2 - Allows bnode predicates (but SPARQL processor may ignore them!).
  4 - Allows variables, but triples with variables are ignored.
  8 - Allows literal subjects, but triples with them are ignored.
 16 - Allows '/', '#', '%' and '+' in local part of QName ("Qname with path")
 32 - Allows invalid symbols between '<' and '>', i.e. in relative IRIs.允许无效符号。
 64 - Relax TURTLE syntax to include popular violations.
128 - Try to recover from lexical errors as much as it is possible.
256 - Allows TriG syntax, thus loading data in more than one graph.
512 - Allows loading N-quad dataset files with and optional context value to indicate provenance as detailed
<ulink url="http://sw.deri.org/2008/07/n-quads/">here</ulink>.
```
例子：
DB.DBA.TTLP_MT (file_to_string_output ('tmp/users.ttl'), '', 'http://example.com',32);
3. 