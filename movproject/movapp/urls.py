from . import views
from django.urls import path

app_name='movapp'
urlpatterns = [

    path('',views.main,name='main'),
    path('movie/<int:mov_id>/',views.datail,name='detail'),
    path('add/',views.add_field,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]
