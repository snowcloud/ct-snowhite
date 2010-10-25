""" views for home app

"""
from django.shortcuts import render_to_response
from django.template import RequestContext 

# from ct_groups.models import CTGroup

def home(request):
    
    # catalogues = CTGroup.objects.filter(tags__contains='catalogue')
    
    return render_to_response('home/index.html' ,
        RequestContext( request , 
            {   'catalogues': None, # CTGroup.objects.filter(tags__contains='catalogue'),
                'mappings': None, #CTGroup.objects.filter(tags__contains='mapping'),
                'groups': None, #CTGroup.objects.all()
            }))
