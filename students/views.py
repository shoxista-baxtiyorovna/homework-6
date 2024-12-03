from django.shortcuts import render

from .models import Student
def student_list(request):
    first_name = request.GET.get('firstName')
    last_name = request.GET.get('lastName')
    email = request.GET.get('email')
    date_of_birthday = request.GET.get('date_of_birthday')
    gender = request.GET.get('gender')
    address = request.GET.get('address')
    print(first_name, last_name, email, date_of_birthday, gender, address)
    if (first_name is not None
            and last_name is not None
            and email is not None
            and date_of_birthday is not None
            and gender is not None
            and address is not None):
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birthday,
            gender=gender,
            address=address
        )
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/student_list.html', ctx)
