from django.contrib import admin

from .models import Usermsg, Intent, Answer, Story, Action

    
admin.site.register(Intent)
admin.site.register(Usermsg)
admin.site.register(Answer)
admin.site.register(Story)
admin.site.register(Action)

