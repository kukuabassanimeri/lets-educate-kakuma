from django.shortcuts import render, redirect
from .forms import ScholarshipUserCreationForm, ScholarshipUserLoginForm, ScholarshipPostModelForm, ContactForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ScholarshipPost, ContactUs
from django.shortcuts import get_object_or_404

# Create your views here.

#scholarship_blog user creation view
def user_registration(request):
    if request.method == 'POST':
        user_form = ScholarshipUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('scholarship_post:user-login')
    else:
        user_form = ScholarshipUserCreationForm()
    return render(request, 'scholarship_post/user_register.html', {'user_form': user_form})

#scholarship_post user login view
def user_login_view(request):
    if request.method == 'POST':
        log_form = ScholarshipUserLoginForm(request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data['username']
            password = log_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user) 
                return redirect('scholarship_post:home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        log_form = ScholarshipUserLoginForm()

    return render(request, 'registration/login.html', {'log_form': log_form})

#scholarship_post user home view
@login_required
def home(request):
    return render(request, 'scholarship_post/home.html')

#scholarship_post user logout view
def user_logout_view(request):
    logout(request) 
    return redirect('scholarship_post:user-login') 

#scholarship_blog scholarship lists view
def scholarships_blog_list(request):
    scholarships = ScholarshipPost.objects.all().order_by('-created_at')
    return render(request,'scholarship_post/scholarship_list.html', {'scholarships': scholarships})

#scholarship_blog post view
def add_scholarship(request):
    if request.method == 'POST':
        s_form = ScholarshipPostModelForm(request.POST)
        if s_form.is_valid():
            scholarship = s_form.save(commit=False)
            scholarship.created_by = request.user
            scholarship.save()
            messages.success(request, "scholarship post added successfully")
            return redirect('scholarship_post:scholarship-blog-list')
    else:
        s_form = ScholarshipPostModelForm()
    return render(request, 'scholarship_post/add_scholarship.html', {'s_form': s_form})
    
#scholarship_blog scholarship post deletion view
def delete_scholarship(request, pk):
    scholarship = get_object_or_404(ScholarshipPost, pk=pk)
    if scholarship.created_by != request.user:
        messages.error(request, "You are not authorized to delete this post")
        return redirect('scholarship_post:scholarship-detail', pk=pk)

    if request.method == 'POST':
        scholarship.delete()
        messages.success(request, "Scholarship post deleted successfully")
        return redirect('scholarship_post:scholarship-blog-list')

    return render(request, 'scholarship_post/confirm_delete_post.html', {'scholarship': scholarship})


#scholarship_post detailed view
def scholarship_detail(request, pk):
    scholarship = get_object_or_404(ScholarshipPost, pk=pk)
    return render(request, 'scholarship_post/scholarship_detailed.html', {'scholarship': scholarship})

#scholarship_post update post view
@login_required
def update_scholarship(request, pk):
    scholarship = get_object_or_404(ScholarshipPost, pk=pk)
    if scholarship.created_by != request.user:
        messages.error(request, "You are not authorized to update this post")
        return redirect('scholarship_post:scholarship-detail', pk=pk)
    
    if request.method == 'POST':
        u_form = ScholarshipPostModelForm(request.POST, instance=scholarship)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Scholarship post updated successfully")
            return redirect('scholarship_post:scholarship-blog-list')
    else:
        u_form = ScholarshipPostModelForm(instance=scholarship)
    return render(request, 'scholarship_post/update_scholarship.html', {'u_form': u_form, 'scholarship': scholarship})

#Scholarship Post Contact Us view
def ContactUsView(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Message Successfully Received!")
            return redirect('scholarship_post:contact-us')
    else:
        contact_form = ContactForm()
    return render(request, 'scholarship_post/contact_us.html', {'contact_form': contact_form})
    