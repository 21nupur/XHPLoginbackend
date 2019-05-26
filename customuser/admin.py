from django.contrib import admin
from .models import CustomUser
# from .forms import UserForm


class UserFormAdmin(admin.ModelAdmin):
    # form = UserForm
    labels = ('id', )


admin.site.register(CustomUser, UserFormAdmin)