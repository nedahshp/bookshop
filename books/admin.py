from django.contrib import admin
from .models import books,coment


class CommentAdmin(admin.ModelAdmin):
    list_display =('author','book','text','datetime_created')
# Register your models here.
admin.site.register(books)
admin.site.register(coment,CommentAdmin)