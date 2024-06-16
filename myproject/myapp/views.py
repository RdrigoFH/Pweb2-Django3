from django.shortcuts import render

def index(request):
    context = {
        'numbers': [1, 2, 3, 4, 5],
        'words': ['apple', 'banana', 'cherry'],
        'users': [
            {'name': 'Alan', 'age': 25},
            {'name': 'Marcelo', 'age': 30},
            {'name': 'Alberto', 'age': 35}
        ]
    }
    return render(request, 'index.html', context)
