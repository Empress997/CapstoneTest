from django.urls import path
from . import views 

app_name = "farms"

urlpatterns = [
    path('',views.HomeView.as_view(), name="home"),
    path('categories/',views.categories,name="categories"),
    path('crop/<slug:slug>/',views.detail, name="crop-detail"),
    path('contact/',views.ContactView.as_view(), name="contact"),
    path('services/',views.services,name="services"),
    path('advisories/',views.advisories,name="advisories"),
    path('news/details',views.Newsview, name="news-details")
]
