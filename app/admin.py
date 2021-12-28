from django.contrib import admin
from app.models import TODO
from django.contrib.auth.models import User
# register model to admin
admin.site.register(TODO)

admin.site.register(User)