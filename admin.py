from django.contrib import admin
from admissionapp.models import *

# Register your models here.


admin.site.register(User)

admin.site.register(Student)

admin.site.register(College)

admin.site.register(Review)

admin.site.register(Application)

admin.site.register(Notification)


