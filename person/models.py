from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Person(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=30)
    last_name = models.CharField(verbose_name='Last Name', max_length=30)
    #id = models.CharField(verbose_name='ID', max_length=10, db_index=True)
    birthday = models.DateField(verbose_name='birthday')
    nationalities = {
        (1, 'rus'),
        (2, 'fr'),
        (3, 'ger'),
        (4, 'eng'),
        (5, 'esp')
    }
    nationality = models.IntegerField(verbose_name='nationality', choices=nationalities)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)