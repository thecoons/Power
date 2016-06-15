"""View ClientWeb."""
# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'clientWeb/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'clientWeb/detail.html', {'question': question})


def results(request, question_id):
    response = ("You are looking at the results of question %s ." % question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return ("You're voting on question %s." % question_id)
