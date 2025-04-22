from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FileUploadForm

class StoragePageView(LoginRequiredMixin, TemplateView):
    template_name = "uploads/uploads.html"
    login_url = "account_login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FileUploadForm()
        return context

    def post(self, request, *args, **kwargs):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            return redirect('uploads')
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, 'uploads/uploads.html', context)


