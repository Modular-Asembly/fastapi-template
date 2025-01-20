from google.cloud import tasks_v2


_client = None


def get_gcp_tasks_client() -> tasks_v2.CloudTasksClient:
    global _client
    if _client is None:
        _client = tasks_v2.CloudTasksClient()
    return _client
