from django.shortcuts import render

def index(request):
    data = {
        "title": "main",
        "values": ["some", "hello", "123"],
        "object": {
            "car": "bmw",
            "age": 2,
            "hobby": "cars"
        }
    }
    return render(request, "main/index.html", data)

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
    return render(request, "main/about.html", data)

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
    return render(request, "main/contacts.html", data)
