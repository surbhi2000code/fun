from django.shortcuts import render
from django.http import HttpResponse
from . models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
# params = {'no_of_slides': nSlides, range: range(1,nSlides), 'products': Products}
    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])
    params = {'AllProds': allprods}
    return render(request, 'lol/index.html', params)

def about(request):
    return render(request, "lol/about.html")


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, mobile=mobile, desc=desc)
        contact.save()
        thank = True
        return render(request, "lol/contact.html", {'thank': thank})

    return render(request, "lol/contact.html")

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'lol/tracker.html')

def search(request):
    return render(request, "lol/search.html")


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, "lol/ProductView.html", {'product': product[0]})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsjson', '')
        name = request.POST.get('name', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        address = request.POST.get('address1','') + " " + request.POST.get('address2','')
        order = Orders(items_json=items_json, name=name, email=email, mobile=mobile, city=city, state=state, address=address, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="the order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, "lol/checkout.html", {'thank': thank, 'id': id})

    return render(request, "lol/checkout.html")
