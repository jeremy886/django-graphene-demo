from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from . import models


class MessageNode(DjangoObjectType):
    class Meta:
        model = models.Message
        filter_fields = {
            "text": ["exact", "icontains", "istartswith"],
            "created_at": ["exact"],
        }
        interfaces = (relay.Node,)


class Query:
    message = relay.Node.Field(MessageNode)
    all_messages = DjangoFilterConnectionField(MessageNode)
