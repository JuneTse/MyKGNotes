### wikidata的所有属性

* List of properties: https://www.wikidata.org/wiki/Wikidata:List_of_properties/all_in_one_table

### 通过API获取wikidata的所有属性

* https://github.com/maxlath/wikidata-properties-dumper
* https://stackoverflow.com/questions/25100224/how-to-get-a-list-of-all-wikidata-properties
* https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#All_properties_with_descriptions_and_aliases_and_types

```SELECT ?property ?propertyLabel WHERE {
    ?property a wikibase:Property .
    SERVICE wikibase:label {
      bd:serviceParam wikibase:language "en" .
   }
 }

LIMIT 5```
