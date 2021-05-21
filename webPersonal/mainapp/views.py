from django.shortcuts import render

# Create your views here.




def about(request):
    return render(request,'template/about.html')

def contact(request):
    return render(request,'template/contact.html')