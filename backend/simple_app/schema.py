import graphene
from graphene_django import DjangoObjectType

from . import models


class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        interfaces = (graphene.Node, )


class Query(graphene.AbstractType):
    all_messages = graphene.List(MessageType)

    def resolve_all_messages(self, info, **kwargs):
        return models.Message.objects.all()