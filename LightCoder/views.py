from django.shortcuts import render


def main(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def contacts(request):
    return render(request, 'contacts.html')