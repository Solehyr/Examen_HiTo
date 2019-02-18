from django.shortcuts import render

# Create your views here.
def index(request):
 if request.method == "POST":
  print(request.POST["content"])
 return render(request, "index.html")
