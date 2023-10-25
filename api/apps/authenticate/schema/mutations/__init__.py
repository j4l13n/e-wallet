import graphene
from .login  import Login
from .register import Register


class Mutation(graphene.ObjectType):
    login = Login.Field()
    register = Register.Field()