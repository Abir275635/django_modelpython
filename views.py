from django.shortcuts import render
from myApp.models import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

# Teacher View with Filtering
def teacher(request):
    teachers = teacherModel.objects.all()
    
    # Get filter parameters from request
    subject_filter = request.GET.get('subject')
    district_filter = request.GET.get('district')
    date_filter = request.GET.get('date')
    filter_type = request.GET.get('filter_type')
    
    # Apply filters based on filter type
    if filter_type == 'subject' and subject_filter:
        teachers = teachers.filter(subject=subject_filter)
    
    elif filter_type == 'district' and district_filter:
        teachers = teachers.filter(district=district_filter)
    
    elif filter_type == 'date' and date_filter:
        # Filter by year of joining date
        teachers = teachers.filter(joining_Date__year=date_filter)
    
    context = {
        'teachers': teachers
    }
    
    return render(request, "teacherPage.html", context)

# Student View with Filtering
def student(request):
    students = studentModel.objects.all()
    
    # Get filter parameters from request
    name_filter = request.GET.get('name')
    department_filter = request.GET.get('department')
    city_filter = request.GET.get('city')
    filter_type = request.GET.get('filter_type')
    
    # Apply filters based on filter type
    if filter_type == 'name' and name_filter:
        students = students.filter(name__icontains=name_filter)
    
    elif filter_type == 'department' and department_filter:
        students = students.filter(department=department_filter)
    
    elif filter_type == 'city' and city_filter:
        students = students.filter(city=city_filter)
    
    context = {
        'students': students
    }
    
    return render(request, "studentPage.html", context)

# Dashboard/Home View
def dashboard(request):
    # Get counts for dashboard
    total_teachers = teacherModel.objects.count()
    total_students = studentModel.objects.count()
    
    # Get recent teachers and students
    recent_teachers = teacherModel.objects.all().order_by('-joining_Date')[:5]
    recent_students = studentModel.objects.all().order_by('-joining_Date')[:5]
    
    context = {
        'total_teachers': total_teachers,
        'total_students': total_students,
        'recent_teachers': recent_teachers,
        'recent_students': recent_students,
    }
    
    return render(request, "dashboard.html", context)