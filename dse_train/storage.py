# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import datetime

from flask import current_app
from google.cloud import storage
import six
from werkzeug import secure_filename
from werkzeug.exceptions import BadRequest

def create_bucket(bucket_name):
    """Creates a new bucket."""
    storage_client = _get_storage_client()
    try:
        bucket = storage_client.get_bucket('dse_models')
    except NotFound:
        print('Bucket does not exist')
        bucket = storage_client.create_bucket(dse_models)
        print('Bucket {} created'.format(complete_bucket.name))

def _get_storage_client():
    return storage.Client(
        project='steady-anagram-187212')


# def _check_extension(filename, allowed_extensions):
#     if ('.' not in filename or
#             filename.split('.').pop().lower() not in allowed_extensions):
#         raise BadRequest(
#             "{0} has an invalid name or extension".format(filename))


def _safe_filename(filename):
    """
    Generates a safe filename that is unlikely to collide with existing objects
    in Google Cloud Storage.

    ``filename.ext`` is transformed into ``filename-YYYY-MM-DD-HHMMSS.ext``
    """
    filename = secure_filename(filename)
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
    basename, extension = filename.rsplit('.', 1)
    return "{0}-{1}.{2}".format(basename, date, extension)

def upload_image_file(file):
    """
    Upload the user-uploaded file to Google Cloud Storage and retrieve its
    publicly-accessible URL.
    """
    if not file:
        return None

    public_url = upload_file(file)
    #     file.read(),
    #     file.filename,
    #     file.content_type
    # )

    # current_app.logger.info(
    #     "Uploaded file %s as %s.", file.filename, public_url)

    return public_url


# [START upload_file]
def upload_file(file, filename, bucketname):

    storage_client = _get_storage_client()
    bucket = storage_client.bucket('dse_models')
    complete_filename =  bucketname + '/' + filename
    blob = bucket.blob(complete_filename)
    blob.upload_from_string(file, content_type = 'application/octet-stream')

    url = blob.public_url

    if isinstance(url, six.binary_type):
        url = url.decode('utf-8')

    return url
# [END upload_file]


def download_model(filename_url):

    storage_client = _get_storage_client()
    bucket = storage_client.bucket('dse_models')
    blob = bucket.blob('20180118_04/20180118_04_1040_7.p')
    blobd = blob.download_as_string()
    
    return blobd