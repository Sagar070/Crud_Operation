from django.contrib import admin
from .models import user

admin.site.register(user)
class userAdmin(admin.ModelAdmin):
    list_display=('id','Name','Email','Password')
# Register your models here.
