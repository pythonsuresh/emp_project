from django.contrib import admin
from emp_app.models import emp

class empadmin(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Age','Email','Mob','Adress']

admin.site.register(emp,empadmin)


