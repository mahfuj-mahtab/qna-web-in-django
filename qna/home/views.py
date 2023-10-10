
from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from home.models import OurUser
from questions.models import Questions
from category.models import Category
from answer.models import Answer
# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import send_mail
import random

def upload(request):
    if request.method == 'POST' and request.FILES['img']:
        pass






def home_view(request):
    user_email = OurUser.objects.all()
    
    user_list={}
    questions_info = Questions.objects.all()
    count=0

    for i in range(0,len(user_email)):
        user_info = {}
        c = 0
        for j in range(0,len(questions_info)):
            if(user_email[i].email == questions_info[j].u_email):
                c+=1
                if(count != 5):
                    if(c == 1):
                        user_info['name'] = user_email[i].name
                        user_info['img'] = user_email[i].img
                        user_info['user'] = user_email[i].user
                        user_list[i] = user_info
                        
                        count+=1
                    else:
                        break
                else:
                    break



    questions = Questions.objects.all()
    total_question = len(questions)
    answer = Answer.objects.all()
    total_answer = 0

    for i in range(0,total_question):
        for j in range(0,len(answer)):
            if questions[i].id == int(answer[j].Q_ID):
                total_answer=total_answer + 1   

    if(total_answer == 0 or total_question == 0):
        perchantage = 0
    else:
        perchantage = (total_answer / total_question) * 100
    question_dict = {}
    for i in range(len(questions)):
        dict = {}
        for j in range(len(user_email)):
            if(questions[i].u_email == user_email[j].email):
                dict['img'] = user_email[j].img
                dict['user'] = user_email[j].user
                dict['title'] = questions[i].title
                dict['details'] = questions[i].details
                dict['cat_name'] = questions[i].cat_name
                dict['id'] = questions[i].id
                dict['time'] = questions[i].time
                question_dict[i] = dict
                

    if request.session['active'] == True:
        print("session available")
        my_user = OurUser.objects.filter(email = request.session['0'])
        return render(request,"index.html",{"my_users" : my_user[0], "registered" : True,"question_dict" : question_dict,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list})
    else:
        print("sorry session not available")
        return render(request,"index.html",{"question_dict" : question_dict,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list})

def about(request):
    return render(request,"about.html")

def profile_view_other(request,u):
    user = OurUser.objects.all().filter(user = u)
    if(request.session['active'] == True and request.session['0'] == user[0].email):
        return HttpResponseRedirect("/profile")
    else:
        my_user = OurUser.objects.filter(email = request.session['0'])
        questions = Questions.objects.all().filter(u_email = user[0].email)
        answers = Answer.objects.all().filter(u_email = user[0].email)
 
        
        return render(request,"othersprofile.html",{"user": user[0],"questions" : questions,"my_users" : my_user[0], "registered" : True})



def search(request):
    user_email = OurUser.objects.all()
    print(user_email)
    
    user_list={}
    questions_info = Questions.objects.all()
    count=0
    for i in range(0,len(user_email)):
        user_info = {}
        c = 0
        for j in range(0,len(questions_info)):
            if(user_email[i].email == questions_info[j].u_email):
                c+=1
                if(count != 5):
                    if(c == 1):
                        print(user_email[i])
                        user_info['name'] = user_email[i].name
                        user_info['img'] = user_email[i].img
                        user_info['user'] = user_email[i].user
                        print(user_info)
                        user_list[i] = user_info
                        
                        count+=1
                    else:
                        break
                else:
                    break



    questions = Questions.objects.all()
    total_question = len(questions)
    answer = Answer.objects.all()
    total_answer = 0

    for i in range(0,total_question):
        for j in range(0,len(answer)):
            if questions[i].id == int(answer[j].Q_ID):
                total_answer=total_answer + 1       
    perchantage = (total_answer / total_question) * 100

    if(request.method == 'GET'):
        search = request.GET['search']
        question = Questions.objects.filter(title__contains = search)
        print(question)
        question_dict = {}
        for i in range(len(question)):
            dict = {}
            for j in range(len(user_email)):
                if(question[i].u_email == user_email[j].email):
                    dict['img'] = user_email[j].img
                    dict['user'] = user_email[j].user
                    dict['title'] = question[i].title
                    dict['details'] = question[i].details
                    dict['cat_name'] = question[i].cat_name
                    dict['id'] = question[i].id
                    dict['time'] = question[i].time
                    question_dict[i] = dict
        if request.session['active'] == True:

            my_user = OurUser.objects.filter(email = request.session['0'])
        return render(request,"search.html",{"my_users" : my_user[0], "registered" : True,"question_dict" : question_dict,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list,"search":search})
        

