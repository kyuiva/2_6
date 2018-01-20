# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from qa.models import Question, Answer
from django.core.paginator import Paginator
from django.http import Http404
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

    answer = Answer.objects.filter(question_id = id)

    return render_to_response('question_page.html', {
        'post': question,
        'answer': answer,
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
