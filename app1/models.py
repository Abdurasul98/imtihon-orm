from django.db import models
from django.db.models.fields.json import JSONIContains


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    is_bool = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title





# 1) Category id 1 katta va 4 dan kechik bolgan idsini teskari sorov orqali oling
# 2) Category id si 1 dan 4 dan kichkina bolgan titleda lalom oszi bolgan newslar (buyam teskari sorov)
# 3) Category id si 1 3 5 bolgan newslarning id lari 3 dan katta bolganlari olinsin (teskari sorov)
# 4) 1 va 2 chi kategoriyadagi newslar (avvval kategoriya olinadi keyin newslari olinadi)
# 5) News jadvalining title da salom sozi bolgan kategoriyalar soni +
# 6) Har bir kategory dagi newslar soni +
# 7) id si 4 dan katta bolgan newslarning soni +
# 8) har bir kategorydagi ortacha korishlar soni kategoriya id si 1 dan balan newslarni id si 5 dan katta
# 9) Category 2 dan katta yoki teng bolgan ortacha korishlar soni 30 dan katta bolgan kategorylar
# 10) har bir kategorydagi eng kam korishlar soni va kategory nomi
