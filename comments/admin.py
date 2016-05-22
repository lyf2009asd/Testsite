from django.contrib import admin
from .models import Comment
# Register your models here.


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["content", "timestamp"]
    list_filter = ["content", "timestamp"]

    class Meta:
        model = Comment
admin.site.register(Comment, CommentModelAdmin)
