from datetime import datetime, timedelta
from django.db.models import Q, F
from django.db.models import Count
from tracker.models import Task, Type

def get_requests():
    request_1 = Task.objects.filter(status__status_name__iexact='done',
                                    changed_at__range=[(datetime.now() - timedelta(days=30)),
                                                       datetime.now()]).distinct().values('id', 'text')
    print(f'\n Результат первого запроса: \n')
    for task in request_1:
        print(task)
    # request_2 = Task.objects.filter(Q(status__status_name__in=[(Q(status__status_name__exact='In process')),
    #                                                            (Q(status__status_name__exact='Done'))])
    #                                 & Q(types__in=[1, 2, 3])).values('id', 'text')
    request_2 = Task.objects.filter(Q(status__in=[1, 2]) & Q(types__in=[1, 2])).values('id', 'text')
    print(f'\n Результат второго запроса: \n')
    for task in request_2:
        print(task)

    request_3 = Task.objects.filter(Q(types__type_name__iexact='bug') | Q(text__icontains='bug')
                                    ).exclude(status__status_name__iexact='done').values('id', 'text')
    print(f'\n Результат третьего запроса: \n')
    for task in request_3:
        print(task)

    tasks = Task.objects.all().values('id', 'text', 'status__status_name', 'types__type_name').distinct()
    print(f'\n bonus 1: \n')
    for task in tasks:
        print(task)

    tasks = Task.objects.filter(text=F('description'))
    print(f'\n bonus 2: \n')
    for task in tasks:
        print(f'id:{task.id} text:{task.text} description:{task.description}')

    tasks = Task.objects.all().values('types').annotate(total=Count('types'))
    print(f'\n bonus 3:{tasks} \n')
