from django.shortcuts import render,HttpResponseRedirect
from .forms import userForm
from .models import user
# this function add items.
def add(request):
    if request.method=='POST':
        abc=userForm(request.POST)
        if abc.is_valid():
            # id=abc.cleaned_data['id']
            nm=abc.cleaned_data['Name']
            em=abc.cleaned_data['Email']
            pwd=abc.cleaned_data['Password']
            new=user(Name=nm,Email=em,Password=pwd)
            new.save()
            abc=userForm()
            # return redirect('addandshow')
    else:
        abc=userForm()
    st=user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':abc,'student':st})


# this function delete the record

def delete(request,id):
    if request.method=="POST":
        pk=user.objects.get(pk=id)
        pk.delete()
        return HttpResponseRedirect('/')

# this is upadate function

def update(request,id):
    if request.method=="POST":
        n=user.objects.get(pk=id)
        pk=userForm(request.POST, instance=n)
        if pk.is_valid():
            pk.save()
    else:
        n=user.objects.get(pk=id)
        pk=userForm(instance=n)


    # up=user.objects.all()
    return render(request,'enroll/updatestudent.html',{'d':pk})