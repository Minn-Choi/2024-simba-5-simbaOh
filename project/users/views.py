from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Portfolio, Education, Experience, Project, Certification
from accounts.models import Profile
from main.models import Mentor
from community.models import Free, Move
from careers.models import Careerinfo, Careerprogram, Eduinfo, Ciapply, Cpapply, Eiapply

def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    profile, created = Profile.objects.get_or_create(user=user)
    portfolio, created = Portfolio.objects.get_or_create(user=user)
    following_count = user.mentor_followings.count()

    context = {
        'user': user,
        'profile': profile,
        'portfolio': portfolio,
        'following_count': following_count,
    }
    
    return render(request, 'users/mypage.html', context)

def follow_list(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'followings': user.mentor_followings.all()
    }
    return render(request, 'users/follow_list.html', context)

def bookmark(request, id):
    return render(request, 'users/bookmark.html')

def ciapply(request):
    ci_apply=Ciapply.objects.filter(user=request.user)
    return render(request, 'users/ciapply.html', {'ci_apply': ci_apply})

def cpapply(request):
    cp_apply=Cpapply.objects.filter(user=request.user)
    return render(request, 'users/cpapply.html', {'cp_apply': cp_apply})

def eiapply(request):
    ei_apply=Eiapply.objects.filter(user=request.user)
    return render(request, 'users/eiapply.html', {'ei_apply': ei_apply})

def edit_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        introduction = request.POST.get('introduction')
        education_list = request.POST.getlist('education')
        experience_list = request.POST.getlist('experience')
        projects_list = request.POST.getlist('projects')
        certifications_list = request.POST.getlist('certifications')

        portfolio.title = title
        portfolio.introduction = introduction

        portfolio.education.clear()
        for edu in education_list:
            education, created = Education.objects.get_or_create(name=edu)
            portfolio.education.add(education)

        portfolio.experience.clear()
        for exp in experience_list:
            experience, created = Experience.objects.get_or_create(name=exp)
            portfolio.experience.add(experience)

        portfolio.projects.clear()
        for proj in projects_list:
            project, created = Project.objects.get_or_create(name=proj)
            portfolio.projects.add(project)

        portfolio.certifications.clear()
        for cert in certifications_list:
            certification, created = Certification.objects.get_or_create(name=cert)
            portfolio.certifications.add(cert)

        portfolio.save()

        return redirect('users:mypage', id=request.user.id)

    return render(request, 'users/edit_portfolio.html', {'portfolio': portfolio})

def my_writing(request, id):
    user = User.objects.get(pk=id)
    username = request.user
    my_writes_free = Free.objects.filter(writer = username)
    my_writes_move = Move.objects.filter(writer = username)
    my_writes_careerinfo = Careerinfo.objects.filter(writer = username)
    context = {
        'user' : user,
        'my_writes_free' : my_writes_free,
        'my_writes_move' : my_writes_move,
        'my_writes_careerinfo' : my_writes_careerinfo
    }
    return render(request, 'users/my_writing.html', context)

def mentoring(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'menti_ship': user.menti_ship.all(),
    }
    return render(request, 'users/mentoring.html', context)

def menti_list(request, id):
    user = get_object_or_404(User, pk=id)
    mentor_ship_list = user.mentor_followings.all()
    menti_ship_list = set()

    for mentor in mentor_ship_list:
        menti_ship_list.update(mentor.mentor_ship.all())

    context = {
        'mentor_ship': mentor_ship_list,
        'menti_ship': menti_ship_list,
    }
    return render(request, 'users/menti_list.html', context)


def career_now(request, id):
    return render(request, 'users/career_now.html')



def cibm_list(request):
    user = request.user
    cibms = user.ci_bms.all()
    return render(request, 'users/cibm.html', {'cibms': cibms})

def cpbm_list(request):
    user = request.user
    cpbms = user.cp_bms.all()
    return render(request, 'users/cpbm.html', {'cpbms': cpbms})

def eibm_list(request):
    user = request.user
    eibms = user.ei_bms.all()
    return render(request, 'users/eibm.html', {'eibms': eibms})

