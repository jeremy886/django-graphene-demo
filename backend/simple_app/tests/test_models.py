import pytest
from mixer.backend.django import mixer

from simple_app import schema

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db


def test_message():
    obj = mixer.blend('simple_app.Message')
    assert obj.pk > 0


def test_message_type():
    instance = schema.MessageType()
    assert instance


def test_resolve_all_messages():
    mixer.blend('simple_app.Message')
    mixer.blend('simple_app.Message')
    q = schema.Query()
    res = q.resolve_all_messages(None)
    assert 2 == res.count(), 'Should return all messages'
