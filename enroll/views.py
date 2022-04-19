from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


#This function will add new item and show new items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
        # return redirect('addnshow')
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'addnshow.html', {'form': fm, 'stu': stud})

#This function will Update/Edit
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request, 'updatestudent.html',{'form':fm})




#This Function will delete
def delete_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')