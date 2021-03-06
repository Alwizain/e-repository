from django.urls import path
from . import views

# app_name = 'order'

urlpatterns = [
	path('', views.order_list, name="order_list"),
	path('delete/<int:id>', views.order_delete, name='order_delete'),
	path('<int:id>', views.order_details, name="order_details"),
	path('details/', views.order_create, name="order_create"),
 	path('views/<int:id>', views.order_view, name="order_view"),
	path('pdf/<int:id>',views.pdf.as_view(), name="pdf"),
]
