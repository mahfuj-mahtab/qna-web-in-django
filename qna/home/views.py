from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from home.models import OurUser
from django.contrib.auth.hashers import make_password,check_password
from questions.models import Questions


def home(request):
    try:
        if(request.session['active'] == True):            
            return render(request,"index.html",{'loged_in' : True})
        else:
            return render(request,"index.html",{'loged_in' : False})

    except:
            return render(request,"index.html",{'loged_in' : False})

def ask_view(request):
    return render(request,'askquestion.html')

        

def signup_view(request):
    if(request.method == "POST"):
        name = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        passw = make_password(password)
        emailcount = OurUser.objects.all().filter(email = email)

        if(len(emailcount) > 0):
            print("More than one email")
        else:
            usercount = OurUser.objects.all().filter(user = username)
            if(len(usercount) > 0):
                print("more than one user name")
            else:
                if(len(password) >= 8):
                    user = OurUser(name = name, email = email,password = passw,user = username,Num_of_followers = 0,Num_of_following = 0,img = "default.jpg",phone_No = 0,Bio = '')
                    user.save()
                    return HttpResponseRedirect("/")
                else:
                    print("password is less than 8 char")
       
        
        
    else:
        return render(request, "Register.html")
    
def login(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        ecount = OurUser.objects.all().filter(email = email)
        if(len(ecount) == 1):
            if(check_password(password,ecount[0].password) == True):
                print("login")
                request.session[0] = email
                request.session['active'] = True
                return HttpResponseRedirect("/")

            else:
                print("not login")
                return HttpResponseRedirect("/login")

        else:
            print("email not available")
            return HttpResponseRedirect("/login")

    else:
        return render(request, "Login.html")
    
def logout(request):
    del request.session['0']
    request.session['active'] = False
    request.session.modified = True
    return HttpResponseRedirect("/")

def profile_view(request):
    if request.session['active'] == True:

        questions = Questions.objects.all().filter(u_email = request.session['0'])

        my_user = OurUser.objects.filter(email = request.session['0'])
      
        return render(request,"profile.html",{"my_users" : my_user[0], "registered" : True,"questions" : questions})
    else:
        print("sorry session not available")
    return render(request,'profile.html')
    
def ask_question_view(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        details = request.POST['details']
        category = request.POST['category']
        q = Questions(title = title , details = details,u_email = request.session['0'],cat_name = category)
        q.save()
        return HttpResponseRedirect("/")
    else:
        if request.session['active'] == True:
            print("session available")
            category = Category.objects.all()
            my_user = OurUser.objects.filter(email = request.session['0'])
            return render(request,"askquestion.html",{"my_users" : my_user[0], "registered" : True, "category" : category})
        else:
            print("sorry session not available")
            return HttpResponseRedirect("/login")
