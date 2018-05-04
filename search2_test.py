from elasticsearch import Elasticsearch
import requests
import json
from  pywords_test1 import term

#query_string = raw_input("Enter your query string: ")
print 'searching for', term
#print (WORDS)

es = Elasticsearch(['dfw-14402-0.es.objectrocket.com', 'dfw-14402-1.es.objectrocket.com', 'dfw-14402-2.es.objectrocket.com', 'dfw-14402-3.es.objectrocket.com'],
    http_auth=('paul', 'Rossme1er'),
    port=14402,
)
#    print("Connected {}".format(es.info()))
#except Exception as ex:
#    print("Error: {}".format(ex))



resp=es.search(index="documents_v3", filter_path=['hits.hits._id', 'hits.hits._source.school_name', 'took'],  body={
    "from":0,
    "size":20,
    "query": {
       "bool": {
         "must": [
           {
             "multi_match": {
               "query": term,
               "fields": [
                 "GRANK1^4.0",
                 "GRANK2^1.0",
                 "GRANK3^1.0",
                 "GRANK3A^1.0"
               ],
               "type": "most_fields",
               "operator": "OR",
               "slop": 0,
               "prefix_length": 0,
               "max_expansions": 50,
               "minimum_should_match": "70%",
               "lenient": False,
               "zero_terms_query": "NONE",
               "boost": 1
             }
           }
         ],
         "should": [
           {
             "multi_match": {
               "query": term,
               "fields": [
                 "GRANK1^4.0",
                 "GRANK2^1.0",
                 "GRANK3^1.0",
                 "GRANK3A^2.0"
               ],
               "type": "phrase",
               "operator": "OR",
               "analyzer": "phrase_analyzer",
               "slop": 16,
               "prefix_length": 0,
               "max_expansions": 50,
               "lenient": False,
               "zero_terms_query": "NONE",
               "boost": 5
             }
           }
         ],
         "disable_coord": False,
         "adjust_pure_negative": True,
         "boost": 1
       }
     },
     "_source": {
       "includes": [
         "db_filename",
         "filehash",
         "title",
         "school_name",
         "school_id",
         "dept_acro",
         "dept_id",
         "course_num",
         "course_id",
         "page_count",
         "doc_date",
         "year",
         "term",
         "resource_type"
       ],
       "excludes": [
         "content",
         "question"
       ]
     },
     "highlight": {
       "pre_tags": [
         "<b>"
       ],
       "post_tags": [
         "</b>"
       ],
       "require_field_match": False,
       "encoder": "html",
       "fields": {
         "content": {
           "fragment_size": 350,
           "number_of_fragments": 1
         }
       }
     }
    })

print(resp)
print(resp["took"])
