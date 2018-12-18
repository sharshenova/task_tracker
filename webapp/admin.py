from django.contrib import admin
from webapp.models import Project, Issue, Programmer, Work
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProgrammerInline(admin.StackedInline):
    model = Programmer
    filter_horizontal = ('issues', )


class ProgrammerAdmin(UserAdmin):
    inlines = (ProgrammerInline,)


admin.site.unregister(User)
admin.site.register(User, ProgrammerAdmin)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Work)
