from django.contrib import admin
from issues.models import Issue

# Register your models here.
class IssueAdmin(admin.ModelAdmin):

    list_display = ('id', 'title')

admin.site.register(Issue, IssueAdmin)