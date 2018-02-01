## 1. 使用`rdf_loader_run `

文档：[http://vos.openlinksw.com/owiki/wiki/VOS/VirtBulkRDFLoader](http://vos.openlinksw.com/owiki/wiki/VOS/VirtBulkRDFLoader )

步骤：
> * (1) 启动virtuoso服务: 进入`virtuoso.ini`所在的目录，运行: `virtuoso-t -f`命令 
> * (2) 运行`isql`命令进入SQL命令界面
> * (3)运行命令注册要加载的RDF文件： 
> > * 不包括子目录： `ld_dir ('<source-filename-or-directory>', '<file name pattern>', 'graph iri');`  
> > * 包括子目录： `ld_dir_all ('<source-filename-or-directory>', '<file name pattern>', 'graph iri');`

> * (4)检查注册的文件列表:`select * from DB.DBA.load_list;`
> * (5) 加载数据： `rdf_loader_run();`
> * (6) 在浏览器中输入网址`http://localhost:8890/sparql`, 进入SPARQL终端进行查询

**注意**：
> * RDF文件中每行是一个三元组形式的, 如果object中有空格，要用双引号括起来。
> * subject和predicate要用尖括号`<>`括起来


## 2. 使用DB.DBA.TTLP_MT命令
文档:[http://docs.openlinksw.com/virtuoso/fn_ttlp_mt/](http://docs.openlinksw.com/virtuoso/fn_ttlp_mt/])

1. 文件转换成字符串
`file_to_string_output('path')`
2. 加载Turtle、N-Triple数据
`DB.DBA.TTLP_MT`


		DB.DBA.TTLP_MT (    in strg any ,  //文件里的字符串 
		    in base varchar ,   //base IRI to resolve relative IRIs to absolute
		    in graph varchar ,  //target graph IRI, 解析的triple存放其中
		    in flags integer ,
		    in log_mode integer ,
		    in threads integer ,
		    in transactional integer );



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

例子：

	DB.DBA.TTLP_MT (file_to_string_output ('tmp/users.ttl'), '', 'http://example.com',32);
步骤：
> * (1) 启动virtuoso服务: 进入`virtuoso.ini`所在的目录，运行: `virtuoso-t -f`命令 
> * (2) 运行`isql`命令进入SQL命令界面
> * (3) 运行命令`DB.DBA.TTLP_MT (file_to_string_output ('tmp/users.ttl'), '', 'http://example.com',32);` 加载数据
> * (4) 在浏览器中输入网址`http://localhost:8890/sparql`, 进入SPARQL终端进行查询

## 3. 使用图形界面加载数据
> * (1) 启动virtuoso服务: 进入`virtuoso.ini`所在的目录，运行: `virtuoso-t -f`命令 
> * (2) 浏览器中输入： http://localhost:8890/conductor， 并登录(用户名和密码：dba)
> * (3) 点解Linked Data -->Quad Store Upload 上传文件