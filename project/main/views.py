from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Mentor



def intro(request):
    return render(request, 'main/intro.html')

def first_screen(request):
    return render(request, 'main/first_screen.html')

def mainpage(request):
    return render(request, 'main/mainpage.html')

def mentor_start(request):
    return render(request, 'main/mentor_start.html')

def mentor_list(request):
    mentors = Mentor.objects.all()
    return render(request, 'main/mentor_list.html', {'mentors' : mentors})

def mentor_enroll(request):
    return render(request, 'main/mentor_enroll.html')

def mentor_info(request, id):
    mentor = get_object_or_404(Mentor, pk = id)
    return render(request, 'main/mentor_info.html', {'mentor' : mentor})

@login_required
def mentor_enroll(request):
    if request.method == 'POST':
        mentor_company = request.POST.get('mentor_company', '')
        mentor_dept = request.POST.get('mentor_dept', '')
        mentor_work = request.POST.get('mentor_work', '')

        # Mentor 객체가 없으면 생성
        if not hasattr(request.user, 'mentor'):
            mentor = Mentor.objects.create(
                user=request.user,
                mentor_company=mentor_company,
                mentor_dept=mentor_dept,
                mentor_work=mentor_work,
                mentor_at=timezone.now()
            )
        else:
            mentor = request.user.mentor
            mentor.mentor_company = mentor_company
            mentor.mentor_dept = mentor_dept
            mentor.mentor_work = mentor_work
            mentor.save()
            request.session['mentor_id'] = mentor.id
        return redirect('main:mentor-enroll2')
    return render(request, 'main/mentor_enroll.html')

@login_required
def mentor_enroll2(request):
    if request.method == 'POST':
        mentor_summary = request.POST.get('mentor_summary', '')
        mentor_info = request.POST.get('mentor_info', '')
        mentor_career = request.POST.get('mentor_career', '')
        mentor_certificate = request.POST.get('mentor_certificate', '')

        mentor_id = request.session.get('mentor_id')
        if mentor_id:
            mentor = Mentor.objects.get(id=mentor_id)
            mentor.mentor_summary = mentor_summary
            mentor.mentor_info = mentor_info
            mentor.mentor_career = mentor_career
            mentor.mentor_certificate = mentor_certificate
            mentor.save()
        return redirect('main:mentor-enroll3')
    return render(request, 'main/mentor_enroll2.html')

@login_required
def mentor_enroll3(request):
    if request.method == 'POST':
        mentor_id_card = request.FILES.get('mentor_id_card')
        mentor_name_card = request.FILES.get('mentor_name_card')

        mentor_id = request.session.get('mentor_id')
        if mentor_id:
            mentor = Mentor.objects.get(id=mentor_id)
            if mentor_id_card:
                mentor.mentor_id_card = mentor_id_card
            if mentor_name_card:
                mentor.mentor_name_card = mentor_name_card
            mentor.save()
        return redirect('main:mentor-list')
    return render(request, 'main/mentor_enroll3.html')

def mentor_ask(request):
    return render(request, 'main/mentor_ask.html')
