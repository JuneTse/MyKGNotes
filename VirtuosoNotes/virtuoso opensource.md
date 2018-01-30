## Virtuoso opensource

1. virtuoso介绍:https://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VOSRDF 
2. 下载：[https://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VOSDownload][1]
3. 启动服务：在有virtuoso.ini的目录下，运行命令：virtuoso-t -f
4. 查看WebUI: http://localhost:8890/sqarql
5. 配置virtuoso.ini: 
当数据集很大时，要配置virtuoso使用的系统内存，使用总内存的2/3到3/5之间
	* NumberOfBuffers     
	* MaxDirtyBuffers      
6. 


## 处理Freebase
1. [Virtuoso Freebase Setup: https://github.com/sameersingh/nlp_serde/wiki/Virtuoso-Freebase-Setup][2]
2. Load Freebase Dump into Virtuoso (SPARQL database): [http://sivareddy.in/load-freebase-dump-into-virtuoso-sparql-sql][3]
3. [https://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VirtBulkRDFLoader][4]
4. overflowstack:Freebase - how to use the freebase-rdf-latest?: [http://stackoverflow.com/questions/28285043/freebase-how-to-use-the-freebase-rdf-latest][5]
5. freebase2rdf:[https://github.com/castagna/freebase2rdf][6]

[1]: https://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VOSDownload
[2]: https://github.com/sameersingh/nlp_serde/wiki/Virtuoso-Freebase-Setup
[3]: http://sivareddy.in/load-freebase-dump-into-virtuoso-sparql-sql
[4]: https://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VirtBulkRDFLoader
[5]: http://stackoverflow.com/questions/28285043/freebase-how-to-use-the-freebase-rdf-latest
[6]: https://github.com/castagna/freebase2rdf