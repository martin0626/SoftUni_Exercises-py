from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DateDetailView, DeleteView, TemplateView, DetailView

from TodoApp.Todo.forms import CreateTodoForm
from TodoApp.Todo.models import Todo


class MyTodosView(CreateView):
    template_name = 'Todo/my_todos.html'
    model = Todo
    form_class = CreateTodoForm
    context_object_name = 'form'
    success_url = reverse_lazy('my todos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        done_todos = Todo.objects.filter(owner_id=user.id, is_done=True).count()
        waiting_todos = Todo.objects.filter(owner_id=user.id, is_done=False).count()
        context["todos"] = Todo.objects.filter(owner_id=user.id)
        context['done_count'] = done_todos
        context['waiting_count'] = waiting_todos
        return context

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.owner = self.request.user
        return super(MyTodosView, self).form_valid(form)


def todo_action_view(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.is_done:
        todo.is_done = False
    else:
        todo.is_done = True
    todo.save()
    return redirect('my todos')


class DeleteTodoView(DetailView):
    template_name = 'Todo/delete_todo.html'
    model = Todo


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('my todos')