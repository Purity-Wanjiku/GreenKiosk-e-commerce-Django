from django.shortcuts import render, redirect
from .forms import OrderUploadForm
from orders.models import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
# Create your views here.

def upload_order(request):
    if  request.method == 'POST':
      form = OrderUploadForm(request.POST , request.FILES)
      if form.is_valid():
       form.save()
      
    else:
       
       form = OrderUploadForm()
    return render(request, 'orders/order_upload.html', {"form" : form})

def order_list(request):
    orders = Order.objects.all()

    return render( 
       request , "orders/order_list.html", {"orders" : orders}
    )

def order_details (request, id):
    order = Order.objects.get( id = id)

    return render(
        request, "orders/order_detail.html", {"order" : order}
    )


def edit_order(request,id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
       form = OrderUploadForm(request.POST, instance=order)
       if form.is_valid():
          form.save()
          return redirect("order_details", id=id)
    else:
       form = OrderUploadForm(instance=order)

    return render (request, "orders/order_edit.html", {"form":form})

