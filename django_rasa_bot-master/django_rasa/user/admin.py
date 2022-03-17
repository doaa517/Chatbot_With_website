from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


from .models import *


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name',
                                         'last_name',
                                         'father_name',
                                         'email',
                                         'phone',
                                         'gender',
                                         'address',
                                         'nationality',
                                         'birth_date',
                                         'profile_image')}),
        (_('Bank info'), {'fields': ('bank_name', 'bank_card_num',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Lecturer)
