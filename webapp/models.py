from django.db import models


from django.contrib.auth.models import User


class Programmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='info', verbose_name='Пользователь')
    birth_date = models.DateField(verbose_name='День рождения')
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    projects = models.ManyToManyField('Project', blank=True, through='Work', through_fields=('programmer', 'project'), related_name='programmers', verbose_name='Проекты')
    issues = models.ManyToManyField('Issue', blank=True, related_name='programmers', verbose_name='Задачи')

    def __str__(self):
        return "%s. %s %s" % (self.pk, self.user.first_name, self.user.last_name)


class Project(models.Model):
    project = models.CharField(max_length=200, verbose_name='Проект')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.project


class Issue(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_ON_PAUSE = 'on_pause'
    STATUS_DONE = 'done'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новая'),
        (STATUS_IN_PROGRESS, 'В процессе'),
        (STATUS_ON_PAUSE, 'На паузе'),
        (STATUS_DONE, 'Выполнена'),
        (STATUS_CANCELED, 'Отменена')
    )

    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='issues', verbose_name='Проект')
    title = models.CharField(max_length=200, verbose_name='Задача')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW, verbose_name='Статус')

    def __str__(self):
        return self.title


class Work(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='work')
    programmer = models.ForeignKey(Programmer, on_delete=models.PROTECT, related_name='work')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')

    def __str__(self):
        return "%s. %s - %s" % (self.pk, self.project.project, self.programmer.user.get_full_name())
