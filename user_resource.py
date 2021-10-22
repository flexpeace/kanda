
import json
from pprint import pprint

import falcon
from marshmallow import ValidationError
from schema import UserSchema


try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict


class BaseResource(object):
    def success(self, resp, data=None):
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({})
        resp.content_type = falcon.MEDIA_JSON

    def error(self, resp, data=None):
        resp.status = falcon.HTTP_400
        obj = OrderedDict()
        obj['field_errors'] = data
        obj['error'] = 'Bad Requests'
        resp.body = json.dumps(obj)
        resp.content_type = falcon.MEDIA_JSON


class UserResource(BaseResource):

    def on_post(self, req, resp, **kwargs):
        try:
            data = json.load(req.bounded_stream)
        except json.decoder.JSONDecodeError:
            return self.error(resp, 'Bad input, must be valid json.')

        try:
            result = UserSchema().load(data)
        except ValidationError as err:
            return self.error(resp, err.messages)
        return self.success(resp, {})
