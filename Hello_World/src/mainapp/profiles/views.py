from django.shortcuts import render, get_object_or_404, redirect
from .models import Profiles
from .forms import ProfileForm


# Create your views here.


def profiles_console(request):
    profiles = Profiles.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profiles, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('profiles_console')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profiles.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profiles, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('profiles_console')
    context = {'item': item}
    return render(request, 'profiles/confirmDelete.html', context)


def confirmed(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect(request, 'profiles_console')
    else:
        return redirect('profiles_console')


def createUser(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profiles_console')
    else:
        print(form.errors)
        form = ProfileForm
    context = {
        'form': form,
    }
    return render(request, 'profiles/createUser.html', context)
