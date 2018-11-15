from django.urls import path
from cbvapp import views
app_name='cbvapp'
urlpatterns = [

    path('',views.personList.as_view(),name='list'),
    path('<int:pk>',views.persondetail.as_view(),name='detail'),
    path('create/',views.personview.as_view(),name='create'),
    path('update/<int:pk>',views.personupdate.as_view(),name='update'),
    path('delete/<int:pk>',views.persondelete.as_view(),name='delete'),
    path('signup/',views.registration,name='signup'),
    path('signin/',views.userlogin,name='userlogin'),
    path('check/',views.checkuser,name='check'),
    path('search/',views.searchuser,name='search')

]
