import graphene
from graphene_django_extras import DjangoListObjectType, \
    DjangoObjectType, LimitOffsetGraphqlPagination, \
    DjangoInputObjectType
from ...models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ['password']
        description = " Type definition for a single user "
        filter_fields = {
            "id": ("exact", ),
            "first_name": ("icontains", "iexact"),
            "last_name": ("icontains", "iexact"),
            "username": ("icontains", "iexact"),
            "email": ("icontains", "iexact"),
            "is_staff": ("exact", ),
        }

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset


class UserInputType(DjangoInputObjectType):
    class Meta:
        model = User
        description = " User Input type "


class UserListType(DjangoListObjectType):
    class Meta:
        model = User
        description = " Type definition for a single user "
        pagination = LimitOffsetGraphqlPagination(
            default_limit=25, ordering="-username")
        filter_fields = {
            "id": ("exact", ),
            "first_name": ("icontains", "iexact"),
            "last_name": ("icontains", "iexact"),
            "username": ("icontains", "iexact"),
            "email": ("exact", "icontains", "iexact"),
            "is_staff": ("exact", ),
            "is_active": ("exact",),
        }
