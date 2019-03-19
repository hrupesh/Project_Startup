# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from user_model.models import register_model, address
from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
def profile(request):
    request.session.set_expiry(300)
    print ('profile user_id is')
    try:
        the_userid = request.session['user_id']
        print (the_userid)
        register_mod = register_model.objects.get(id = the_userid)
        try:
            if the_userid:
                print ("hey profile")
                
                print (register_mod)
                context = {
                    'register_mod' : register_mod
                }                    
                return render(request, 'profilee/profile.html', context)
            else:
                print ('no profile')
                context = {
                    'message': 'Might be there is some error, please try again later' 
                }
                
        except:
            context = {
                    'message': 'Might be there is some error, please try again later' 
                }
    except:
        print ('no the_id')
        context = {
                    'message': 'Please Login your account and if you are a new user than register first and than proceed' 
                }
    return render(request, 'user_model/error.html', context)

    


def edit_profile_page(request):
    request.session.set_expiry(300)
    print ('profile user_id is')
    try:
        the_userid = request.session['user_id']
        print (the_userid)
        register_models = register_model.objects.get(id=the_userid)
        if the_userid:
            print ('user-id is')
            #register_model = register_model.objects.get(id=the_userid)
            context={
                "register_models": register_models
            }
            return render(request, 'profilee/edit_profile.html', context)

        else:
            context = {
                    'message': 'Please Login your account, may be your session time has expired' 
            }
            print ("heyyyyyyyyyyyyyyyy")
            
    
    except:
        context = {
                    'message': 'Please Login your account, may be your session time has expired' 
            }
        print ("hey last")
        
    return render(request, 'user_model/error.html', context)



def edit_address(request):
    request.session.set_expiry(300)
    print ('profile user_id is')
    try:
        the_userid = request.session['user_id']
        print (the_userid)
        user = register_model.objects.get(id=the_userid)
        print (user)
        add = user.address_set.all()
        if the_userid:
            print (the_userid)
            print ('address nedeche hai')
            #ad = address.objects.all()
            #print ad
            #address = address.objects.get(user=the_userid)
            print ("hey adres")
            print (add)
            context={
                "add" : add
            }
            return render(request, 'profilee/edit_address.html', context)
            
        else:
            print ("pass1")
            context = {
                    'message': 'Please Login your account, may be your session time has expired' 
                }
            
    except:
        print ("not in try")
        context = {
                    'message': 'Please Login your account, may be your session time has expired' 
                }

    return render(request, 'user_model/error.html', context)


def address_user(request):
    print ("hey")
    request.session.set_expiry(300)
    print ('profile user_id is')
    try:
        the_userid = request.session['user_id']
        print (the_userid)
        if the_userid:
            if request.method == 'POST':
                print ("post")
                userr = register_model.objects.get(id=the_userid)
                print (userr)
                user = userr.address_set.all()
                print (user)
                for i in user:
                    i.city = request.POST['city']
                    i.service_area = request.POST['service_area']
                    i.local_address = request.POST['local_address']
                    i.landmark = request.POST['landmark']
                    i.pin = request.POST['pin']
                    print (the_userid)
                    print (i.city)
                    print (i.service_area)
                    print (i.local_address)
                    print (i.landmark)
                    print (i.pin)
                    print ("address saved")
                    i.save()
                    
                return HttpResponseRedirect(reverse('edit_address'))
                print ("jiy")
            else:
                print ("no post")
        else:
            print ("no userid")
    except:
        print ("no_try")





def profile_user(request):
    print ("hey")
    request.session.set_expiry(300)
    print ('profile user_id is')
    try:
        the_userid = request.session['user_id']
        print (the_userid)
        if the_userid:
            if request.method == 'POST':
                print ("post")
                userr = register_model.objects.get(id=the_userid)
                print (userr)
                #user = userr.address_set.all()
                #print user
                username = request.POST['username']
                print ("username")
                #cond = register_model.objects.filter(username=username).exists()
                #print cond
                if not (register_model.objects.filter(username=username).exists()):
                    print ("hey if")
                    userr.username = request.POST['username']
                    userr.email = request.POST['email']
                    
                    
                    print (userr.email)
                    print (userr.username)
                    print ("account saved")
                    userr.save()
                else:
                    print ("else block") 

                return HttpResponseRedirect(reverse('edit_profile_page'))
                print ("jiy")
            else:
                print ("no post")
        else:
            print ("no userid")
    except:
        print ("no_try")



def profile_settings(request):
    print ("hey")
    request.session.set_expiry(300)
    print ('profile user_id is')
    try:
        the_userid = request.session['user_id']
        print (the_userid)
        if the_userid:
            if request.method == 'POST':
                print ("post")
                userr = register_model.objects.get(id=the_userid)
                print (userr)
                #user = userr.address_set.all()
                #print user
                #username = request.POST['firstname']
                #print "username"
                #cond = register_model.objects.filter(username=username).exists()
                #print cond
                if userr:
                    print ("hey if")
                    userr.firstname = request.POST['firstname']
                    userr.lastname = request.POST['lastname']
                    
                    
                    print (userr.firstname)
                    print (userr.lastname)
                    print ("account saved")
                    userr.save()
                else:
                    print ("else block") 

                return HttpResponseRedirect(reverse('edit_profile_page'))
                print ("jiy")
            else:
                print ("no post")
        else:
            print ("no userid")
    except:
        print ("no_try")



def profile_contact(request):
    print ("hey")
    request.session.set_expiry(300)
    print ('profile user_id is')
    try:
        the_userid = request.session['user_id']
        print (the_userid)
        if the_userid:
            if request.method == 'POST':
                print ("post")
                userr = register_model.objects.get(id=the_userid)
                print (userr)
                #user = userr.address_set.all()
                #print user
                #username = request.POST['firstname']
                #print "username"
                #cond = register_model.objects.filter(username=username).exists()
                #print cond
                if userr:
                    print ("hey if contact")
                    userr.contact_no = request.POST['contact_no']
                    
                    
                    
                    print (userr.contact_no)
                    print ("account saved")
                    userr.save()
                else:
                    print ("else block") 

                return HttpResponseRedirect(reverse('edit_profile_page'))
                print ("jiy")
            else:
                print ("no post")
        else:
            print ("no userid")
    except:
        print ("no_try")




def your_order(request):
    try:
        print ("orders")
        return render(request, 'profilee/your_orders.html')
    except:
        print ("no_order")