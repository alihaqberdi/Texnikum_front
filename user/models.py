from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def _create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('doctor_leader', 'Bosh shifokor'),
        ('doctor', 'Shifokor'),
        ('nurse', 'Hamshira'),
        ('citizen', 'Fuqoro'),
        ('admin', 'Admin'),
    )
    first_name = models.CharField(verbose_name='Ism', max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name='Familiya', max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name='Pochta', unique=False, blank=True, null=True)
    username = models.CharField(verbose_name='username', max_length=255, unique=True)
    is_staff = models.BooleanField(verbose_name='Xodimlarning holati', default=False, )
    is_active = models.BooleanField(verbose_name='Faol', default=True, )
    birthday = models.DateField(verbose_name="Tug'ilgan kun",
                                null=True, blank=True)
    phone = models.CharField(verbose_name='Telefon raqami', max_length=255, null=True, blank=True)
    user_type = models.CharField(verbose_name='Foydalanuvchi turi', max_length=255, choices=USER_TYPE, default='nurse')
    clinic_leader = models.ForeignKey('home.Clinic', verbose_name='Qaysi poliklinika bosh shifokori',
                                     on_delete=models.SET_NULL, null=True, blank=True)
    # doctor = models.ForeignKey('user.', verbose_name='Qaysi sektor rahbari',
    #                            on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'





