from django.contrib import admin

from .models import Employee


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(Employee)

admin.site.site_header = "MigrantDoc Admin"
admin.site.site_title = "MigrantDoc Admin Portal"
admin.site.index_title = "Welcome to MigrantDoc"

