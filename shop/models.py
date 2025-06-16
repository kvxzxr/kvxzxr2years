from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва виробника")
    country = models.CharField(max_length=100, blank=True, verbose_name="Країна")
    founded_year = models.PositiveIntegerField(null=True, blank=True, verbose_name="Рік заснування")
    website = models.URLField(blank=True, verbose_name="Сайт")

    def __str__(self):
        return self.name


class Guitar(models.Model):
    BODY_TYPES = [
        ('ST', 'Stratocaster'),
        ('LP', 'Les Paul'),
        ('TE', 'Telecaster'),
        ('SG', 'SG'),
        ('EX', 'Explorer'),
    ]

    name = models.CharField(max_length=100, verbose_name="Назва гітари")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Виробник")
    body_type = models.CharField(max_length=2, choices=BODY_TYPES, default='ST', verbose_name="Тип корпусу")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    available = models.BooleanField(default=True, verbose_name="В наявності")
    color = models.CharField(max_length=50, default='Black', verbose_name="Колір")
    stock = models.PositiveIntegerField(default=10, verbose_name="Кількість на складі")
    added = models.DateField(auto_now_add=True, verbose_name="Дата додавання")
    description = models.TextField(blank=True, verbose_name="Опис", help_text="Короткий опис товару")

    def __str__(self):
        return f"{self.name} ({self.manufacturer.name})"

