# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response, render
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
# from  django.core.exceptions import DoesNotExist

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK all right!!!')

def root(request):
    posts = Question.objects.new()
   # question_all = Question.objects.all()
    limit = request.GET.get('limit', 10)
    currpage = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    baseurl = "/?page="
    page = paginator.page(currpage)
    argum = "Main page"
    question_url = "/question/"

    return render_to_response('main.html', {
        'paginator': paginator,
        'page': page,
        'posts': page.object_list,
        'baseurl': baseurl,
        'question_url': question_url,
        'arg': argum, } )

def question_page(request, id):
    try:
        question = Question.objects.get(id=id)
    except  Question.DoesNotExist:
        raise Http404
    user = 1
    if request.method == "POST":
       # form = AnswerForm(user, request.POST)
        form = AnswerForm(request.POST)
        if form.is_valid():
            url = "/question/" + str(id) + "/"
            form.save()
            # return HttpResponse("is valid!")
            # return HttpResponseRedirect("/")
            return HttpResponseRedirect(url)
        else:
            form.clean()
    else:
        # form = AnswerForm(request, initial={'question': str(id)})
        form = AnswerForm(initial={'question': str(id)})
    answer = Answer.objects.filter(question_id = id)

    return render(request, 'question_page.html', {
        'post': question,
        'answer': answer,
        'form': form,
    })

def popular_sort_page(request):
    posts = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    currpage = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    baseurl = "/popular/?page="
    page = paginator.page(currpage)
    argum = "Main page sort by popular"
    question_url = "/question/"
    return render_to_response('popular_sort_page.html', {
        'paginator': paginator,
        'page': page,
        'posts': page.object_list,
        'baseurl': baseurl,
        'question_url': question_url,
        'arg': argum, } )

def post_add(request):
    # user = 1
    if request.method == "POST":

        # form = AskForm(user, request.POST)
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = "/question/" + str(post.id) + "/"
          #  url = Concat(url, str(post.id), "/")
            return HttpResponseRedirect(url)
    else:
        #form = AskForm(request)
        form = AskForm()
    return render(request, 'askform.html', {
        'form': form,
    })



