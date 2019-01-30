from django.shortcuts import render, redirect
from .models import Candidate, Position
from django.http import HttpResponseRedirect
from .forms import NewCandidate, NewPosition

def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request, 'votes/index.html', context)

def candidate_detail(request, candidate_id):
    context = {}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    #context['votes'] = candidate.can.all.count(id=candidate_id)
    return render(request, 'votes/candidate_detail.html', context)

def candidate_create(request):
    context = {}
    form = NewCandidate(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
            return render(request, 'votes/candidate_create.html', context)
    else:
        context['form'] = NewCandidate()
        return render(request, 'votes/candidate_create.html', context)

def candidate_update(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)

    if request.method == 'POST':
        form = NewCandidate(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            context['form'] = form
            render(request, 'votes/candidate_update.html', context)
    else:
        context['form'] = NewCandidate(instance=candidate)
    return render(request, 'votes/candidate_update.html', context)

def position_create(request):
    context = {}
    form = NewPosition(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
            return render(request, 'votes/position_create.html', context)
    else:
        context['form'] = NewPosition()
        return render(request, 'votes/position_create.html', context)

def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    candidate.can.create()
    candidate.save()

    return redirect('votes:index')