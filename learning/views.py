from django.shortcuts import redirect, render
from .forms import MilkForm, SettingForm
from .models import Milk, Setting
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = MilkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Done")
            return redirect("/")
    else:
        form = MilkForm()
        return render(request, 'index.html', {'form': form})

def record(request):
    milk = Milk.objects.order_by('milk_date')
    total = Milk.objects.filter(milk_taken=True).count()
    setting = Setting.objects.all()
    return render(request, 'records.html', {'records': milk, 'setting': setting, 'total': total})

def setting(request):
    price = Setting.objects.get(id=1)
    if request.method != 'POST':
        form = SettingForm(instance=price)
    else:
        form = SettingForm(instance=price, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("settings")
    return render(request, 'settings.html', {'form': form})