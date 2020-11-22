from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        addressline1 = request.POST.get('addressline1')
        addressline2 = request.POST.get('addressline2')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        city = request.session.get('city')
        pincode = request.session.get('pincode')
        state = request.session.get('state')
        products = Product.get_products_by_id(list(cart.keys()))
        print(addressline1, addressline2, city, state, pincode,  phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          city=city,
                          state=state,
                          address1=addressline1,
                          address2=addressline2,
                          pincode=pincode,
                          phone=phone,
                          
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
