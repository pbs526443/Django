from django.shortcuts import render
from .models import vote,option
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def votelist (request):
    try:
        result = vote.objects.all()
        return render(request, 'poll/list.html', {'votes': result})
    except Exception as e:
        print(e)

def optionlist(request,voteid):
    try:
        vot = vote.objects.get(pk=voteid)
        print(vot.votename)
        result = vot.option_set.all()
        return render(request, 'poll/detail.html', {'options': result, 'vot': vot})
    except Exception as e:
        print(e)

def votedetail(request):
    try:
        optionid = request.POST['option']
        num = option.objects.get(pk=optionid)
        number = num.number + 1
        print(number)
        votid = request.POST['votid']
        print(votid)
        num.number = number
        print(num.number)
        num.save()
        vot = vote.objects.get(pk=votid)
        result = vot.option_set.all()
        return render(request, 'poll/votdetail.html', {'options': result, 'vot': vot})
        # return HttpResponseRedirect('/polls/votdetail.html',{'options': result, 'vot': vot})
    except Exception as e:
        print(e)