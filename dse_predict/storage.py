# from __future__ import absolute_import

from flask import current_app
from google.cloud import storage
# import six
# from werkzeug import secure_filename
# from werkzeug.exceptions import BadRequest


def _get_storage_client():
    return storage.Client(
        project='steady-anagram-187212')


def download_model(filename_url):

    storage_client = _get_storage_client()
    bucket = storage_client.bucket('dse_models')
    blob = bucket.blob('20180118_04/20180118_04_1040_7.p')
    blob_string = blob.download_as_string()
    
    return blob_string