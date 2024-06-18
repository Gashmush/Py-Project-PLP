from django.shortcuts import render,redirect,get_object_or_404
from .forms import WorkerForm
from .models import Category,Worker
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, "domestic/home.html")


def workers_list(request,category_slug=None):
    workers=Worker.objects.all().filter(status='Available')
    categories=Category.objects.all()
    category=None
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        workers=workers.filter(category=category)
    
    workers = workers[:10]
    if request.user.is_authenticated:
        worker = get_object_or_404(Worker, user=request.user)
        worker.profile_visits += 1
        worker.save()

    return render(request, "domestic/worker_list.html", {"category":category, "workers":workers,"categories":categories})

def worker_detail(request,slug):
    worker=get_object_or_404(Worker, status='Available', slug=slug)
    if request.user.is_authenticated and request.user.is_customer:
        worker.profile_views += 1
        worker.save()
    context={"worker":worker}
    return render(request, "domestic/detail.html", context)




@login_required
def worker_register_form(request):
    if request.method == "POST":
        form = WorkerForm(request.POST, request.FILES)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.user = request.user 
            worker.save()
            return redirect("dashboard")
    else:
        form = WorkerForm()
    
    return render(request, "domestic/worker_form.html", {"form": form})




def user_dashboard(request):
    profile_views = 0
    if request.user.is_authenticated and request.user.is_worker:
        try:
            worker = Worker.objects.get(user=request.user)
            profile_views = worker.profile_views
        except Worker.DoesNotExist:
            pass
    return render(request, "domestic/dashboard.html", {"profile_views": profile_views})
