from django.urls import path

from tasks.views import TaskList, ApplicationsList
from .views import UserList, UserDetail, UserRegistration, CurrentUserDetail

urlpatterns = [
    path('registration', UserRegistration.as_view()),  # TODO пока сырой вариант

    path('<int:pk>', UserDetail.as_view()),
    path('<int:authorid>/tasks', TaskList.as_view()),
    path('<int:implementerid>/todo_tasks', TaskList.as_view()),
    path('<int:userid>/applications', ApplicationsList.as_view()),

    path('<str:username>', UserDetail.as_view(lookup_field='username')),
    path('<str:authorusername>/tasks', TaskList.as_view()),
    path('<str:implementerusername>/todo_tasks', TaskList.as_view()),
    path('<str:username>/applications', ApplicationsList.as_view()),

    path('', UserList.as_view()),
]
