from django.contrib import admin

from .models import ContactForm, File, FilesAdmin, Post


class FormsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]

    class Meta:
        model = ContactForm


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ContactForm, FormsAdmin)
admin.site.register(FilesAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(File)
