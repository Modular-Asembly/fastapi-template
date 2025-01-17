from google.cloud import scheduler_v1


_client = None


def get_gcs_scheduler_client() -> scheduler_v1.CloudSchedulerClient:
    global _client
    if _client is None:
        _client = scheduler_v1.CloudSchedulerClient()
    return _client
