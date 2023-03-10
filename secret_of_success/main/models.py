from django.db import models


class ContestNomination(models.Model):
    title = models.CharField('Название номинации', max_length=255)
    nomination_letter = models.CharField('Буква номинации', max_length=1, unique=True)

    class Meta:
        verbose_name_plural = 'Конкурсные номинации'
        verbose_name = 'Конкурсная номинация'
        ordering = ['nomination_letter']

    def __str__(self):
        return f'{self.nomination_letter} - {self.title}'


class Institution(models.Model):
    zip_code = models.CharField('Индекс', default='000000', max_length=6)
    city = models.CharField('Город', max_length=255)
    address = models.CharField('Адрес учреждения', max_length=255)
    short_name = models.CharField('Краткое название учреждения', max_length=255)
    name = models.CharField('Название учреждения', max_length=255)

    class Meta:
        verbose_name_plural = 'Учреждения'
        verbose_name = 'Учреждение'

    def __str__(self):
        return self.short_name


class Author(models.Model):
    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    patronymic = models.CharField('Отчество', max_length=255)
    position = models.CharField('Должность', max_length=255)
    institute = models.ForeignKey(Institution,
                                  verbose_name='Учреждение',
                                  on_delete=models.SET_DEFAULT,
                                  default='Нет данных')

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} - {self.institute}'


class ContestMaterial(models.Model):
    name = models.CharField('Название материала', max_length=255)
    nomination = models.ForeignKey(ContestNomination,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   verbose_name='Номинация',
                                   )
    main_author = models.ForeignKey(Author,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name='Руководитель авторской группы')
    other_authors = models.ManyToManyField(Author,
                                           related_name='other_author',
                                           null=True,
                                           blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Конкурсные материалы'
        verbose_name = 'Конкурсный материал'

    def __str__(self):
        return self.name
