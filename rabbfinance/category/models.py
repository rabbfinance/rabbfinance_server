from django.conf import settings
from django.db.models import SlugField, CharField, ForeignKey, CASCADE
from django.utils.text import slugify
from rabbfinance.utils.models import BaseAppModel


# Modelo category
class Category(BaseAppModel):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)
    parent = ForeignKey('self', blank=True, null=True, related_name='children', on_delete=CASCADE)
    owner = ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        full_path = [self.name]
        n = self.parent

        while n is not None:
            full_path.append(n.name)
            n = n.parent

        return ' -> '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Origin(BaseAppModel):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)
    owner = ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=CASCADE)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Origin, self).save(*args, **kwargs)


    class Meta:
        verbose_name = ("Origin")
        verbose_name_plural = ("Origins")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Origin_detail", kwargs={"pk": self.pk})
