## wikidata实体


### 查询所有实体

* 查询实体的某个属性：https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#All_items_with_a_property
```
# Sample to query all values of a property
# Property talk pages on Wikidata include basic queries adapted to each property
SELECT
  ?item ?itemLabel
  ?value ?valueLabel
# valueLabel is only useful for properties with item-datatype
WHERE 
{
  ?item wdt:P1800 ?value
  # change P1800 to another property        
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
# remove or change limit for more results
LIMIT 10
```

* 查询实体和其对应的wikipedia文章：https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Wikidata_items_of_Wikipedia_articles
```
#Returns a list of Wikidata items for a given list of Wikipedia article names
#List of Wikipedia article names (lemma) is like "WIKIPEDIA ARTICLE NAME"@LANGUAGE CODE with de for German, en for English, etc.
#Language version and project is defined in schema:isPartOF with de.wikipedia.org for German Wikipedia, es.wikivoyage for Spanish Wikivoyage, etc.

SELECT ?lemma ?item WHERE {
  VALUES ?lemma {
    "Wikipedia"@de
    "Wikidata"@de
    "Berlin"@de
    "Technische Universität Berlin"@de
  }
  ?sitelink schema:about ?item;
    schema:isPartOf <https://de.wikipedia.org/>;
    schema:name ?lemma.
}
```
