from datetime import date
from django.shortcuts import render

# Create your views here.
def family(request, ):

    context = {
        'familiar1' : {
        'name': 'Dante',
        'surname': 'Paez',
        'age': 11,
        'date': date(2011, 6, 25),
        'family_relationship': 'Hijo',
        },


        'familiar2' : {
        'name': 'Fernando',
        'surname': 'Machado',
        'age': 28,
        'date': date(1994, 8, 11),
        'family_relationship': 'Primo',
        },

        'familiar3' : {
        'name': 'Daniela',
        'surname': 'Warzel',
        'age': 34,
        'date': date(1988, 6, 20),
        'family_relationship': 'Hermana',
        }


    }

    return render(request, 'family.html', context)
