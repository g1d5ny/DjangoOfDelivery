from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Point
from .forms import AddPointForm


@require_POST
def add_point(request):
    now = timezone.now()
    form = AddPointForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']

        try:
            point = Point.objects.get(code__iexact=code, use_from__lte=now, use_to__gte=now, active=True)
            request.session['point_id'] = point.id
        except Point.DoesNotExist:
            request.session['point_id'] = None

    return redirect('cart:detail')
