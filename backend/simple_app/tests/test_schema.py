import pytest
from mixer.backend.django import mixer
# from graphql_relay.node.node import to_global_id

from .. import schema


pytestmark = pytest.mark.django_db


def test_message_type():
    instance = schema.MessageType()
    assert instance


def test_resolve_all_messages():
    mixer.blend('simple_app.Message')
    mixer.blend('simple_app.Message')
    q = schema.Query()
    res = q.resolve_all_messages(None)
    assert res.count() == 2, 'Should return all messages'



# def test_resolve_message():
#     msg = mixer.blend('simple_app.Message')
#     q = schema.Query()
#     id = to_global_id('MessageType', msg.pk)
#     res = q.resolve_message(None, id=id)
#     assert res == msg, 'Should return the requested message'