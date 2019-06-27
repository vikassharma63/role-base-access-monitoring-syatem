from django.shortcuts import render
from users.models import Logs,Daily,System
from datetime import date


def homefunc(request):
    return render(request,'users/home.html')


def loginfunc(request):
    return render(request,'users/login.html')

def regfunc(request):
    return render(request,'users/register.html')

def osepagefunc(request):
    return render(request,'users/osepage.html')

def prolefunc(request):
    return render(request,'users/prole.html')

def modpopfunc(request):
    return render(request,'users/modpop.html')

def syspopfunc(request):
    return render(request,'users/syspop.html')

def rcdviewfunc(request):
    return render(request,'users/rcdview.html')

def registrationfunc(request):
    if request.method=="POST":
        uname=request.POST.get('username','')
        pssword = request.POST.get("psw",'')
        repssword = request.POST.get("psw-repeat", '')
        rol = request.POST.get("role",'')
        l=Logs(u_name=uname,passwd=pssword,role=rol,repasswd=repssword)
        l.save()
    return render(request,"users/login.html")

def logsfunc(request):
    if request.method=="POST":
        name=request.POST.get("uname")
        pssword = request.POST.get("psw")
        rol = request.POST.get("role")
        print(name)
        print(pssword)
        print(rol)
        l=Logs.objects.get(u_name=name,passwd=pssword,role=rol)
        print(l.role)
        if l.role=="OSE":
            return render(request, "users/osepage.html",{'list1':l})
        elif l.role=="PL":
            return render(request, "users/prole.html")

def osefunc(request):
    if request.method == "POST":
        sname = str(request.POST.get('drpsys', ''))
        mname = str(request.POST.get("drpmod", ''))
        status = str(request.POST.get("status", ''))
        rmark = str(request.POST.get("remark", ''))
        l = Daily(s_name = sname, m_name = mname, status = status, remark = rmark)
        l.save()

        return render(request,"users/osepage.html")


def sysfillfunc(request):
    if request.method=="POST":
        sname=request.POST.get('sysname','')
        stype = request.POST.get("systype",'')
        swork = request.POST.get("syswork", '')
        l=System(s_name=sname,s_type=stype,s_work=swork)
        l.save()
    return render(request,"users/syspop.html")

'''
def modfillfunc(request):
    if request.method=="POST":
        mname=request.POST.get('modname','')
        mtype= request.POST.get("modtype",'')
        mwork = request.POST.get("modwork", '')
        rel_sys = str(request.POST.get("rel_sys",''))
        l=Logs(m_name=modname,m_type=modtype,m_work=modwork,System=rel_sys)
        l.save()
    return render(request,"users/modpop.html")
'''


