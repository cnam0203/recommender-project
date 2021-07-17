from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from json import dumps

# Create your views here.
# @login_required(login_url="/authentication/login")
def home(request):
    activity = {
            'customer_id'   : '123456',
            'time'          : 12,
            'action'        : 'visit web',
            'channel'       : 'website',
            'device'        : 'laptop',
            'experience'    : 'happy'
        }

    activities = [activity]*5
    total_customer  = 12345
    new_customer    = 1234

    reports = [
        {
            'id': 'action-chart',
            'title': 'Total touchpoint by action',
            'data': [['12-01-2021', 10], ['13-01-2021', 12], ['14-01-2021', 13], ['15-01-2021', 10]]
        },
        {
            'id': 'channel-chart',
            'title': 'Total touchpoint by channel',
            'data': [['12/01/2021', 10], ['13/01/2021', 12], ['14/01/2021', 13], ['15/01/2021', 10]]
        },

        {
            'id': 'device-chart',
            'title': 'Total touchpoint by device',
            'data': [['12/01/2021', 10], ['13/01/2021', 12], ['14/01/2021', 13], ['15/01/2021', 10]]
        }
    ]

    return render(request, "dashboard/home.html", 
                        { 
                            'activities': activities, 
                            'total_customer': total_customer, 
                            'new_customer': new_customer,
                            'reports': dumps(reports) 
                        })