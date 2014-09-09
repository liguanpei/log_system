#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import time
import os

from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

def device_info(request, area_name, template_name):
    """
    """
    return render(request, template_name)

def device_create(request, template_name):
    if request.method == 'POST':
        device_name = request.POST.get("device_name")
        device_area = request.POST.get("device_area")
        print device_name, device_area
    return render(request, template_name)

def area_info(request, template_name):
    """
    """
    return render(request, template_name)

def area_create(request, template_name):
    if request.method == 'POST':
        pass
    return render(request, template_name)

def email_info(request, template_name):
    """
    """
    return render(request, template_name)

def email_create(request, template_name):
    if request.method == 'POST':
        pass
    return render(request, template_name)

def history_log(request, dev_name, template_name):
    return render(request, template_name)

def delete(request):
    return HttpResponseRedirect(reverse("index"))
    
