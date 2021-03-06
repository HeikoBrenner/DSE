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

from flask import current_app
from google.cloud import datastore
import datetime

# builtin_list = list


def init_app(app):
    pass


def get_client():
    return datastore.Client('steady-anagram-187212')


def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()

    entity['id'] = entity.key.id
    return entity


# def list(limit=10, dse_model_kind, cursor=None):
#     ds = get_client()

#     query = ds.query(kind=dse_model_kind, order=['title'])
#     query_iterator = query.fetch(limit=limit, start_cursor=cursor)
#     page = next(query_iterator.pages)

#     entities = builtin_list(map(from_datastore, page))
#     next_cursor = (
#         query_iterator.next_page_token.decode('utf-8')
#         if query_iterator.next_page_token else None)

#     return entities, next_cursor


def read(id):
    ds = get_client()
    key = ds.key('Book', int(id))
    results = ds.get(key)
    return from_datastore(results)

def query(run_id, postalcode, horizon):
    ds = get_client()
    taskname = 'dse_models' + run_id
    query = ds.query(kind=taskname)
    query.add_filter('done', '=', True)
    query.add_filter('postalcode', '=', postalcode)
    query.add_filter('horizon', '=', horizon)
    lst_models = list(query.fetch())
    serialized_model = lst_models[0]
    return serialized_model


def update(storage_blob_url, run_id, postalcode, horizon, id=None):
    ds = get_client()
    if id:
        key = ds.key('dse_models', int(id))
    else:
        key = ds.key('dse_models' + run_id )

    entity = datastore.Entity(
        key=key,
        exclude_from_indexes=['description'])

    entity.update({
        'created': datetime.datetime.utcnow(),
        'run_id': run_id,
        'postalcode': postalcode,
        'horizon': horizon,
        'model_url': storage_blob_url,
        'done': True
    })
    #entity.update(data)
    ds.put(entity)
    return from_datastore(entity)


create = update


def delete(id):
    ds = get_client()
    key = ds.key('Book', int(id))
    ds.delete(key)
