from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django at least 20 minutes every day!",
    "april": "Learn Django at least 20 minutes every day!",
    "may": "Learn Django at least 20 minutes every day!",
    "june": "Learn Django at least 20 minutes every day!",
    "july": "Learn Django at least 20 minutes every day!",
    "august": "Learn Django at least 20 minutes every day!",
    "september": "Learn Django at least 20 minutes every day!",
    "october": "Learn Django at least 20 minutes every day!",
    "november": "Learn Django at least 20 minutes every day!",
    "december": "Learn Django at least 20 minutes every day!",
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html", {"text": challenge_text, "month_name": month})
        return HttpResponse(response_data, content_type="text/html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")