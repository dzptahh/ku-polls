
from django.contrib.auth import logout

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vote, Question, Choice
from django.contrib.auth.models import User
import logging
from datetime import datetime



from .models import Choice, Question
from django.contrib import messages



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    """Class based view for viewing a poll."""
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        votes = question.can_vote()
        if not votes:
            messages.error(request, "This poll is not published.")
            return HttpResponseRedirect(reverse('polls:index'))
        return super().get(request, pk=pk)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required
def logout(request):
    # Log user out
    logout(request)
    return redirect('login')


def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            voted = Vote.objects.get(user=user, choice__question=question)
            voted.choice = selected_choice
            voted.save()
        except Vote.DoesNotExist:
            Vote.objects.create(user=user, choice=selected_choice).save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def get_client_ip(request):
    """Get the visitor’s IP address using request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
