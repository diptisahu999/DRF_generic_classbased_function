from django.urls import path
from .import views
from .views import ListViewStudent,ListDelete,ListEdit


urlpatterns = [
    # path('api',views.studentlistview),
    # path('update/<int:pk>',views.studentdetailview)
    path('get/',ListViewStudent.as_view(),name='get'),
    path('post/',ListViewStudent.as_view(),name='post'),
    path('delete/<int:id>',ListDelete.as_view(),name='delete'),
    path('put/<int:id>',ListEdit.as_view(),name='put'),
    
]
