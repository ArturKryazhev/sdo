from django.db import models
from django.contrib.auth.models import User


class team(models.Model): #класс команды

    region_choices = []
    city_choices = []
    status_choices = []

    
    region = models.CharField(max_length=100, choices=region_choices)
    city = models.CharField(max_length=100, choices = city_choices)
    date_registraion = models.DateTimeField(auto_now=True, verbose_name='дата регистрации команды')
    team_status = models.CharField(max_length=50, choices = status_choices)
    e_mail = models.EmailField(null=True, blank= True)
 
    def __str__(self):
        return "руководитель : {} {} {}".format(self.leader.first_name, self.leader.second_name, self.leader.parent_name)

class member(models.Model): #класс участника конкурса
    status_choices = [('Не подтвержден e-mail','Не подтвержден e-mail'), ('Подтверждено','Подтверждено')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) #связь с встроенной моделью пользователя
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    second_name = models.CharField(max_length=50, verbose_name='Фамилия')
    parent_name = models.CharField(max_length=50, verbose_name='Отчество', null=True, blank = True)
    e_mail = models.EmailField(null = True)
    photo = models.ImageField(verbose_name='фото профиля',null=True, blank=True)
    phone_number = models.CharField(max_length=50, verbose_name='номер телефона',null=True, blank=True)
    whats_up = models.CharField(max_length=50, verbose_name='номер Whats Up',null=True, blank=True)
    pasport_series = models.CharField(max_length=10, verbose_name='Серия паспорта', null=True, blank=True)
    profile_status = models.CharField(max_length=50, choices=status_choices, default = 'не подтвержден e-mail')
    team = models.ForeignKey(team, on_delete=models.CASCADE, null=True,blank=True)
    is_leader = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return "{} {} {}".format(self.first_name, self.second_name, self.parent_name)
    

# Create your models here.
