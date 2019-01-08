from django.contrib import admin
from groups import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = GroupMember

admin.site.register(models.Group)