def profile_view_other_answer(request,u):
    user = OurUser.objects.all().filter(user = u)
    if(request.session['active'] == True and request.session['0'] == user[0].email):
        return HttpResponseRedirect("/profile")
    else:
        my_user = OurUser.objects.filter(email = request.session['0'])
        questions = Questions.objects.all().filter(u_email = user[0].email)
        answers = Answer.objects.all().filter(u_email = user[0].email)
        q=[]
        for i in range(len(answers)):
            q.append(answers[i].Q_ID)
            q2 = Questions.objects.filter(id = answers[i].Q_ID)
        q50 = Questions.objects.filter(id__in = q)
        return render(request,"othersprofile2.html",{"user": user[0],"questions" : questions,"answered_question" : q50,"my_users" : my_user[0], "registered" : True})    

def show_answer_view(request,id):
    user_email = OurUser.objects.all()
    
    user_list={}
    questions_info = Questions.objects.all()
    count=0
    for i in range(0,len(user_email)):
        user_info = {}
        c = 0
        for j in range(0,len(questions_info)):
            if(user_email[i].email == questions_info[j].u_email):
                c+=1
                if(count != 5):
                    if(c == 1):
                        print(user_email[i])
                        user_info['name'] = user_email[i].name
                        user_info['img'] = user_email[i].img
                        user_info['user'] = user_email[i].user
                        print(user_info)
                        user_list[i] = user_info
                        
                        count+=1
                    else:
                        break
                else:
                    break



    questions = Questions.objects.all()
    total_question = len(questions)
    answer = Answer.objects.all()
    total_answer = 0

    for i in range(0,total_question):
        for j in range(0,len(answer)):
            if questions[i].id == int(answer[j].Q_ID):
                total_answer=total_answer + 1       
    perchantage = (total_answer / total_question) * 100
    if(request.method == 'POST'):
        answer = request.POST['answer']
        a = Answer(Q_answer = answer, like = 0, dislike = 0,u_email = request.session['0'],Q_ID = id)
        a.save()
        return HttpResponseRedirect("/answer/{}".format(id))
    else:      
        ques = Questions.objects.filter(id = id)
        ans = Answer.objects.all().filter(Q_ID = id)
        user_info_collection ={}
        for i in range(0,len(ans)):
            user_info_dict= {}
            for j in range(0,len(user_email)):
                if(ans[i].u_email == user_email[j].email):
                    user_info_dict['name'] = user_email[j].name
                    user_info_dict['img'] = user_email[j].img
                    user_info_dict['user'] = user_email[j].user
                    user_info_dict['answer'] = ans[i].Q_answer
                user_info_collection[i] = user_info_dict

        question_user = OurUser.objects.filter(email = ques[0].u_email)
        # print("userrr", question_user)

        if request.session['active'] == True:
            print("session available")
            my_user = OurUser.objects.filter(email = request.session['0'])
            return render(request,'answer.html',{"question": ques[0],"my_users" : my_user[0], "registered" : True,"answers" : ans,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list,"info":user_info_collection,"question_user": question_user[0]})
        else:
            return render(request,'answer.html',{"question": ques[0],"answers" : ans,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list,"info":user_info_collection,"question_user": question_user[0]})


def search_view(request):
    return HttpResponse('Hello search page')

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

