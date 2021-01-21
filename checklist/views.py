from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from .models import item, sets
from .forms import displayedForm

# Create your views here.
def index(request):
    sets_list = sets.objects.order_by('-id')
    item_list = item.objects.order_by('-id')
    
    context = {
        'item_list': item_list,
        'sets_list': sets_list, 
    }
    return render(request, 'checklist/index.html', context)

def setDetail(request, sets_id):
    item_list = item.objects.order_by('-id')
    Sets = get_object_or_404(sets, pk=sets_id)
    context = {
        'item_list': item_list,
        'Sets': Sets

    }

    return render(request, 'checklist/setDetail.html', context)

def itemDetail(request, sets_id, item_id):

    Item = get_object_or_404(item, pk=item_id)
    a = item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = displayedForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request, 'checklist/itemDetail.html', {'Item': Item, 'form': form})
    else:
        form = displayedForm()
        
    return render(request, 'checklist/itemDetail.html', {'Item': Item, 'form': form})