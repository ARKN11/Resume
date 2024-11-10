from django.shortcuts import render

# Create your views here.
def resume(request):
    context = {"name" : "Amirreza", "last_name" : "Kordnaeij", "date" : "2005", "city_of_birth":"Noshahr"}
    return render(request,"index.html", context)
