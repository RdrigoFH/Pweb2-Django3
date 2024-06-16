from django.shortcuts import render

def index(request):
    numbers = [1, 2, 3, 4, 5]
    words = ['apple', 'banana', 'cherry']
    users = [
        {'name': 'Alice', 'age': 25, 'is_adult': True},
        {'name': 'Bob', 'age': 17, 'is_adult': False},
        {'name': 'Charlie', 'age': 30, 'is_adult': True}
    ]
    
    context = {
        'numbers': numbers,
        'words': words,
        'users': users,
        'current_date': '2024-06-15',
        'currency': 1500,
    }
    return render(request, 'index.html', context)
