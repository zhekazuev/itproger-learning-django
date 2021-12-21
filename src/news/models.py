from django.db import models

class Article(models.Model):
    title = models.CharField("Title", max_length=50)
    anons = models.CharField("Anons", max_length=250)
    full_text = models.TextField("Article")
    date = models.DateTimeField("Publication Date", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self) -> str:
        """String for representing the Article object (in Admin site etc.)."""
        return f'{self.title}'

    def get_absolute_url(self):
        return f"/news/{self.id}"
    
