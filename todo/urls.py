from django.urls import path
# from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, DeleteView
from .forms import TodoForm

from .models import Todo
from .views import Home, TodoCreate, TodoList, TodoUpdate, TodoDelete, TodoDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('', TemplateView.as_view(template_name='todo/home.html'), name='home'),

    path('list', TodoList.as_view(), name='list'),
    # path('list', ListView.as_view(template_name='todo/todo_list.html'), name='list'),

    path('add', TodoCreate.as_view(), name='add'),
    # path('add', CreateView.as_view(template_name='todo/todo_add.html', model=Todo, form_class=TodoForm, success_url=reverse_lazy('todos/')), name='add'),

    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    # path('update/<int:id>', TodoUpdate.as_view(), name='update'),
    # path('update'/<int:pk>', TodoUpdate.as_view(model = Todo, form_class = TodoForm, template_name = 'todo/todo_update.html', success_url = reverse_lazy('list')), name='update'),

    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    # path('delete/<int:id>', TodoDelete.as_view(), name='delete'),
    # path('delete/<int:pk>', TodoDelete.as_view(model = Todo, template_name = 'todo/todo_delete.html', success_url = reverse_lazy('list')), name='delete'),

    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    # path('detail/<int:id>', TodoDetail.as_view(), name='detail'),
    # path('detail/<int:pk>', TodoDetail.as_view(model = Todo, template_name = 'todo/todo_detail.html'), name='detail'),
]