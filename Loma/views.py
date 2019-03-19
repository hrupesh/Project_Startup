# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Loma_master
from django.shortcuts import render
import hashlib
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
# authenticate is for to autnticate username and paswd and login is for session_id
from django.shortcuts import render, redirect
#from django.views.generic import TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .tokens import account_activation_token
#from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from django.core.context_processors import csrf
from django.template import RequestContext
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
import hashlib
from django.contrib.auth.hashers import make_password , check_password

# Create your views here.

def Loma(request):
#    print request.session['user_id']
    context = {
        'Loma': 'Loma Registration'
    }

    return render(request, 'Loma/loma_home.html', context)

def loma_register(request):
    try:
        print ("in try Loma")
        #csrfContext = RequestContext(request)
        print ("hey")
        if request.method == 'POST':
            print ("register in postt")
            #form = SignupForm(request.POST or None)
            #if form.is_valid():
            #password = form.cleaned_data['password']
            #print password
            #form.password = make_password(password)
            #pswd = form.password
            #print pswd
            loma_password = request.POST['loma_password']
            #user = form.save(commit=False)
            #user.is_active = False
            #user.save()
            #userobj = form.cleaned_data
            #username = userobj['username']
            #email = userobj['email']
            #raw_password = userobj['password']
            user = Loma_master()
            user.loma_name = request.POST['loma_name']
            email = request.POST['loma_email']
            user.loma_permanent_Address = request.POST['loma_permanent_Address']    
            user.city = request.POST['city'] 
            user.Loma_mandi_name = request.POST['Loma_mandi_name'] 
            user.loma_zone = request.POST['loma_zone']
            user.loma_mobile_no = request.POST['loma_mobile_no']    
            user.loma_password = make_password(loma_password)    
            user.loma_email = email   
            print (email) 
            if not (Loma_master.objects.filter(loma_email=email).exists()):
                #user.password = make_password(password)
                print ("hey")
                pd = user.loma_password
        
             #   print "encrpted passwd is"
                print (pd)
                user.save()
                context = {
                    "message": "Activation link is sent to an email, Please activate your account"
                }
                return render(request, 'Loma/loma_register.html', context)
            else:
                context = {
                'message': "Username or email exist please try something different"
            }
                return render(request,'Loma/loma_register.html', context)
        else:
            print ("no_post but error")
            #del request.session['user_id']
            #del request.session['cart_id'] 
            return render(request, 'Loma/loma_register.html')
    except:
        print ('no post')
        #return render(request, 'user_model/error.html')    
        return render(request, 'Loma/loma_register.html')

#def make_password(password):
    #hash = hashlib.md5(password).hexdigest()
    #return hash


def activate(request, uidb64, token):
    try:
        #return HttpResponse('hey')
        #return HttpResponse(uidb64)
        #uidb64 = request.GET.get('uidb64')
        #return HttpResponse(uidb64)
        uid = force_text(urlsafe_base64_decode(uidb64))
        #return HttpResponse(uid)
        user = register_model.objects.get(pk=uid)


        if user:
            user.verified = True
            user.save()
        else:
            user.verified = False
            user.delete()
        #return HttpResponse(user)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        #return HttpResponse("heyyyyyyyyyyyyy")
        #user.is_active = True
        user.save()
        #login(request, user)
        return HttpResponseRedirect(reverse('user_login'))
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


#def check_password(password):
#    paswd = make_password(password)
#    return paswd


