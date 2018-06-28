import graphene
from graphene_django import DjangoObjectType

from . import models


class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message


class Query:
    all_messages = graphene.List(MessageType)
    message = graphene.Field(
        MessageType,
        id=graphene.Int(),
        text=graphene.String(),
        created_at=graphene.DateTime(),
    )

    def resolve_all_messages(selfself, info, **kwargs):
        return models.Message.objects.all()

    def resolve_message(self, info, **kwargs):
        id = kwargs.get("id")
        text = kwargs.get("text")
        created_at = kwargs.get("created_at")

        if id is not None:
            return models.Message.objects.get(pk=id)

        if text is not None:
            return models.Message.objects.get(text=text)

        if created_at is not None:
            return models.Message.objects.get(created_at=created_at)
