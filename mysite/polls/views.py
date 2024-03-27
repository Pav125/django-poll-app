from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.db.models import F
from django.urls import reverse

from .models import Question,Choice

'''Each view is responsible for doing one of two things: returning an HttpResponse 
 object containing the content for the rquested page, or raising an exception such as 
 Http404.'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list]) #1 method
    # template = loader.get_template('polls/index.html') #2 method
    '''That code loads the template called polls/index.html and passes it a context. 
    The context is a dictionary mapping template variable names to Python objects.'''
    context = {
        'latest_question_list' : latest_question_list,
    }
    # return HttpResponse(template.render(context, request)) #2
    return render(request, 'polls/index.html', context)
    ''''''

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question deoes not exist')
    # The view raises the Http404 exception if a question with the requested ID doesn’t exist.
    
    # return HttpResponse("You're looking at question %s." %question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', { 'question' : question })

def results(request, question_id):
    # response = "You're looking at results of question %s."
    # return HttpResponse(response %question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(
        request,
        'polls/results.html',
        {
            'question' : question
        }
    )
    
def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." %question_id)
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
                'question' : question,
                'error_message' : "You did'nt select a choice"
            }
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
                                                  

    

'''There’s a problem here, though: the page’s design is hard-coded in the view. 
If you want to change the way the page looks, you’ll have to edit this Python code. 
So let’s use Django’s template system to separate the design from Python by creating 
a template that the view can use.'''