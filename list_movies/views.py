from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Product, Comment
from users.models import Profile
from .forms import *
from django.db.models import Avg, Max
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from .filters import OrderFilter
from .forms import OrderForm


def show_all_movie_review(request):

    products = Product.objects.all()
    paginator = Paginator(products, 5)

    page_obj = paginator.get_page(request.GET.get('page', 1))

    my_filter = OrderFilter()

    context = {
        'page_obj': page_obj,
        'my_filter': my_filter,
    }
    return render(request, 'list/list.html', context)


def show_all_movie_details(request, pk):
    post = Product.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

    nr_com = comments.count()
    avg = average_review(pk)
    Product.objects.filter(id=pk).update(nr_com=nr_com, avg=avg)
    each_product = Product.objects.get(id=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            stars = request.POST.get('stars')

            user_id = request.user.id
            coins = request.user.profile.coins
            coins = coins + 10

            last_comm = content
            timestamp = datetime.now()

            Profile.objects.filter(user_id=user_id).update(coins=coins, last_comm=last_comm, timestamp=timestamp)

            comment = Comment.objects.create(post=post, user=request.user, stars=stars, content=content)
            comment.save()
            messages.success(request, 'Thanks for your submit! You receive +10 coins!')

            return redirect(reverse('list:details', args=(pk,)))

    else:
        comment_form = CommentForm()

    stuff = get_object_or_404(Product, id=pk)
    total_likes = stuff.total_likes()
    liked = False

    if stuff.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'each_product': each_product,
        'comments': comments,
        'comment_form': comment_form,
        'total_likes': total_likes,
        'liked': liked,
    }

    return render(request, 'list/details.html', context)


def average_review(pk):
    reviews = Comment.objects.filter(post_id=pk).aggregate(average=Avg('stars'))

    avg = 0
    if reviews['average'] is not None:
        avg = float(reviews['average'])
        avg = round(avg, 1)
    return avg


def like_view(request, pk):
    post = get_object_or_404(Product, id=request.POST.get('each_product_pk'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        total_like = Product(pk).total_likes()
        Product.objects.filter(id=pk).update(total_like=total_like)
    else:
        post.likes.add(request.user)
        liked = True
        total_like = Product(pk).total_likes()
        Product.objects.filter(id=pk).update(total_like=total_like)

    return HttpResponseRedirect(reverse('list:details', args=(pk,)))



