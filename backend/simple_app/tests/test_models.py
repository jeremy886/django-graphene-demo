import pytest
from model_mommy import mommy

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db


def test_message():
    obj = mommy.make('simple_app.Message')
    assert obj.pk > 0