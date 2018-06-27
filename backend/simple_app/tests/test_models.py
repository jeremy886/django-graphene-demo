import pytest

from model_mommy import mommy

from .. import schema
# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db


def test_message():
    obj = mommy.make('simple_app.Message')
    assert obj.pk > 0


def test_message_type():
    instance = schema.MessageType()
    assert instance


def test_resolve_all_messages():
    mommy.make('simple_app.Message')
    mommy.make('simple_app.Message')
    q = schema.Query()
    res = q.resolve_all_messages(None)
    assert 2 == res.count(), 'Should return all messages'