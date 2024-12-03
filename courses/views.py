from django.shortcuts import render
from .models import Course


def course_list(request):
    title = request.GET.get('title')
    description = request.GET.get('description')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    number_of_max_students = request.GET.get('number_of_max_students')

    if title is not None and description is not None and start_date is not None and end_date is not None and end_date is not None and number_of_max_students is not None :
        Course.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            number_of_max_students=number_of_max_students,
        )
    courses = Course.objects.all()
    ctx = {'courses': courses }
    return render(request, 'courses/courses_list.html', ctx)