from django.shortcuts import render
from .models import Session, Tracker
from .templates import *
def show_form(request):
    return render(request, "home.html")

def Home(request):
    Session.objects.create(req_type=str(request.method))

    if request.method == "POST":
        transaction_type = request.POST.get("Type")
        amount = request.POST.get("Amount")

        if transaction_type and amount:
            Tracker.objects.create(
                amount=int(amount),
                transactiontype=transaction_type[:2].upper()
            )

    transactions = Tracker.objects.all()

    return render(request, "output.html", {"transactions": transactions})
