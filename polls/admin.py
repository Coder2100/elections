from django.contrib import admin
#from django.contrib.admin import AdminSite
# Register your models here.
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
admin.site.site_header = "Elections"
#admin.site.site_title = "Admin Point for Election"

"""
class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'


admin_site = MyAdminSite(name='myadmin')
"""
