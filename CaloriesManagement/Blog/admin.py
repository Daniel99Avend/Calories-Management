from django.contrib import admin
from .models import *

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at')

    def save_model(self,request,obj,form,change):

        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

admin.site.register(food)
admin.site.register(meal,MealAdmin)
admin.site.register(hora)