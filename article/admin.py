from django.contrib import admin

from . models import Article

# Register your models here.

#admin.site.register(Article)
#bu ilk hali
@admin.register(Article) #decorator seklinde class olusturuyoruz decorator normelde fonksiyonlar icin kullanilir ama bazen class icinde kullanabiliriz
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ['title','author','created_date'] 

    list_display_links = ['title','created_date']

    search_fields = ["title"]

    list_filter = ["title"]
    
    class Meta:
        model = Article