from django.shortcuts import render

from .forms import PropertyForm
from .models import Property


def index(request):
    return render(request, 'App/index.html')


def buy(request):
    return render(request, 'App/buy.html')


def rent(request):
    return render(request, 'App/rent.html')




def sell(request):
    form = PropertyForm(request.POST, request.FILES)
    if request.method == "POST":

        print('inside post')
        if form.is_valid():
            form.save()
            return render(request, 'App/success.html')
    # else:
    #     form = UserRegForm()
    return render(request, 'App/sell.html', {'form': form})


def search_view(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        property_category = request.GET.get('property_category')

        # Perform the search query based on the parameters
        properties = Property.objects.filter(
            property_location=city
        )

        return render(request, 'App/search_results.html', {'properties': properties})
    else:
        return render(request, 'App/search_results.html')


