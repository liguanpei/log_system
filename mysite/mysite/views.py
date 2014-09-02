#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import time
import os

from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

def index(request, template_name):
    """
    """
    return render(request, template_name)

def history_log(request, dev_name, template_name):
    print dev_name
    return render(request, template_name)
    
