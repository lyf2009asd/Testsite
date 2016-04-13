from django.shortcuts import render
from .forms import SignUpForm,ContactForm
from django.conf import settings
# Create your views here.


def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None) #get the raw data
    context = {
        'title': title,
        'form': form,
    }
    #if request.user.is_authenticated():
        #title = "Sign Up Page %s" % request.user
    #if request.method == "Post":
        #print request.POST
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context ={
            "title": "Thank you",
        }

    return render(request, 'newsletter/home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():

        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')

        Subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youotheremail@gmail.com']
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_email,
            form_email,)
        some_html_message = """ <h1> Hello <h1>"""
        # send_mail = (Subject,
        #              contact_message,
        #              from_email,
        #              to_email,
        #              html_message=some_html_message,
        #             fail_silently=True)




    context = {
        "form": form,
    }
    return render(request, "newsletter/forms.html", context)
