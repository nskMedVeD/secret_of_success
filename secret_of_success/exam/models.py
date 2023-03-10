from django.db import models

from main.models import Institution


class Expert(models.Model):
    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    patronymic = models.CharField('Отчество', max_length=255)
    position = models.CharField('Должность', max_length=255)
    institute = models.ForeignKey(Institution,
                                  verbose_name='Учреждение',
                                  on_delete=models.SET_DEFAULT,
                                  default='Нет данных')

    class Meta:
        verbose_name_plural = 'Эксперты'
        verbose_name = 'Эксперт'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} - {self.institute}'