def loma_login(request):
    #context = {}
    #csrfContext = RequestContext(request)
    try:
        print ('try')
        if request.method == 'POST':
            print ("post")
            #con = {}
            username = request.POST['loma_email']
            print (username)
            password = (request.POST['loma_password'])
            print (password)
            #return HttpResponse(password)
            #user = register.objects.get(username=username)
            #return HttpResponse(user.password)
            try:
                passw = Loma_master.objects.get(loma_email=username)
                if passw.verified == True:
                    print ("hey u r in")
                    passwordd = passw.loma_password
                    print (passwordd)
                    passwd = check_password(password, passwordd)
                    print (passwd)
                    if passwd:
                        user = Loma_master.objects.get(loma_email=username , loma_password = passwordd)
                        print (user)
                    else:
                        print ("hey")
                        pass
                else:
                    print ("hey2")
                    pass
            except:
                print ("hey3")
                print ("error")

                
            #user = authenticate(username = username, password = password)
            #    print "error"
            #return HttpResponse(user)
            #return HttpResponse(user.username)
            if user:
                print(user)
                #return HttpResponse(user.id)
                #request.session['signupp_id'] = user
                user.is_active = True
                print (user.id)
                request.session['user_id'] = user.id
                new_id = user.id
                user.save()
                print (new_id)
                #print (request.session['user_id'])
                #return render(request,'S_W/error.html',{'username':username})
                #login(request, user)
                #uu = request.session['signupp_id']
                #return HttpResponse(uu)
                #request.session['email_confirmed'] = True 

                return HttpResponseRedirect(reverse('home'))
            #else:
                #context['error'] = "Error in Connection"
                #return render(request, 'S_W/error.html', context)
        else:
            #context[error] = "ERROR"
            #return HttpResponse("eeeoooorrrrooror")
            return render(request, 'user_model/login.html')
    except:
        print ("error3")
        context = {
            "message": "You are a new user, please register your account"
        }
        return render(request, 'Loma/loma_login.html', context)

def password_reset(request):
    #print "hey"
    if request.method == 'POST':
     #   print "problem"
        email = request.POST['email']
        try:
            users = register_model.objects.get(email=email)
            print (users)
        except:
            users = None

      #  print email

        if users is not None:
       #     print "password reset process"
            context = {
                "message" : "you are registered user"
            }
            user = users
            user.save()
        #    print user
            current_site = get_current_site(request)
            subject = 'rest password of your account.'
            message = render_to_string('user_model/password_reset_confirm.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            })
            to_email = email
            Email = EmailMessage(subject,message,to=[to_email])
            Email.send()
            request.session['user_id'] = user.id
            new_id = user.id
         #   print "session is"
          #  print new_id
            #return HttpResponse("Activation link is sent to an email, Please activate your account")
            #return render(request, 'S_W/confirmaton.html')
            context = {
                    "message": "Activation link is sent to an email, Please activate your account"
                }
            return render(request, 'user_model/password_reset.html', context)

        else:
           # print "Something wents wrong"
            #print "please try again with different ID"
            context = {
                "message" : "you are not registered user"
            }

    else:
        context = {
            "message" : "Please Enter your Email......"
        }
        #print "Sorry"

    return render(request, 'user_model/password_reset.html', context)


def password_reset_new(request):

        new_id = request.session['user_id']
        #print new_id
        if new_id is not None:
         #   print new_id
            if request.method == 'POST':
                try:
                    user = register_model.objects.get(id = new_id)
           #         print "User is"
          #          print user
                except:
                    user = None
                if user is not None:           
            #        print new_id
                    old_password = request.POST['old_password']
                    new_password = request.POST['new_password']
             #       print old_password
              #      print user.password
                    confirm_password = make_password(old_password)
                    #print password

                    if (old_password == new_password):
               #         print "passwords are same"
                        user.password = confirm_password
                #        print user.password
                        user.is_active = True
                        user.email_confirmed = True
                        user.save()
                        
                        context = {
                            "message": "your password is changed successfully",
                            "conn": True
                        }
                        

                        # now redirect a page on user_login and set a sleep time of 5 sec to redirect it automaticaly
                        # ye dekhna hai apan ko kal kii kesse
                        # ki back jaaane pr session expire ho jaaaye
                        # fir wapas login page pr redirect ho and new sessions bane
                        # 

                    else:
                 #       print "passswords are not same"
                        
                        context = {
                            "message": "your password is not changed, both passwords are not same",
                        }

                    
                
                else:
                  #  print "user is none"
                # print user
                # print user.firstname
                # print user.password
                # user.password = make_password(password)
                # user.save()
            
                # print user.password

                # print "hey"

                    context = {
                        "message": "your password is changed successfully"
                    }

            else:
            #    print "you are on secand path"

                context = {
                        "message": "you are on wrong path"
                    }

        else:
            context = {
                "message" : "Please reset your password"
            }

        return render(request, 'user_model/reset_pass.html', context)


def activate_password(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = register_model.objects.get(pk = uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        #return HttpResponse("heyyyyyyyyyyyyy")
        #user.is_active = True
        user.save()
        #login(request, user)
        return HttpResponseRedirect(reverse('password_reset_new'))

        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')

    else:
        return HttpResponse('Activation link is invalid!')

