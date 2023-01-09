from django.shortcuts import render
from .models import Skill, Message, Project
from django.http import HttpResponseRedirect

# Create your views here.
def main(request):
    skill = Skill.objects.all()
    project = Project.objects.all()
    return render(request, 'index.html', {'skill': skill, 'project': project})

def message(request):
    if request.method == 'POST':
        message = Message()
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.text = request.POST.get('message')
        message.save()
    return HttpResponseRedirect('/')




