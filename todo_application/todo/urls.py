from django.urls import path
from . import views
from .views import TaskList,TaskCreate,TaskUpdate,TaskDelete,TaskDetailView,Home


urlpatterns =[
    path('',views.Home, name='home'),
    path('register/', views.register_function, name='Register'),
    path('login/', views.login_fun, name='login'),
    # path('login',CustomLoginView.as_view(),name='login'),
    path('task-list/',TaskList.as_view(), name='task1'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(), name='task-delete'),
    path('task-detail/<int:pk>/',TaskDetailView.as_view(), name='task-detail')



]