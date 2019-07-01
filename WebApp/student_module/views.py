from django.shortcuts import render


def start(request):
    """Start page with a documentation.
    """
    # return render(request,"start.html")
    return render(request, "student_module/homepage.html")
