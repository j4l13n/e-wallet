import logging
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.utils import timezone
from django.db.models import F
from django.conf import settings

from api.manager import BaseManager
from api.models import BaseModel
from api.utils.generators import id_generator, ID_LENGTH


logger = logging.getLogger(settings.LOGGER_NAME)


class UserManager(BaseUserManager, BaseManager):
    """
    User Manager Class

    Args:
        BaseUserManager (obj): Base User Manager Object
        BaseManager (obj): Base Manager Object

    Methods:
        create_user: Create new user method
        create_superuser: Create superuser method
    """

    def create_user(self, **kwargs):
        """
        Create User

        Raises:
            ValueError: Value error when error occur

        Returns:
            user: new user instance
        """
        username = kwargs.get("username")
        email = kwargs.get("email")
        password = kwargs.get("password")

        check_email = self.model.objects.filter(email=email).first()

        check_username = \
            self.model.objects.filter(username=username).first()

        if check_email:
            raise ValueError(
                "User with email {} already exists".format(email)
            )

        if check_username:
            raise ValueError(
                "User with username {} already exists".format(username)
            )
        try:
            user = self.model(
                username=username,
                email=self.normalize_email(email),
            )
            user.set_password(password)
            user.save()
            return user
        except ValueError as e:
            logger.error(e.args[0])
            return

    def create_superuser(self, email, password):
        """
        Crete superuser

        Args:
            email (str): super user email
            password (str): user password

        Returns:
            user: new superuser instance
        """
        try:
            user = self.create_user(email=email, password=password)
            user.is_superuser = user.is_staff = True
            user.is_active = user.is_admin = True
            user.save(using=self._db)
            return user
        except ValueError as e:
            logger.error(e.args[0])
            return


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    """
    id = models.CharField(
        max_length=ID_LENGTH,
        primary_key=True,
        default=id_generator,
        editable=False,
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()
    all_objects = UserManager(alive_only=False)

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name_plural = "Users"
        ordering = [F('email').asc(nulls_last=True)]

    def __str__(self):
        return self.email

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()

    @property
    def fullname(self):
        """
        Returns the person's full name.
        """
        return "%s %s" % (self.first_name, self.last_name)
