from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question


def index(request):
	last_question_list = Question.objects.order_by('-pub_date')[:5]
	context = { 'last_question_list': last_question_list }
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        pass

    return HttpResponse("Your're votting on question %s." %question_id)



















