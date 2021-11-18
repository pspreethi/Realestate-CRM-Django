from django.shortcuts import render, redirect
from .forms import ClientUpdateForm, PropertyUpdateForm
from django.contrib.auth.models import User
from .models import Client,Property,Review
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
import pandas as pd
from django_pandas.io import read_frame
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request,'home.html')


@login_required
def properties(request):
    properties = Property.objects.all()
    return render(request,'properties.html', {'properties':properties})


def faq(request):
    return render(request,'faq.html')


def adminhome(request):
    return render(request,'addclient.html')


def getintouch(request):
        if request.method=="POST":
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            need = request.POST['need']
            message = request.POST['message']
            print(firstname,lastname,email,need,message)
            subject = need
            msg     = "From: "+firstname+" "+lastname+"\n"+"Email: "+email+"\n"+"Message: "+message
            to      = ['laharipedineedi@gmail.com','raveenab113@gmail.com']
            res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, to)
        return render(request,'getintouch.html')


def requestinfo(request):
        if request.method=="POST":
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            mobile = request.POST['mobile']
            email = request.POST['email']
            need = request.POST['need']
            message = request.POST['message']
            print(firstname,lastname,mobile,email,need,message)
            subject = need
            msg     = "From: "+firstname+" "+lastname+"\n"+ "Mobile: "+mobile+"\n"+"Email: "+email+"\n"+"Message: "+message
            to      = ['laharipedineedi@gmail.com','raveenab113@gmail.com']
            res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, to)
        return render(request,'requestinfo.html')


def addclient(request):
    if request.method=="POST":
        newclient = Client.objects.create(
        firstname = request.POST['firstname'],
        lastname = request.POST['lastname'] ,
        mobile = request.POST['mobile']  ,                 
        address = request.POST['address'],
        email = request.POST['email'],
        gender = request.POST['gender'],
        dob = request.POST['dob'],
        city = request.POST['city'],
        state = request.POST['state'],
        occupation = request.POST['occupation'],
        source = request.POST['source'],
        agent = request.POST['agent'],
        follow_up_date = request.POST['follow_up_date'],
        doj = request.POST['doj'],
        remarks = request.POST['remarks'],
        contacted = request.POST['contacted'].lower())
        newclient.save()
        return redirect('/addclient/')
    return render(request,'addclient.html',{})


def viewclients(request):
    clients = Client.objects.all()  							#  "select * from blog"
    return render(request, 'viewclients.html', {'clients':clients})


def updateclient(request,firstname):
        form = ClientUpdateForm()
        selected_client = Client.objects.get(firstname=firstname)
        if request.method=="POST":
            form = ClientUpdateForm(request.POST, instance=selected_client)
            if form.is_valid():
                form.save()
                return redirect('/addclient/')
        else:
            form = ClientUpdateForm(instance=selected_client)
        return render(request, 'updateclient.html', {'form':form})


def deleteclient(request, firstname):
	selected_client = Client.objects.get(firstname=firstname)
	selected_client.delete()
	return redirect('/viewclients/')


def property(request,property_name):
    property = Property.objects.filter(property_name=property_name)
    return render(request, 'property.html', {'property':property})


def addproperty(request):
    if request.method=="POST":
        newproperty = Property.objects.create(
            banner = request.FILES['banner'],
            property_name = request.POST['property_name'].split()[0],
            property_type = request.POST['property_type'] ,
            area = request.POST['area']  ,
            price = float(request.POST['price']),
            no_of_bedrooms = int(request.POST['no_of_bedrooms']),
            no_of_bathrooms = int(request.POST['no_of_bathrooms']),
            city = request.POST['city'],
            state = request.POST['state'])
        newproperty.save()
        return redirect('/viewproperties/')
    return render(request,'addproperty.html',{})


def viewproperties(request):
    properties = Property.objects.all()
    return render(request, 'viewproperties.html', {'properties':properties})


def updateproperty(request, property_name):
	selected_property = Property.objects.get(property_name=property_name)
	if request.method=="POST":
		form = PropertyUpdateForm(request.POST, instance=selected_property)
		if form.is_valid():
			form.save()
			return redirect('/viewproperties/')
	else:
		form = PropertyUpdateForm(instance=selected_property)
	return render(request, 'updateproperty.html', {'form':form})


