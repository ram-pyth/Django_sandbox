from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world")


from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Order, OrderLine, Client, Product
from .forms import OrderForm


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm
    success_url = '/success/'  # Update this to the URL you want to redirect to after successful form submission

    # def form_valid(self, form):
    #     # You can add additional logic here if needed before saving the form
    #     return super().form_valid(form)

    def form_valid(self, form):
        # Save the main form
        response = super().form_valid(form)

        # Save the formset data
        product_formset = form.products(self.request.POST, instance=self.object)
        if product_formset.is_valid():
            print("valid")
            [print(k, v) for k, v in self.request.__dict__.copy().items()]
            product_formset.save()
        else:
            print("NOT VALID")
            print(product_formset.errors)

        return response
