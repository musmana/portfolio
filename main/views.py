from django.shortcuts import render

def home(request):
    skills = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django']
    return render(request, 'home.html', {'skills': skills})

def about(request):
    bio = "I’m a passionate web developer specializing in building interactive websites using Django and React."
    return render(request, 'about.html', {'bio': bio})

def projects(request):
    projects = [
        {'title': 'Portfolio Website', 'description': 'A personal portfolio built with Django.'},
        {'title': 'E-Commerce App', 'description': 'Online store built using Django and Stripe integration.'},
        {'title': 'Blog Platform', 'description': 'Dynamic blog with user authentication and CRUD features.'},
    ]
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    contact_info = {
        'email': 'youremail@example.com',
        'phone': '+91 9876543210'
    }
    return render(request, 'contact.html', {'contact_info': contact_info})
