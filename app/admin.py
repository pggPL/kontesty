from django.contrib import admin

from app.models import User, Settings, News
# Register your models here.

admin.site.register(User)
admin.site.register(Settings)
admin.site.register(News)
