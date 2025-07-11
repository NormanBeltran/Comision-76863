from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Gender(models.Model):
    name = models.CharField(verbose_name="Género", max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Géneros"
        verbose_name = "Género"
        ordering = ["id"]
    
class Company(models.Model):
    name = models.CharField(verbose_name="Compañía", max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"    

    class Meta:
        verbose_name_plural = "Compañías"
        verbose_name = "Compañía"
        ordering = ["id"]

class Movie(models.Model):
    name = models.CharField(verbose_name="Película", max_length=50)
    description = models.TextField(verbose_name="Sinopsis")
    RATING = [
        (1, "Mala"),
        (2, "Mediocre"),
        (3, "Buena"),
        (4, "Muy Buena"),
        (5, "Excelente"),
    ]
    rating = models.PositiveSmallIntegerField(choices=RATING)
    premiere = models.PositiveSmallIntegerField(verbose_name="Año de estreno", null=False, blank=False)
    genders = models.ManyToManyField(Gender, verbose_name="Géneros")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Compañía")
    image = models.ImageField(upload_to="movies", null=True, blank=True, verbose_name="Cover")

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"    

    class Meta:
        verbose_name_plural = "Películas"
        verbose_name = "Película"
        ordering = ["name"]

    @admin.display(ordering="description")
    def sinopsis(self):
        return format_html(self.description[:20] + "...")

    @admin.display(ordering="name")
    def pelicula(self):
        return format_html(f"<span style='color:red;'>{self.name}</span>")
    
    @admin.display(ordering="rating")
    def estrellas(self):
        stars = "*"*self.rating
        return format_html(f"<span style='color:green;'>{stars}</span>")    
