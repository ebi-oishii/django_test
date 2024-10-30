from django.db import models

# Create your models here.
class Publisher(models.Model):
    """出版社モデル"""
    class Meta:
        db_tablee = "publisher"
    
    name = models.CharField(verbose_name="出版社名", max_length=255)

    def __str__(self):
        return self.name


class Author(model.Model):
    """著者モデル"""
    class Meta:
        db_table = "author"

    name = models.CharField(verbose_name="著者名", max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """本モデル"""
    class Meta:
        db_table = 'book'

    title = models.CharField(verbose_name="タイトル", max_length=255, unique=True)
    publisher = models.ForeignKey(Publisher, verbose_name="出版社", on_deleta=models.PROTECT)
    authors = models.ManyToManyField(Author, verbose_name="著者")
    price = models.IntegerField(verbose_name="価格", null=True, blank=True)
    description = models.TextField(verbose_name="概要", null=True, blank=True)
    publish_date = models.DateField(verbose_name="出版日")

    def __str__(self):
        return self.title
    

class BookStock(models.Model):
    """本の在庫モデル"""
    class Meta:
        db_table = "book_stock"
    
    book = models.OneToOneField(Book, verbose_name="本", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="在庫数", default=0)

    def __str__(self):
        return self.book.title
