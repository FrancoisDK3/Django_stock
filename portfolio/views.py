#portfolio/views.py

from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
from django.urls import reverse


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        #pk_d94ea148d5a64b058cafe25dac4ee281
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/quote?token=pk_d94ea148d5a64b058cafe25dac4ee281")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api })

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

def about(request):
    return render(request, 'about.html', {})

def watchlist(request):
    import requests
    import json
    
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('watchlist')

    else:
        ticker = Stock.objects.all()
        output = [] #create empty list to initiate the data to save
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) +"/quote?token=pk_d94ea148d5a64b058cafe25dac4ee281")
            try:
                api = json.loads(api_request.content)
                output.append(api) #add data to list
            except Exception as e:
                api = "Error..."
        #pass context to page
        #transfer out to page by adding api content to the page
        return render(request, 'watchlist.html', {'ticker' : ticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted!"))
    return redirect (delete_stock)

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker })


    