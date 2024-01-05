from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice
from django.http import HttpResponseRedirect


@login_required(login_url='/user_auth/login/')
def index(request):
    """
    View for displaying the index page of the polls application.

    Retrieves the five most recent questions ordered by publication date
    and renders the 'polls/poll.html' template with the context containing
    the latest question list.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Renders the 'polls/poll.html' template.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)


def detail(request, question_id):
    """
    View for displaying the details of a specific question.

    Retrieves the question with the given question_id from the database
    or raises a 404 error if the question does not exist. Renders the
    'polls/detail.html' template with the retrieved question.

    Args:
        request: HttpRequest object.
        question_id (int): ID of the question.

    Returns:
        HttpResponse: Renders the 'polls/detail.html' template.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """
    View for displaying the results of a specific question.

    Retrieves the question with the given question_id from the database
    or raises a 404 error if the question does not exist. Renders the
    'polls/results.html' template with the retrieved question.

    Args:
        request: HttpRequest object.
        question_id (int): ID of the question.

    Returns:
        HttpResponse: Renders the 'polls/results.html' template.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """
    View for handling user votes on a specific question.

    Retrieves the question with the given question_id from the database
    or raises a 404 error if the question does not exist. If the user's
    choice is valid, increments the vote count for the selected choice
    and redirects to the 'results' page for that question.

    Args:
        request: HttpRequest object.
        question_id (int): ID of the question.

    Returns:
        HttpResponseRedirect: Redirects to 'polls:results' page.
    """
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))



    
     
    
