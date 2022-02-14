from django import forms
from .models import Comment, RATE_CHOICES, Product, Order


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=True)
    stars = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Comment
        fields = ('content', 'stars')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('avg', 'nr_com')


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = '__all__'









