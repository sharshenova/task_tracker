from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from webapp.models import Project
from webapp.forms import ProjectSearchForm, ProjectForm
from django.urls import reverse, reverse_lazy

class ProjectListView(ListView, FormView):
    model = Project
    template_name = 'project_list.html'
    form_class = ProjectSearchForm

    def get_queryset(self):
        project_name = self.request.GET.get('project_name')
        if project_name:
            return self.model.objects.filter(project__icontains=project_name)
        else:
            return self.model.objects.all()


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



