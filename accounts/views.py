from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    errors = None
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")
        else:
            for err in form.error_messages:
                print(err, dir(err))
            errors = [ msg for msg in form.error_messages ]

    form = UserCreationForm
    return render(request = request,
                  template_name = "accounts/register.html",
                  context={"form": form, "errors": errors})
