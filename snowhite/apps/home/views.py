""" views for home app

"""
from django.shortcuts import render_to_response
from django.template import RequestContext 

from ct_groups.models import CTGroup

def home(request):
    
    return render_to_response('home/index.html' ,
        RequestContext( request , 
            {   'groups': CTGroup.objects.all()
            }))
