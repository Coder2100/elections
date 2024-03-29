from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic 

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
    #return HttpResponse(output)
    #return HttpResponse("Hello, world")

def detail(request, question_id):
    #long way
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
          """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
  
    #return HttpResponse("You loook at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #display the question voting frm
        return render(request, 'polls/detail', {
            'question': question,
            'error_message': "You didnt select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
   # return HttpResponse("You're voting on question %s." % question_id)

"""
<h2>{{ question.question_text }}</h2>
{% if error_message %}<p><strong>{{ error_message}}</strong></p> {% endif %}

<form action="{% url 'polls:vote' question.id %}" method="POST">
 {% csrf_token %}
 {% for choice in question.choice_set.all %} 
 <input type="radio" name="choice" id="choice{{ forloop.counter}}" value="{{choice.id}}" />
 <label for="choice{{ forloop.counter}}">{{ choice.choice_text }}</label> <br>
 {% endfor %}
 <input type="submit" value="Vote" />
</form>
"""