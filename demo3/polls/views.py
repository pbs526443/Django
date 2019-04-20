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

def addvote(request):
    return render(request,'poll/addvote.html')

def voteadd(request):
    votename = request.POST['votename']
    vot = vote()
    vot.votename = votename
    vot.save()

    return HttpResponseRedirect('/polls/')

def updatevote(request,vid):
    result = vote.objects.get(pk=vid)
    return render(request,'poll/updatevote.html',{"vote":result})

def voteupdate(request):
    votename = request.POST['votename']
    vid = request.POST['vid']

    vot = vote.objects.get(pk=vid)
    vot.votename = votename
    vot.save()

    return HttpResponseRedirect('/polls/')

def votdelete(request,vid):
    vote.objects.get(pk=vid).delete()
    return HttpResponseRedirect('/polls/')

def addoption(request,vid):
    vot = vote.objects.get(pk=vid)
    return render(request,'poll/addoption.html',{"vot":vot})


def optionadd(request):
    vid = request.POST['vid']
    options = request.POST['options']
    number = request.POST['number']

    opt = option()
    opt.options = options
    opt.number = number
    result = vote.objects.get(pk=vid)
    opt.voteid = result
    opt.save()


    return HttpResponseRedirect('/polls/optionlist/'+ str(result.id) +'/')

def updateoption(request,oid):
    result = option.objects.get(pk=oid)
    vot = vote.objects.get(votename=result.voteid)
    return render(request,'poll/updateoption.html',{"result":result,"vot":vot})

def optionupdate(request):
    oid = request.POST['oid']
    options = request.POST['optionname']
    number = request.POST['number']

    h1 = option.objects.get(pk=oid)
    h1.options = options
    h1.number =number
    result = vote.objects.get(votename=h1.voteid)
    h1.voteid = result
    h1.save()

    return HttpResponseRedirect('/polls/optionlist/'+ str(result.id) +'/')

def deleteoption(request,oid):
    opt = option.objects.get(pk=oid)
    result = vote.objects.get(votename=opt.voteid)
    option.objects.get(pk=oid).delete()
    return HttpResponseRedirect('/polls/optionlist/'+ str(result.id) +'/')

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
        if 'option' in request.POST:
            optionid = request.POST['option']
            print(optionid)
            num = option.objects.get(pk=optionid)
            number = num.number + 1
            print(number)
            votid = request.POST['votid']
            print(votid)
            num.number = number
            print(num.number)
            num.save()
            return HttpResponseRedirect('/polls/optdetail/'+ str(votid) +'/')
        else:
            votid = request.POST['votid']
            return HttpResponseRedirect('/polls/optionlist/' + str(votid) + '/')
    except Exception as e:
        print(e)

def optdetail(request,votid):
    vot = vote.objects.get(pk=votid)
    print(vot.id)
    return render(request, 'poll/votdetail.html', { 'vot': vot})