from django.db import models


class Diploma(models.Model):
    title = models.CharField(verbose_name='Название диплома', max_length=100)
    description = models.TextField(verbose_name='Описание(по желанию)', blank=True)
    file = models.FileField('Фотография или другой документ', upload_to='files')

    def __str__(self) -> str:
        return self.title
