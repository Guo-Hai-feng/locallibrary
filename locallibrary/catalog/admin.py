from django.contrib import admin

# Register your models here.


from .models import Author, Genre, Book, BookInstance,Language

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra=0

class BooksInline(admin.TabularInline):
    model=Book
    extra=0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines=[BooksInline]




"""
BooksInstanceInline 类用于定义内联模型。
内联模型使你可以在 Book 模型的编辑页面上直接编辑关联的 BookInstance 记录。
admin.TabularInline 使用表格形式来显示和编辑内联模型。
"""




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    
    



@admin.register(BookInstance)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')  # 显示书籍、状态、到期日期和ID
   
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )




admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)