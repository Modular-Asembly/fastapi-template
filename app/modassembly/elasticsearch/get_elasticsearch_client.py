import os

from elasticsearch import Elasticsearch


ES_HOSTS = os.getenv("ELASTICSEARCH_HOSTS", "localhost:9200")
ES_USERNAME = os.getenv("ELASTICSEARCH_USERNAME")
ES_PASSWORD = os.getenv("ELASTICSEARCH_PASSWORD")
ES_VERIFY_CERTS = os.getenv("ELASTICSEARCH_VERIFY_CERTS", "true").lower() == "true"


_client = None


def get_elasticsearch_client() -> Elasticsearch:
    global _client
    if _client is None:
        auth = None
        if ES_USERNAME and ES_PASSWORD:
            auth = (ES_USERNAME, ES_PASSWORD)
        _client = Elasticsearch(
            hosts=ES_HOSTS, basic_auth=auth, verify_certs=ES_VERIFY_CERTS
        )
    return _client
