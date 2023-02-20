from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView
from .forms import RegisterForm,LoginForm

from .models import Tasks,Login,Register



# Create your views here.

def Home(request):
    return render(request,'home.html')


# class CustomLoginView(LoginView):
#     model = Login
#     template_name = 'login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return reverse_lazy('task1')


class TaskList(ListView):
    model = Tasks
    context_object_name = 'task1'
    template_name = 'tasklist.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     messages.success(self.request,'The task was created successfully..')
    #     return super(TaskCreate,self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'


class TaskDelete(DeleteView):
    model= Tasks
    fields = '__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model = Tasks
    # context_object_name = 'task1'
    # success_url = reverse_lazy('task1')
    template_name = 'taskdetail.html'


def register_function(request):
    register = Register.objects.all()
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login/')
    context = {'register': register, 'form': form}
    return render(request, 'Register.html', context)

    # context = {}
    # a = RegisterForm(request.POST)
    # if a.is_valid():
    #     a.save()
    # context['form']=a
    # return render(request,"Register.html",context)


def login_fun(request):
    login = Login.objects.all()
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/task-list/')
    context = {'login':login,'form':form}
    return render(request,'login.html',context)

    # context = {}
    # ab = LoginForm(request.POST)
    # if ab.is_valid():
    #     ab.save()
    # context['form'] = ab
    # return render(request, 'login.html',context)
