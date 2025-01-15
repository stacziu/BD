"""
URL configuration for mydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from libraryapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('rejestracja/', views.register, name='register'),
    path('zaloguj/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_physical_book/<int:book_id>/', views.delete_physical_book, name='delete_physical_book'),
    path('add_physical_book/<int:book_id>/', views.add_physical_book, name='add_physical_book'),
    path('place_hold/<int:book_id>/', views.place_hold, name='place_hold'),
    path('holds/', views.active_holds, name='active_holds'),
    path('loans/',views.loans, name='active_loans'),
    path('approve_loan/<int:hold_id>/', views.approve_loan, name='approve_loan'),
    path('cancel_hold/<int:hold_id>/', views.cancel_hold, name='cancel_hold'),
    path('mark_returned/<int:loan_id>/', views.mark_returned, name='mark_returned'),
    path('users/', views.users, name='users'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('profile/', views.update_profile, name='profile'),
    path("update-user-roles/", views.users, name="update_user_roles"),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('most_borrowed/', views.add_book, name='most_borrowed'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
