
The proposed template can be applied to an existing cluster using the below curl command.

```shell
curl -s -H 'Content-Type: application/json' -XPUT 'http://elasticsearch:9200/_template/products-v2?pretty' -d @./products-index-template.json
```


<details><summary>Testing the Mapping can be achieving like so</summary>
<p>
  
```JSON
POST products-v2/_analyze
{
  "field": "title.simpleWord",
  "text": " Candioli Bolo 40g"
}
```

