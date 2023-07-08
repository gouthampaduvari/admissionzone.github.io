from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from admissionapp.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.conf.urls.static import static
from django.core.mail import send_mail
from django.http import JsonResponse
import random
# Create your views here.

from .models import *


def index(request):
    reviews = Review.objects.all()
    return render(request,'home.html',{'reviews':reviews})

def reg(request):
    return render(request,'reg.html')



def college_register(request):
    if request.method=="POST":
        caname=request.POST.get('caname')
        caemail=request.POST.get('caemail')
        capswd=request.POST.get('capswd')
        cacpswd=request.POST.get('cacpswd')
        uexist = User.objects.filter(username=caname)
        if uexist :
            # messages.warning(request,"The entered email is already registerd")
            return render(request,'reg.html',{"umessagess":'1',})
        exist = User.objects.filter(email=caemail)
        if exist :
            # messages.warning(request,"The entered email is already registerd")
            return render(request,'reg.html',{"messagess":'1',})
        if cacpswd!=cacpswd:
            return render(request,'reg.html',{"emessagess":'1',})
        college=User.objects.create_user(username=caname,email=caemail,password=capswd,is_college=True)
        college.save()
        return redirect('/login')
    return render(request,'reg.html')

def student_register(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        semail=request.POST.get('semail')
        spswd=request.POST.get('spswd')
        scpswd=request.POST.get('scpswd')
        uexist = User.objects.filter(username=sname)
        if uexist :
            # messages.warning(request,"The entered email is already registerd")
            return render(request,'reg.html',{"umessagess":'1',})
        exist = User.objects.filter(email=semail)
        if exist :
            # messages.warning(request,"The entered email is already registerd")
            return render(request,'reg.html',{"messagess":'1',})
        if spswd!=scpswd:
            return render(request,'reg.html',{"emessagess":'1',})
        student=User.objects.create_user(username=sname,email=semail,password=spswd,is_student=True,status='notapplied')
        student.save()
        return redirect('/login')
    return render(request,'reg.html')



def logins(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass') 
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None and user.is_active:
            login(request,user)
            if user.is_superuser:
                return redirect('admin_dashboard.html')
            elif user.is_student:
                return redirect('student_dashboard.html')
            elif user.is_college:
                return redirect('college_dashboard.html')
            return redirect('/student_dashboard')
        else:
            messages.error(request,'invalid password')

    
    return render(request,'login.html')

@login_required
def college_dashboard(request):
    return render(request,'college_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request,'student_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')
    

    
def about(request):
    return render(request,'aboutus.html')


def terms(request):
    return render(request,'terms.html')

def dashboard(request):
    return render(request,'dashboard.html')

def logouts(request):
    logout(request)
    return redirect('login')

def student_profile(request):
    if request.user.is_authenticated:
        return render(request,'student_profile.html')
    else:
        return redirect('/login')
def college_profile(request):
    if request.user.is_authenticated:
        return render(request,'college_profile.html')
    else:
        return redirect('/login')
def admin_profile(request):
    if request.user.is_authenticated:
        return render(request,'admin_profile.html')
    else:
        return redirect('/login')
    
def apply(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname')
        # middle_name=request.POST.get('middlename')
        last_name=request.POST.get('lastname')
        father_name=request.POST.get('fathername')
        mother_name=request.POST.get('mothername')
        date_of_birth=request.POST.get('dateofbirth')
        gender=request.POST.get('gender')
        phone_number=request.POST.get('phone')
        alt_number=request.POST.get('alt')
        address=request.POST.get('address')
        sslc_percentage=request.POST.get('sslcpercent')
        sslc_school=request.POST.get('sslcschool')
        puc_percentage=request.POST.get('pupercent')
        puc_college=request.POST.get('pucollege')
        college=request.POST.get('selcol')
        selected_course=request.POST.get('selcour')
        photo=request.FILES.get('photo')
        user=request.user
        us=User.objects.get(id=request.user.id)
        us.status='pending'
        us.save()
        student=Student(user=request.user,username=user,first_name=first_name,last_name=last_name,father_name=father_name,mother_name=mother_name,date_of_birth=date_of_birth,gender=gender,phone_number=phone_number,alt_number=alt_number,address=address,sslc_percentage=sslc_percentage,sslc_school=sslc_school,puc_percentage=puc_percentage,puc_college=puc_college,college=college,selected_course=selected_course,photo=photo)  
        student.save()
        col=User.objects.get(username=college)
        application=Application(applied_by=request.user,applied_to=col,status=False,std=student)
        application.save()

        user = request.user
        has_applied = Application.objects.filter(applied_by=request.user)
        applied=[]
        clgs=[]
        notapplied=[]
        for col in has_applied:
            clg=col.applied_to
            applied.append(clg.username)

        print(applied)

        # colgs=College.objects.all()
        colgs=User.objects.filter(is_college=True,status='accept')
        for c in colgs:
            clgs.append(c.username)

        print(clgs)

        for a in clgs:
            if a not in applied:
                notapplied.append(a)


        return render(request, 'apply.html', {'clg': notapplied,'messagess':'sucessfully Apllied...!'})      
    user = request.user
    has_applied = Application.objects.filter(applied_by=request.user)
    applied=[]
    clgs=[]
    notapplied=[]
    for col in has_applied:
        clg=col.applied_to
        applied.append(clg.username)

    print(applied)

    # colgs=College.objects.all()
    colgs=User.objects.filter(is_college=True,status='accept')
    for c in colgs:
        clgs.append(c.username)

    print(clgs)

    for a in clgs:
        if a not in applied:
            notapplied.append(a)


    return render(request, 'apply.html', {'clg': notapplied})

    # return render(request,'apply.html')

def applydone(request):
    return render(request,'applydone.html')

def c_apply(request):
    if request.method=='POST':
        college_name=request.POST.get('colname')
        place=request.POST.get('place')
        pincode=request.POST.get('pincode')
        college_strength=request.POST.get('strength')
        inaugration_date=request.POST.get('idate')
        naac_grade=request.POST.get('grade')
        principal_phone=request.POST.get('phone')
        # alt_phone=request.POST.get('alt')
        address=request.POST.get('address')
        coursess=request.POST.getlist('courses_available')
        courses=' '.join(coursess)
        photo=request.FILES.get('photo')
        uexist =College.objects.filter(username=request.user)
        if uexist :
            # messages.warning(request,"The entered email is already registerd")
           return render(request,'c_apply.html',{'messagess':'College with this name alredy applied',})
        college=College(clg=request.user,username=college_name,college_name=college_name,place=place,pincode=pincode,college_strength=college_strength,inaugration_date=inaugration_date,naac_grade=naac_grade,principal_phone=principal_phone,address=address,courses_available=courses,photo=photo)
        college.save()
        us=User.objects.get(id=request.user.id)
        us.status='notapplied'
        us.save()
        return render(request,'c_apply.html',{'messagess':'sucessfully Requested...!',})
        #return redirect('/applydone')
    return render(request,'c_apply.html')


def viewall(request):
    pass
    return render(request,'viewall.html')


    # otp
import random
global otp
global fuser
def forgetpass(request):
    global otp
    global fuser
    if request.method=="POST":
        if request.POST.get("get_otp"):
            email=request.POST['email']
            user=User.objects.filter(email=email)
            print(email)
            print(user)
            fuser=user[0]
            
            if user:
                otp=str(random.randrange(10000,99999))
                send_mail('OTP to Reset Password','OTP= '+otp+' username= '+fuser.username,'settings.EMAIL_HOST_USER',[fuser.email],fail_silently=False) 
                return render(request,'enter_otp.html')
            else:
                messages.info(request,"no user found with that email")
                return render(request,'forgot_password.html')
        elif request.POST.get("check_otp"):
            entered_otp=request.POST['otp']
            if entered_otp==otp:
                return render(request,'password_reset.html')
            else:
                messages.info(request,"enter otp is wrong")
                return render(request,'enter_otp.html')
        elif request.POST.get("change_pass"):
            user=fuser
            print(user)
            password=request.POST['password']
            confirm_pass=request.POST['confirm_password']
            if password != confirm_pass:
                messages.info(request,"The first and second password differ")
                return render(request,'password_reset.html')
            else:
                print(user)
                print(password)
                user.set_password(password)
                user.save()
                return render(request,'login.html')
    else:
        return render(request,'forgot_password.html')

def college_list(request):
    # students_nitm=Student.objects.filter(college="National Institute of Technology, Mangaluru.")
    # students_jnub=Student.objects.filter(college="Jawaharlal Nehru University, Bengaluru.")
    # students_sacm=Student.objects.filter(college="St Aloysious College, Mangaluru.")
    # students_pcu=Student.objects.filter(college="Presidency College, Udupi.")
    # students_sitt=Student.objects.filter(college="Siddaganga Institute of Technology,Tumkur.")
    # context={'students_nitm':students_nitm,'students_jnub':students_jnub,'students_sacm':students_sacm,'students_pcu':students_pcu,'students_sitt':students_sitt}   
    
    clg=User.objects.filter(is_college=True,status='accept')
    stud=Application.objects.filter(status=True)
    print(stud)

    students=[]
    data={}
    for c in clg:
        students=[]
        for s in stud:
            if c.id == s.applied_to_id:
                students.append(Student.objects.get(user=s.applied_by,college=c.username))
        data[c.username]=students
        

    print(data)
    
    return render(request,'college_list.html',{'data':data,})
    

def status(request):
    ap=Application.objects.filter(applied_by=request.user)
    # st=request.user.status
    return render(request,'status.html',{'status':ap})

def ratings(request):
    if request.method=='POST':
        #username=request.POST.get('username')
        username=request.user.username
        rating=request.POST.get('rating')
        feedback=request.POST.get('feedback')
       
        review=Review(username=username,rating=rating,feedback=feedback)
        review.save()
        return render(request,'ratings.html',{'messagess':'Your review was successfully recieved...!',})
    return render(request,'ratings.html')
    
def student_list(request):
    col=request.user
    st=[]
    sts=[]
    students=Application.objects.filter(applied_to=col,status=True)
    stud=Student.objects.filter(college=request.user.username)
    for i in students:
        for j in stud:
            if i.applied_by == j.user:
                sts.append(j)
    
    print(sts)
    
    return render(request, 'student_list.html', {'slist': sts})

def applicants(request):
    if request.method == "POST":
        if "accept" in request.POST:
            id = request.POST.get("accept")
            data = Application.objects.get(id=id)
            data.status=True
            data.save()
            print(request.user.username)
            applicant = Application.objects.filter(applied_to=request.user,status=False,rej=False)

            applied=[]
            for a in applicant:
                applied.append(a)

            # Student.objects.filter(college=request.user.username,user__status='pending')
            if applicant:
                print("pass")
                return render(request, "view_applicants.html", {'applicant': applied,'messagess':'Student accepted'})
            else:
                noapply = "No applicants"
                print("fail")
                return render(request, "view_applicants.html", {'noapply': noapply ,'messagess':'Student accepted'})
            
        elif "reject" in request.POST:
            id = request.POST.get("reject")
            print(id)
            stud=Application.objects.get(id=id)
            # datu = Application.objects.get(applied_by=stud.applied_by,applied_to=request.user)
            # datu.rej=True
            stud.rej=True
            stud.save()
            data = Student.objects.get(user=stud.applied_by,college=request.user.username)
            data.delete()
            # datu.save()
            print(request.user.username)
            applicant = Application.objects.filter(applied_to=request.user,status=False,rej=False)

            applied=[]
            for a in applicant:
                applied.append(a)

            # Student.objects.filter(college=request.user.username,user__status='pending')
            if applicant:
                print("pass")
                return render(request, "view_applicants.html", {'applicant': applied,'messagess':'Student rejected'})
            else:
                if "reject" in request.POST:
                    return render(request, "view_applicants.html", {'applicant': applied,'messagess':'Student rejected','noapply': "No Applicaton"}) 
                noapply = "No applicants"
                print("fail")
                return render(request, "view_applicants.html", {'noapply': noapply})

    print(request.user.username)
    applicant = Application.objects.filter(applied_to=request.user,status=False,rej=False)

    applied=[]
    for a in applicant:
        applied.append(a)

    # Student.objects.filter(college=request.user.username,user__status='pending')
    if applicant:
        print("pass")
        return render(request, "view_applicants.html", {'applicant': applied})
    else:
        noapply = "No applicants"
        print("fail")
        return render(request, "view_applicants.html", {'noapply': noapply})
    

def get_available_courses(request): 
    selected_college = request.GET.get('selcol')
    print(selected_college)
    # Retrieve the college object based on the selected college name
    college = College.objects.get(college_name=selected_college)

    # Retrieve the available courses for the selected college
    available_courses = college.courses_available.split(' ')

    return JsonResponse(available_courses, safe=False)

def manage_course(request):
    colleges = College.objects.filter(username=request.user)
    return render(request,'manage_course.html',{'colleges': colleges})

def add_course(request, college_id):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        if course_name:
            college = College.objects.get(id=college_id)
            available_courses = college.courses_available.split(' ')

            if course_name not in available_courses:
                available_courses.append(course_name)
                college.courses_available = ' '.join(available_courses)
                college.save()
                error_message = "Added new course"
                colleges = College.objects.filter(username=request.user)
                return render(request, 'manage_course.html', {'colleges': colleges, 'error_message': error_message})
            else:
                error_message = "Course already exists."
        else:
            error_message = "Course name is required."
    else:
        error_message = "Invalid request method."

    colleges = College.objects.filter(username=request.user)
    return render(request, 'manage_course.html', {'colleges': colleges, 'error_message': error_message})

def delete_course(request, college_id):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        if course_name:
            college = College.objects.get(id=college_id)
            available_courses = college.courses_available.split(' ')

            if course_name in available_courses:
                available_courses.remove(course_name)
                college.courses_available = ' '.join(available_courses)
                college.save()
                error_message = "Course Deleted"
                colleges = College.objects.filter(username=request.user)
                return render(request, 'manage_course.html', {'colleges': colleges, 'error_message': error_message})
            else:
                error_message = "Course does not exist."
        else:
            error_message = "Course name is required."
    else:
        error_message = "Invalid request method."

    colleges = College.objects.filter(username=request.user)
    return render(request, 'manage_course.html', {'colleges': colleges, 'error_message': error_message})

def notifications(request):
    notifications = Notification.objects.all().order_by('-timestamp')
    print(notifications)
    return render(request, 'notification.html', {'notifications': notifications})

def add_notification(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Notification.objects.create(message=message)
            # return redirect('notification')
            return render(request,'add_notification.html',{'messagess':'new notification successfully added...!',})
    return render(request,'add_notification.html')


def tieup_status(request):
    return render(request, 'tieup_status.html')

def college_request(request):
    msg=""
    if request.method == "POST":
        if "accept" in request.POST:
            id = request.POST.get("accept")
            clgs=College.objects.get(id=id)
            clgs.clg.status="accept"
            clgs.clg.save()
            # stud=User.objects.get(id=id)
            # stud.status="accept"
            # stud.save()
            msg="accepted the college"
            
        elif "reject" in request.POST:
            id = request.POST.get("reject")
            print(id)
            clgs=College.objects.get(id=id)
            clgs.clg.status="reject"
            clgs.clg.save()
            # clgs.save()
            clgs.delete()
            # stud=User.objects.get(id=id)
            # stud.status='reject'
            # stud.save()
            # clg=College.objects.get(username=stud.username)
            # clg.delete() 
            msg="rejected the college"

    clgs=College.objects.filter(clg__status="notapplied")
    return render(request, "college_request.html",{'applicant':clgs,'messagess':msg,})


def edit_profile(request):
    if request.method=="POST":
        pf=request.FILES.get("s-profile")
        
        phone=request.POST.get("c-no")
        email=request.POST.get("s-add")
        user=User.objects.get(id=request.user.id)
        user.photo=pf
        
        user.phone=phone
        user.email=email
        user.save()
        print("saved")
        #return render(request,"student_profile.html")
        return redirect("student_profile")
    return render(request,"edit_profile.html")