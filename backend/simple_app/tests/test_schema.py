import pytest
from mixer.backend.django import mixer
from graphene.test import Client

from .. import schema
from backend.schema import schema as root_schema

pytestmark = pytest.mark.django_db


def test_message_type():
    instance = schema.MessageNode()
    assert instance


def test_message_node():
    instance = schema.MessageNode()
    assert instance


def test_resolve_all_messages_count():
    mixer.blend("simple_app.Message")
    mixer.blend("simple_app.Message")
    client = Client(root_schema)
    executed = client.execute(
        """
    {
        allMessages { 
            edges {
                node {
                    id
                }
            }     
        }
    }
    """
    )

    assert 2 == len(
        executed["data"]["allMessages"]["edges"]
    ), "Should return all messages"


def test_resolve_all_messages_content():
    message0 = mixer.blend("simple_app.Message")
    message1 = mixer.blend("simple_app.Message")
    client = Client(root_schema)
    executed = client.execute(
        """
    {
        allMessages { 
            edges {
                node {
                    text
                }
            }     
        }
    }
    """
    )

    assert (
        message0.text == executed["data"]["allMessages"]["edges"][0]["node"]["text"]
    ), "Should return the message"

    assert (
        message1.text == executed["data"]["allMessages"]["edges"][1]["node"]["text"]
    ), "Should return the message"