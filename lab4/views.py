from django.shortcuts import render

def home(request):
    pages = [
        {'name': 'view1', 'title': 'Вюшка 1'},
        {'name': 'view2', 'title': 'Вюшка 2'},
        {'name': 'view3', 'title': 'Вюшка 3'},
        {'name': 'view4', 'title': 'Вюшка 4'},
        {'name': 'view5', 'title': 'Вюшка 5'},
    ]
    return render(request, 'lab4/home.html', {'pages': pages, 'title': 'Головна сторінка'})

def view1(request):
    return render(request, 'lab4/view.html', {'title': 'Вюшка 1'})

def view2(request):
    return render(request, 'lab4/view.html', {'title': 'Вюшка 2'})

def view3(request):
    return render(request, 'lab4/view.html', {'title': 'Вюшка 3'})

def view4(request):
    return render(request, 'lab4/view.html', {'title': 'Вюшка 4'})

def view5(request):
    return render(request, 'lab4/view.html', {'title': 'Вюшка 5'})



