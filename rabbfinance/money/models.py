from django.conf import settings
from django.db.models import ForeignKey, BigIntegerField, CharField, CASCADE
from rabbfinance.utils.models import BaseAppModel
from rabbfinance.category.models import Category,Origin


class Money(BaseAppModel):
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    amount = BigIntegerField()
    category = ForeignKey(Category, on_delete=CASCADE)
    description = CharField(blank=True, max_length=255)
    origin = ForeignKey(Origin,blank=True,null=True, on_delete=CASCADE)

    class Meta:
        ordering = ['-amount']

    def __str__(self):
        return str(self.amount)
    

    def get_absolute_url(self):
        return reverse("mony_detail", kwargs={"pk": self.pk})


