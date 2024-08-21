from django.shortcuts import render, redirect

# Create your views here.
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Part, PartCategory, Manufacturer

from .forms import PartForm


def part_search(request):
    query = request.GET.get('q')
    results = Part.objects.all()
    if query:
        results = results.filter(
            Q(car_model__manufacturer__name__icontains=query) |
            Q(car_model__name__icontains=query) |
            Q(original_part_name__icontains=query) |
            Q(compatible_part_name__icontains=query)
        )
    return render(request, 'parts/part_search.html', {'results': results})

@login_required
def part_create(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('part_list')
    else:
        form = PartForm()
    return render(request, 'parts/part_form.html', {'form': form})


def part_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    manufacturer_id = request.GET.get('manufacturer')

    parts = Part.objects.all()

    if query:
        parts = parts.filter(
            Q(car_model__manufacturer__name__icontains=query) |
            Q(car_model__name__icontains=query) |
            Q(original_part_name__icontains=query) |
            Q(compatible_part_name__icontains=query)
        )

    if category_id:
        parts = parts.filter(category_id=category_id)

    if manufacturer_id:
        parts = parts.filter(car_model__manufacturer_id=manufacturer_id)

    categories = PartCategory.objects.all()
    manufacturers = Manufacturer.objects.all()

    return render(request, 'parts/part_list.html', {
        'parts': parts,
        'categories': categories,
        'manufacturers': manufacturers
    })