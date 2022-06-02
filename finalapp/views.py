from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


#base function
def base_view(request):
    # return response
    return render(request, "base.html")

#search view
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Customers.objects.filter(Q(name__contains=searched) |Q(session__contains=searched) |Q(location__contains=searched) |Q(email__contains=searched) |Q(date__contains=searched))
        return render(request, 'search.html', {'searched': searched, 'items':items})
    else:
        return render(request, 'search.html', {})

#index view
def index(request):
    customer_list = Customers.objects.all().order_by('date')
    page = request.GET.get('page', 1)
    paginator = Paginator(customer_list,5)
    try:
        customer_list = paginator.page(page)
    except PageNotAnInteger:
        customer_list = paginator.page(1)
    except EmptyPage:
        customer_list = paginator.page(paginator.num_pages)
        
    context = {
        'customer_list' : customer_list
    }
    return render(request,'index.html', context)

#add new records function
def add(request):  
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        date = request.POST['date']
        session = request.POST['session']
        location = request.POST['location']
        customers = Customers(name = name, email = email, address = address, date = date, session = session, location = location)
        customers.save()
        messages.info(request,"Customer added successfully!")
    else:
        pass

    customer_list = Customers.objects.all()
    context = {
        'customer_list' : customer_list
    }

    return render(request,'add.html', context)

#delete record function
def delete(request, myid):
    customer = Customers.objects.get(id = myid)
    customer.delete()
    messages.info(request, "Customer deleted successfully!")
    return redirect(index)

#edit record function
def edit(request, myid):
    edit_customer = Customers.objects.get(id = myid)
    customer_list = Customers.objects.all()
    context = {
        'edit_customer': edit_customer,
        'customer_list' : customer_list
    }
    return render(request, 'edit.html', context)

#update record function
def update(request, myid):
    customer = Customers.objects.get(id = myid)
    customer.name = request.POST['name']
    customer.email = request.POST['email']
    customer.address = request.POST['address']
    customer.date = request.POST['date']
    customer.session = request.POST['session']
    customer.location = request.POST['location']
    customer.save()
    messages.info(request,"Customer updated successfully!")
    return redirect('index')

#view function
def view(request, myid):
    view_customer = Customers.objects.get(id = myid)
    edit_customer = Customers.objects.all()
    customer_list = Customers.objects.all()
    context = {
        'view_customer': view_customer,
        'edit_customer': edit_customer,
        'customer_list' : customer_list
    }
    return render(request, 'view.html', context)

#return to index function when user view a record
def back(request):
    return redirect('index')
