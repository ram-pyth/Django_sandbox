from django import forms
from .models import Order, OrderLine, Product, Client


def get_products_with_quantity_formset():
    # This function returns a formset for the OrderLine model to be used in the OrderForm
    from django.forms import inlineformset_factory
    ProductFormSet = inlineformset_factory(Order, OrderLine, fields=('product', 'quantity'),
                                           extra=len(Product.objects.all()))
    return ProductFormSet


def get_clients_choices():
    # This function returns choices for the clients dropdown in the OrderForm
    clients = Client.objects.all()
    return [(client.id, client.name) for client in clients]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'client']

    products = get_products_with_quantity_formset()
    product_quantities = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['client'].choices = [('', '---------')] + get_clients_choices()
        self.fields['product_quantities'] = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

    def clean(self):
        cleaned_data = super(OrderForm, self).clean()
        product_quantities = cleaned_data.get('product_quantities')
        if product_quantities <= 0:
            raise forms.ValidationError("Please select at least one product with a quantity greater than 0.")
        return cleaned_data
