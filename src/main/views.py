from django.shortcuts import render

def index(request):
    data = {
        "title": "home",
        "values": ["some", "hello", "123"],
        "object": {
            "car": "bmw",
            "age": 2,
            "hobby": "cars"
        }
    }
    return render(request, "main/index.html", {"data": data})

def about(request):
    data = {
        "title": "about",
        "values": ["some", "hello", "123"],
        "object": {
            "car": "bmw",
            "age": 2,
            "hobby": "cars"
        }
    }
    return render(request, "main/about.html", {"data": data})

def contacts(request):
    data = {
        "title": "contacts",
        "values": ["some", "hello", "123"],
        "object": {
            "car": "bmw",
            "age": 2,
            "hobby": "cars"
        }
    }
    return render(request, "main/contacts.html", {"data": data})
