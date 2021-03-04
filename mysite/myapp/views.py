from django.shortcuts import render
from django.http import HttpResponse


def base(request):
    return render(request, 'base.html')


def articles(request):
    return render(request, 'articles.html')


def archive(request):
    return render(request, 'archive.html')


def users(request):
    return render(request, 'users.html')


def article(request, art_num):
    return render(request, 'article_number.html', {
        'art_num': art_num
    })


# def archive(request, art_num):
#     # return HttpResponse(
#     #     "This is an article #{} {}".format(art_num, "+archive"))
#     return render(request, art_num, {
#         'art_num': art_num
#     })


def slug_text(request, art_num, slug_text):
    return render(request, 'slug_text.html', {
        'art_num': art_num,
        'slug_text': slug_text
    })


def users_num(request, user_number):
    return HttpResponse('Number this User #{}'.format(user_number))


def number(request):
    return HttpResponse('This is correct number')


def last_url(request):
    return HttpResponse('It working')