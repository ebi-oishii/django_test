from django.contrib import admin
from django import forms
from .models import Publisher, Author, Book

# Register your models here.

class BookAdminForm(forms.ModelForm):
    def clean_title(self):
        value = self.cleaned_data["title"]
        if "Django" not in value:
            raise forms.ValidationError("タイトルには「Django」という文字列を含めてください")
        return value

class BookModelAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "price")
    ordering = ("-price")
    fields = ("title", "publisher", "authors", "price")
    form = BookAdminForm

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, BookModelAdmin)