def recover(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        o = OurUser.objects.filter(email = email)
        if(len(o) == 1):
            r = random.randint(100000,999999)
            send_mail(
                'Password Recovery Email',
                'Here is the Code : {}'.format(r),
                'itstechnerd@gmail.com',
                ['{}'.format(email)],
                fail_silently=False,
            )
            request.session['verify'] = r
            request.session[0] = email
            return HttpResponseRedirect("/verify")
        else:
            print("sorry email not available")

    else:
        if(request.session['active'] == False):
            return render(request, "Recover.html")
        else:
            return HttpResponseRedirect("/")
def verify(request):
    if(request.method == 'POST'):
        n = request.POST['verify']
        if(int(request.session['verify']) == int(n)):
            print("yess success")
            request.session['verified'] = True
            return HttpResponseRedirect("/changed")
        else:
            print("failed")
    return render(request,"verify.html")
def pass_changed(request):
    if(request.session['verified'] == True):
        if(request.method == 'POST'):
            pass1 = request.POST['password1']
            pass2 = request.POST['password2']
            if(pass1 == pass2):
                pass3 = make_password(pass1)
                account = OurUser.objects.filter(email = request.session['0']).update(password = pass3)
                return HttpResponseRedirect("/login")
            else:
                print("password didnot match")
                return HttpResponseRedirect("/changed")
        else:
            return render(request,"password.html")
    else:
        print("not verified")
        return HttpResponseRedirect("/verify")
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

def pagination_view(request):
    return HttpResponse('Hello pagination  page')

def profile_view(request):
    if request.session['active'] == True:

        questions = Questions.objects.all().filter(u_email = request.session['0'])

        my_user = OurUser.objects.filter(email = request.session['0'])
      
        return render(request,"profile.html",{"my_users" : my_user[0], "registered" : True,"questions" : questions})
    else:
        print("sorry session not available")
    return render(request,'profile.html')

def profile_view_answer(request):
    if request.session['active'] == True:
        print("session available")
        questions = Questions.objects.all().filter(u_email = request.session['0'])
        answers = Answer.objects.all().filter(u_email = request.session['0'])
        q=[]
        for i in range(len(answers)):
            q.append(answers[i].Q_ID)
            q2 = Questions.objects.filter(id = answers[i].Q_ID)
        q50 = Questions.objects.filter(id__in = q)

        my_user = OurUser.objects.filter(email = request.session['0'])

        return render(request,"profile2.html",{"my_users" : my_user[0], "registered" : True,"questions" : questions,"answers" : answers, "answered_question" : q50})
    else:
        print("sorry session not available")
    return render(request,'profile.html')

def profileedit(request):
    if(request.method == 'POST'):
        fullname = request.POST['fullname']
        password = request.POST['password']
        bio = request.POST['bio']
        number = request.POST['phone']
        upload = request.FILES['img']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)

        if(len(fullname) != 0 and len(password)!= 0 and len(bio) !=0 and len(number) > 10 and len(upload.name) != 0 ):
            user = OurUser.objects.filter(email = request.session['0']).update(name = fullname,password = password,Bio = bio,phone_No = number,img=upload.name)
            return HttpResponseRedirect("/")
        elif(len(password) == 0):
            user = OurUser.objects.filter(email = request.session['0']).update(name = fullname,Bio = bio,phone_No = number,img=upload.name)
            return HttpResponseRedirect("/")
        else:
            print("please fillup all form")



    else:
        if(request.session['active'] == True):
            my_user = OurUser.objects.filter(email = request.session['0'])
            return render(request,"profile_edit.html",{"my_users" : my_user[0], "registered" : True})
        else:
            return HttpResponseRedirect("/")




def profile_setting_view(request):
    return HttpResponse('Hello profile setting page')


def category_view(request,cat):
    user_email = OurUser.objects.all()
    
    user_list={}
    questions_info = Questions.objects.all()
    count=0
    for i in range(0,len(user_email)):
        user_info = {}
        c = 0
        for j in range(0,len(questions_info)):
            if(user_email[i].email == questions_info[j].u_email):
                c+=1
                if(count != 5):
                    if(c == 1):
                        print(user_email[i])
                        user_info['name'] = user_email[i].name
                        user_info['img'] = user_email[i].img
                        user_info['user'] = user_email[i].user
                        print(user_info)
                        user_list[i] = user_info
                        
                        count+=1
                    else:
                        break
                else:
                    break


    questions = Questions.objects.all()
    total_question = len(questions)
    answer = Answer.objects.all()
    total_answer = 0

    for i in range(0,total_question):
        for j in range(0,len(answer)):
            if questions[i].id == int(answer[j].Q_ID):
                total_answer=total_answer + 1       
    perchantage = (total_answer / total_question) * 100

    question = Questions.objects.all().filter(cat_name = cat)
    question_dict = {}
    for i in range(len(question)):
        dict = {}
        for j in range(len(user_email)):
            if(question[i].u_email == user_email[j].email):
                dict['img'] = user_email[j].img
                dict['user'] = user_email[j].user
                dict['title'] = question[i].title
                dict['details'] = question[i].details
                dict['cat_name'] = question[i].cat_name
                dict['id'] = question[i].id
                dict['time'] = question[i].time
                question_dict[i] = dict

    if request.session['active'] == True:

        my_user = OurUser.objects.filter(email = request.session['0'])
        return render(request,"category.html",{"my_users" : my_user[0], "registered" : True,"question_dict" : question_dict,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list,"search":cat})

def tag_view(request):
    return HttpResponse('Hello tag page')

def message(request):
    return render(request,"message.html")