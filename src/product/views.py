from django.shortcuts import render
# from product.models import Product
from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=2)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "product/product_detail.html", context)