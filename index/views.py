from django.shortcuts import render
from index.forms import ContactForm
from index.models import Contact, Category, Project, Human, Sumary, Education, ProfessionalExperience
import requests

def home(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            token = '7638919419:AAG0EYZ0fcdTahTIcM-ZicpIKZQ1dfKYQug'
            tg_id = str(919323624)
            form.save()
            text = f"\nXabar keldi! \n\nXabar egasi: {name}\nEmail: {email}\nXabar maqsadi: {subject}\nXabar: {message}"
            url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
            requests.get(url + tg_id + '&text=' + text)
        else:
            print(form.errors)

    categories = Category.objects.all()
    projects = Project.objects.all()
    people = Human.objects.all()
    sumaries = Sumary.objects.all()
    educations = Education.objects.all()
    proexies = ProfessionalExperience.objects.all()

    context = {
        "form": form,
        "categories": categories,
        "projects": projects,
        "people": people,
        "sumaries": sumaries,
        "educations": educations,
        "proexies": proexies,
    }

    return render(request, "index.html", context=context)