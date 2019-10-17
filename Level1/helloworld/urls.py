from django.urls import path
from helloworld import views


app_name = 'helloworld'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    path('experience/', views.PreviousFirmView.as_view(), name='list'),
    path('education/', views.EducationView.as_view(), name='courses'),
    path('bio/', views.BioView.as_view(), name='bio'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('contact/', views.ContactOne, name='contact_one' ),
    path('CVdownload/', views.DownloadView.as_view(), name='download')
    # path('cv/', views.PreviousFirmView.as_view(), name='list'),
    #path('CVall/', views.PreviousTitleView.as_view(), name='detail')
    
]