def deleteproperty(request, property_name):
	selected_property = Property.objects.get(property_name=property_name)
	selected_property.delete()
	return redirect('/viewproperties/')


def loginpage(request):
    if request.method=="POST":
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('/')
            except Exception as e:
                print(e)
                return render(request, 'errorpage.html', {})
    return render(request, 'loginpage.html', {})


def register(request):
    if request.method=="POST":
        newuser = User.objects.create_user(
        username = request.POST['username'],
        first_name = request.POST['first_name'] ,
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = request.POST['password']
        )
        newuser.save()
        return redirect('/')
    return render(request,'register.html')


def logoutpage(request):
    logout(request)
    return redirect('/')



def upcoming(request):
    startdate = datetime.today()
    enddate = startdate + timedelta(days=6)
    clients = Client.objects.filter(follow_up_date__range=[startdate,enddate])
    print(clients)							#  "select * from blog"
    return render(request, 'upcoming.html', {'clients':clients})


def performance(request):
    qs = Client.objects.all()
    df = read_frame(qs)
    df['contacted'] = df['contacted'].map({'Yes': 'yes','YES':'yes', 'No': 'no','NO':'no'})
    d = df.contacted.value_counts()
    print(d)
    try:
        no_c = d['no']
        print(no_c)
    except Exception as e:
        print(e)
        no_c = 0
    try:
        yes_c = d['yes']
        print(yes_c)
    except Exception as e:
        print(e)
        yes_c = 0
    labels = ['Contacted','Not Contacted']
    data = [yes_c, no_c]
    print(data)
    return render(request, 'performance.html', {
        'labels': labels,
        'data': data,
    })


def source(request):
    qs = Client.objects.all()
    df = read_frame(qs)
    df['source'] = df['source'].map({'Website': 'website','WEBSITE':'website', 'Agent': 'agent','AGENT':'agent','Call':'call','CALL':'call'})
    d = df.source.value_counts()
    print(d)
    try:
        web_c = d['website']
        print(web_c)
    except Exception as e:
        print(e)
        web_c = 0
    try:
        agent_c = d['agent']
        print(agent_c)
    except Exception as e:
        print(e)
        agent_c = 0
    try:
        call_c = d['call']
        print(call_c)
    except Exception as e:
        print(e)
        call_c = 0
    labels = ['Website','Agent', 'Call']
    data = [web_c, agent_c,call_c]
    print(labels)
    print(data)
    return render(request, 'source.html', {'labels': labels,'data': data})


def progress(request):
    qs = Client.objects.all()
    df = read_frame(qs)
    df['doj'] = pd.to_datetime(df['doj'])
    df1 = df.groupby(df['doj'].dt.to_period('M')).count()
    d = dict(df1['id'])
    periods = list(d.keys())
    labels = []
    for i in periods:
        labels.append(str(i))
    data = list(d.values())
    return render(request, 'progress.html', {'labels': labels,'data': data})


def errorpage(request):
    return render(request,'errorpage.html')



def viewinfo(request,property_name):
    try:
        property = Property.objects.get(property_name=property_name)
        return render(request, 'viewinfo.html', {'property':property})
    except:
        return render(request, 'viewproperties.html')

@login_required
def review(request,property_name):
    review_property = Property.objects.get(property_name=property_name)
    
    wished_item = Review.objects.get_or_create(wished_item=review_property,
        property_name = review_property.property_name,
        property_type = review_property.property_type,
        area = review_property.area,
        price = review_property.price,
        no_of_bedrooms = review_property.no_of_bedrooms,
        no_of_bathrooms = review_property.no_of_bathrooms,
        city = review_property.city,
        state= review_property.state,
        user = request.user)
    # wished_item.save()
    return redirect('/properties/')
   
    # return render(request, 'properties.html')


@login_required
def reviewlist(request):
    properties = Review.objects.all()
    return render(request,'review.html', {'properties':properties})

def deleteproperty(request, property_name):
    user = request.user
    selected_property = Review.objects.filter(property_name=property_name, user=user )
    selected_property.delete()
    return redirect('/reviewlist/')