from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from webapp.models import Project
from webapp.forms import ProjectSearchForm, ProjectForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


class ProjectListView(ListView, FormView):
    model = Project
    template_name = 'project_list.html'
    form_class = ProjectSearchForm

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('accounts:login')
    #     else:
    #         return super().dispatch(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('webapp.project_view'):
            return HttpResponseForbidden()
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        project_name = self.request.GET.get('project_name')
        if project_name:
            return self.model.objects.filter(project__icontains=project_name)
        else:
            return self.model.objects.all()

# написать базовый класс представлений и в нем переопределить метод dispatch и везде наследоваться от него


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project_create.html'
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project_update.html'
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('project_list')



