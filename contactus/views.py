from django.shortcuts import render, redirect
from .models import ContactUs
from .forms import ContactUsForm

def contact_us_view(request):
    messages = ContactUs.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us') 
    else:
        form = ContactUsForm()

    context = {
        'form': form,
        'messages': messages
    }
    return render(request, 'contactus/contact_us.html', context)
