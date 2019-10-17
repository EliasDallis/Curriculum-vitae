from django.contrib import admin
from helloworld.models import (PreviousFirm, 
                                    PreviousTitle, 
                                    CurrentObjective, 
                                    Education, Biography, 
                                    Message, Skill,
                                    Portfolio)
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    ##fields = ['time', 'name', 'text', 'email'] ## field order
    list_display = ['time', 'name' , 'text']

admin.site.register(PreviousFirm)
admin.site.register(PreviousTitle)
admin.site.register(CurrentObjective)
admin.site.register(Education)
admin.site.register(Biography)
admin.site.register(Message, MessageAdmin)
admin.site.register(Skill)
admin.site.register(Portfolio)
