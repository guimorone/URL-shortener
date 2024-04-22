import traceback
from django.http import HttpResponse
from django.shortcuts import render
from utils.misc import base_context


def index(request) -> HttpResponse:
    try:
        context = {**base_context, "latest_question_list": 'oi'}

        return render(request, 'index.html', context, status=200)
    except:
        traceback.print_exc()

        return HttpResponse(status=500)
