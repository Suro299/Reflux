from django.shortcuts import render, redirect
from .models import User_Info, AboutMe, Content, Whats, Skill, Contact
from .forms import ContactForm
# Create your views here.

def home(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = ContactForm()
    myuser = User_Info.objects.all()[0]
    about = AboutMe.objects.all()[0]
    content_1 = Content.objects.all()[0]
    content_2 = Content.objects.all()[1]
    whats = Whats.objects.all()[0]
    skill_list = Skill.objects.all()
    return render(request, 'main/index.html', context={
        'myuser':myuser,
        'about':about,
        'content_1':content_1,
        'content_2':content_2,
        'whats':whats,
        'skill_list':skill_list,
        'form':form
        })