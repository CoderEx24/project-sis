from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from command.models import *
from .forms import *
from .models import *

@login_required(login_url='student:login')
def index(req):
    return render(req, 'student/home.html', {'user': req.user.student })

def logout(req):
    auth_logout(req)
    return redirect('student:index')

@login_required(login_url='student:login')
def courses(req):
    student = req.user.student
    current_semester = Semester.objects.last()

    passed_courses = student.enrollment_set.exclude(offering__semester=current_semester).filter(gpa__gte=1.7)
    passed_courses = list(map(lambda o: o.offering.course.id, passed_courses))
    registered_courses = student.enrollment_set.filter(offering__semester=current_semester)
    registered_courses = list(map(lambda o: o.offering.course.id, registered_courses))

    courses = Offering.objects.exclude(Q(course__pk__in=passed_courses) | Q(course__pk__in=registered_courses)) \
            if len(passed_courses) > 0 else Course.objects.exclude(course__pk__in=registered_courses)

    courses = courses.exclude(course__pk__in=registered_courses).filter(course__faculty=student.major.faculty,
                                                                        course__minimum_level__lte=student.level) \
                                                                .values_list('course', flat=True)
    courses = list(map(lambda obj: Course.object.get(pk=obj), courses))

    current_enrollments = student.enrollment_set.filter(offering__semester=current_semester)

    print(f'{courses=}')

    return render(req, 'student/courses.html', {'courses': courses, 'current_enrollments': current_enrollments})

@login_required(login_url='student:login')
def calender(req):
    student = req.user.student
    current_semester = Semester.objects.last()

    current_enrollments = student.enrollment_set.filter(offering__semester=current_semester)
    schedule = {f'{day[1]}': [None] * len(TIMESLOTS) for day in DAYS}

    for enrol in current_enrollments:
        timeslot = enrol.offering.timeslot_set.last()
        day = DAYS[timeslot.day - 1][1]
        if day not in schedule:
            schedule[day] = [timeslot]
            continue

        schedule[day][timeslot.timeslot - 1] = timeslot

    print(schedule)
    return render(req, 'student/calander.html', {'schedule': schedule})

@login_required(login_url='student:login')
def gpa_calculator(req):

    return render(req, 'student/gpa_calculator.html', {})

@login_required(login_url='student:login')
def payment(req):
    return render(req, 'student/payment.html', {})

@login_required(login_url='student:login')
def profile(req):
    student = req.user
    return render(req, 'student/profile.html', {'student': student})

@login_required(login_url='student:login')
def update_profile(req):
    return render(req, 'student/update.html', {})

@login_required(login_url='student:login')
def register_course(req, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    student = req.user.student

    offering = get_object_or_404(course.offering_set, semester=Semester.objects.last())

    new_enrollment = Enrollment.objects.create(student=student, offering=offering)
    new_enrollment.save()

    return redirect('student:courses')

@login_required(login_url='student:login')
def drop_course(req, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    student = req.user.student

    enrollment = get_object_or_404(student.enrollment_set,
                                   offering__semester=Semester.objects.last(),
                                   offering__course=course)
    enrollment.delete()

    return redirect('student:courses')

@login_required(login_url='student:login')
def withdraw_course(req, course_pk=None):
    student = req.user.student
    current_semester = Semester.objects.last()

    currently_withdrawn = WithdrawRequest.objects.filter(enrollment__offering__semester=current_semester,
                                                         enrollment__student=student) \
                                                 .values_list('enrollment__offering__course__pk', flat=True)
    print(currently_withdrawn)
    current_enrollments = student.enrollment_set.exclude(offering__course__pk__in=currently_withdrawn) \
                                                .filter(offering__semester=current_semester)
    print(current_enrollments)

    if course_pk is None:
        return render(req, 'student/withdraw.html', {'current_enrollments': current_enrollments})


    enrollment = get_object_or_404(student.enrollment_set,
                                   offering__course__pk=course_pk,
                                   offering__semester=current_semester)
    
    withdraw_request = WithdrawRequest.objects.create(enrollment=enrollment)
    withdraw_request.save()
    
    return redirect('student:withdraw_course')


@login_required(login_url='student:login')
def view_absense(req):
    student = req.user.student
    current_semester = Semester.objects.last()

    absense_records = Absense.objects.filter(enrollment__offering__semester=current_semester,
                                             enrollment__student=student) \
                                     .values_list('enrollment') \
                                     .annotate(absenses=Count('id')) \

    absense_records = list(map(lambda t: (Enrollment.objects.get(pk=t[0]), t[1]), absense_records))

    return render(req, 'student/absense.html', {'absense_records': absense_records})

@login_required(login_url='student:login')
def view_report(req):
    student = req.user.student
    enrollments = Enrollment.objects.filter(student=student)
    semesters = enrollments.values_list('offering__semester', flat=True) \
                           .distinct()

    semesters = {
        f'{Semester.objects.get(pk=pk)}': [
            *enrollments.filter(offering__semester__pk=pk)
        ]
        for pk in semesters

    }
    print(semesters)

    return render(req, 'student/report.html', {'semesters': semesters})

@login_required(login_url='student:login')
def view_results(req, semester_pk=None):
    student = req.user.student
    current_semester = Semester.objects.last()

    semesters = Enrollment.objects.filter(student=student) \
                                  .values_list('offering__semester', flat=True) \
                                  .distinct()

    semesters = Semester.objects.filter(Q(pk__in=semesters) & ~Q(pk=current_semester.pk))

    if semester_pk is None:
        return render(req, 'student/result.html', {'semesters': semesters})

    results = Enrollment.objects.filter(student=student,
                                        offering__semester__pk=semester_pk)

    return render(req, 'student/result.html', {'semesters': semesters, 'results': results})

