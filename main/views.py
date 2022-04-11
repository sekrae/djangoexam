from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from main.models import Worker, Membership
from .forms import WorkerForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class WorkerListView(ListView):
    model = Worker
    template_name = 'worker_list.html'

def get_queryset(self):
        name = self.request.GET.get('query')
        queryset = Worker.objects.all()

        if name and name != '':
            queryset = queryset.filter(fullname__icontains=name)
        else:
            queryset = Worker.objects.all()
        return queryset

class WorkerCreateView(LoginRequiredMixin, CreateView):
    form_class = WorkerForm
    template_name = 'worker_form.html'
    success_url = reverse_lazy('worker_list')


class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'worker_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WorkerDetailView, self).get_context_data(**kwargs)
        context['membership'] = Membership.objects.filter(worker=self.get_object())
        return context


class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'worker_delete.html'
    success_url = reverse_lazy('worker_list')



class WorkerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Worker
    form_class = WorkerForm
    template_name = 'worker_form.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False

