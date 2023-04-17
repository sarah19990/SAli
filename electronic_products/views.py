from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review, Product
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request, 'electronic_products/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'electronic_products/about.html',  {'title': 'About Us'})

def contact(request):
    return render(request, 'electronic_products/contact.html',  {'title': 'Contact Us'})

def product(request):
    daily_report= {
        'reviews': Review.objects.all()
    }
    return render(request, 'electronic_products/product.html',  daily_report)

def smartTv(request):
    paginate_by = 5
    daily_reports= {
        'smartTvs': Product.objects.all()
    }
    return render(request, 'electronic_products/SmartTv.html', daily_reports)


def smartphone(request):
    paginate_by = 5
    daily_reports= {
        'smartphones': Product.objects.all()
    }
    return render(request, 'electronic_products/smartphone.html', daily_reports)

def smartwatch(request):
    paginate_by = 5
    daily_reports= {
        'smartwatch': Product.objects.all()
    }
    return render(request, 'electronic_products/smartwatch.html', daily_reports)

def tablet(request):
    paginate_by = 5
    daily_reports= {
        'tablet': Product.objects.all()
    }
    return render(request, 'electronic_products/tablet.html', daily_reports)

class PostListView(ListView):
    model = Review
    template_name = 'electronic_products/review_detail.html'
    context_object_name = 'reviews'
    ordering = ['-date_submitted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Review

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['author', 'product', 'product_rating', 'date_reviewed', 'text']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['author', 'product', 'product_rating', 'date_reviewed', 'text']
    def test_func(self):
        Review = self.get_object()
        if self.request.user == Review.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/product'
    def test_func(self):
        Review = self.get_object()
        if self.request.user == Review.author:
                return True
        return False
    
class PostListView2(ListView):
    model = Product
    template_name = 'electronic_products/SmartTv.html'
    context_object_name = 'smartTvs'
    ordering = ['-date_submitted']

class PostListView3(ListView):
    model = Product
    template_name = 'electronic_products/smartphone.html'
    context_object_name = 'smartphones'
    ordering = ['-date_submitted']  

class PostListView3(ListView):
    model = Product
    template_name = 'electronic_products/smartwatch.html'
    context_object_name = 'wearables'
    ordering = ['-date_submitted']  

class PostListView3(ListView):
    model = Product
    template_name = 'electronic_products/tablet.html'
    context_object_name = 'tablet'
    ordering = ['-date_submitted']  

class PostDetailView2(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
            reviews = Review.objects.filter(product = self.object).order_by('-date_reviewed')
            context = super(PostDetailView2, self).get_context_data(**kwargs)
            context.update({'title': 'List of Reviews', 'Reviews': reviews})
            return context

class PostCreateView2(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'brand', 'category', 'date_reviewed', 'release_of_date', 'description', 'image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView2(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'brand', 'category', 'date_reviewed', 'release_of_date', 'description', 'image']
    def test_func(self):
        Review = self.get_object()
        if self.request.user == Review.name:
            return True
        return False
    
class PostDeleteView2(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/product'
    def test_func(self):
        Review = self.get_object()
        if self.request.user == Review.name:
                return True
        return False
    
    
    