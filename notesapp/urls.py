from django.urls import path
from . import views

urlpatterns = (
    # <--------Notes--------->
    path('', views.index, name='index'),
    path('addNotes', views.addNotes, name='new'),
    path('note/<str:pk>', views.note_detail, name = 'note'),
    path('delete_note/<str:pk>', views.delete_note, name = 'delete'),
    path('search_result', views.search_page, name = 'search'),
    path('viewNotes',views.viewNotes,name='view'),
    path('dashboard', views.dashboard, name='dashboard'),


)
