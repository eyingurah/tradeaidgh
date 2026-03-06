import os

from django.conf import settings
from django.core.mail import send_mail
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from .forms import CForm
from .models import ContactForm, File, FilesAdmin, Post


def home(request):
    template = "index.html"
    context = {}
    return render(request, template, context)


def about(request):
    template = "about.html"
    context = {}
    return render(request, template, context)


def contact(request):
    if request.method == "POST":
        form = CForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            message = request.POST["message"]

            send_mail(
                name,
                subject,
                message,
                ["elijahyingurah@gmail.com", "apokerah@gmail.com"],
                fail_silently=False,
            )
            return redirect("/contact")
    else:
        form = CForm()

    template = "contact.html"
    context = {"form": form}
    return render(request, template, context)


def corporate(request):
    template = "corporate.html"
    context = {}
    return render(request, template, context)


def project_income(request):
    template = "project_income.html"
    context = {}
    return render(request, template, context)


def project_bawemas(request):
    template = "project_bawemas.html"
    context = {"file": FilesAdmin.objects.all()}
    return render(request, template, context)


def project_suscrib(request):
    template = "project_suscrib.html"
    context = {}
    return render(request, template, context)


def project_ieow(request):
    template = "project_ieow.html"
    context = {}
    return render(request, template, context)


def project_sei(request):
    template = "project_sei.html"
    context = {}
    return render(request, template, context)


def project_shine(request):
    template = "project_shine.html"
    context = {}
    return render(request, template, context)


def project_isolve(request):
    template = "project_isolve.html"
    context = {}
    return render(request, template, context)


def project_coslec(request):
    template = "project_coslec.html"
    context = {}
    return render(request, template, context)


def impact(request):
    template = "impact.html"
    context = {}
    return render(request, template, context)


def contribute(request):
    template = "contribute.html"
    context = {"file": FilesAdmin.objects.all()}
    return render(request, template, context)


def gift_card(request):
    template = "gift_card.html"
    context = {}
    return render(request, template, context)


def gallery(request):
    template = "gallery.html"
    context = {}
    return render(request, template, context)


def blog(request):
    template = "blog.html"
    context = {}
    return render(request, template, context)


def blog_kayayei(request):
    template = "blog-kayayei.html"
    context = {}
    return render(request, template, context)


def blog_cftc(request):
    template = "blog-cftc.html"
    context = {}
    return render(request, template, context)


def blog_environ(request):
    template = "blog-environ.html"
    context = {}
    return render(request, template, context)


def blog_call(request):
    template = "blog-call.html"
    context = {}
    return render(request, template, context)


def blog_bicaf23(request):
    template = "blog-bicaf23.html"
    context = {}
    return render(request, template, context)


def blog_25years(request):
    template = "blog-25years.html"
    context = {}
    return render(request, template, context)


def blog_25years2(request):
    template = "blog-25years2.html"
    context = {}
    return render(request, template, context)


def media(request):
    template = "media.html"
    context = {}
    return render(request, template, context)


def download_file(request):
    file = os.path.join(settings.BASE_DIR, "static/media/TAI_Catalogue_2022.pdf")
    file_opened = open(file, "rb")
    return FileResponse(file_opened)


def coslec_form(request):
    file = os.path.join(settings.BASE_DIR, "static/media/COSLEC_Application_Form.pdf")
    file_opened = open(file, "rb")
    return FileResponse(file_opened)
