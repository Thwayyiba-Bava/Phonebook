from django.shortcuts import render
from.models import Phonebook

# Create your views here.
def home(request):
    return render(request,"home.html")

def add_contact(request):
    responseDict={}
    try:
        name=request.POST['name']
        phno=request.POST['phno']
        conList=Phonebook.objects.all()
        for i in conList:
            if name in i.name:
                responseDict["msg1"]="Name already exists!"
                responseDict["obj"]=Phonebook.objects.all()
                return render(request,"home.html",responseDict)
        contactList=Phonebook(name=name,phone_no=phno)
        contactList.save()
        responseDict["msg1"]="Contact added"
        responseDict["obj"]=Phonebook.objects.all()
        return render(request,"home.html",responseDict)
    except Exception as e:
        print(e)
        responseDict["msg2"]="Contact cannot be added"
        return render(request,"home.html")
    
def update_contact(request):
    responseDict={}
    flag=0
    try:
        data=request.POST['opr']
        if (data=='Update Name'):
            oldName=request.POST['oldname']
            newName=request.POST['newname']
            contactList=Phonebook.objects.filter(name=oldName)
            contacts=Phonebook.objects.all()
            for i in contacts:
                if newName in i.name:
                    responseDict["msg4"]="Name already exists!!"
                    return render(request,"home.html",responseDict)
            for i in contactList:
                i.name=newName
                i.save()
            responseDict["msg3"]="Name Updated.."
            return render(request,"home.html",responseDict)
        elif(data=='Update Phone Number'):
            name=request.POST['name']
            phno=request.POST['phoneno']
            contactList=Phonebook.objects.get(name=name)
            if name in contactList.name:
                contactList.phone_no=phno
                contactList.save()
                responseDict["msg3"]="Phone Number Updated"
                return render(request,"home.html",responseDict)
            else:
                responseDict["msg3"]="Contact not exists!!"
                return render(request,"home.html",responseDict)
        else:
            return render(request,"home.html")
    except Exception as e:
        print(e)
        responseDict["msg3"]="Contact cannot be updated"
        return render(request,"home.html")

def display(request):
    responseDict={}
    responseDict["obj1"]=Phonebook.objects.all()
    return render(request,"home.html",responseDict)


