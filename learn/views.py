from django.shortcuts import render


# Create your views here.
def index(request):
    str = u"I'm learning Django."
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # return render(request, 'home_learn.html', {'string': str})
    return render(request, 'home_learn.html', {'list': list})
