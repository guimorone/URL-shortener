import traceback
from typing import Optional
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from utils.misc import base_context

from .models import UrlModel


def index(request: HttpRequest) -> HttpResponse:
    try:
        status = 200
        context = {**base_context}
        if request.method == 'POST':
            long_url: str = request.POST.get('long_url')
            if not long_url:
                context['error_message'] = 'Please provide a URL to shorten.'
                status = 400
                return render(request, 'index.html', context, status=status)

            url_model_instance, _ = UrlModel.objects.get_or_create(long_url=long_url)
            if url_model_instance.has_expired:
                url_model_instance.delete()
                url_model_instance = UrlModel.objects.create(long_url=long_url)

            context['short_url'] = request.build_absolute_uri(f'/{url_model_instance.short_code}')
            status = 201

        return render(request, 'index.html', context, status=status)
    except:
        traceback.print_exc()

        return HttpResponse(status=500)


def parse(_request: HttpRequest, short_code: Optional[str]) -> HttpResponse:
    try:
        url_model_instance = UrlModel.objects.get(short_code=short_code)

        return HttpResponseRedirect(url_model_instance.long_url)
    except UrlModel.DoesNotExist:
        return HttpResponse(status=404)
    except:
        traceback.print_exc()

        return HttpResponse(status=500)
