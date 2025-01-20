import os

from google.cloud import tasks_v2

from app.modassembly.tasks.get_gcp_tasks_client import get_gcp_tasks_client


GCP_PROJECT = os.environ["GCP_PROJECT"]
GCP_LOCATION = os.environ["GCP_LOCATION"]
GCP_QUEUE = os.environ["GCP_QUEUE"]


def get_gcp_tasks_queue() -> tasks_v2.Queue:
    client = get_gcp_tasks_client()
    return client.queue_path(GCP_PROJECT, GCP_LOCATION, GCP_QUEUE)
