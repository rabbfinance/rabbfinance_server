from django.shortcuts import render
from django.views.generic import TemplateView
from rabbfinance.money.models import Money
from django.db.models import Sum


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        total = Money.objects.aggregate(Sum('amount'))
        gasto = Money.objects.filter(amount__lte = 0).aggregate(Sum('amount'))
        ingresos = Money.objects.filter(amount__gte = 0).aggregate(Sum('amount'))
        
        context.update({
            'total': total['amount__sum'],
            'gasto': gasto['amount__sum']*-1,
            'ingresos': ingresos['amount__sum'],
        })
        return context
