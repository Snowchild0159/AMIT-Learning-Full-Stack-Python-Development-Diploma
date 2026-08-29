"""
URL configuration for firstpoject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from .hello import say_hello
from students.views import add_department , delete_department_template , update_department_template , render_departments ,  DepartmentDetail ,  DepartmentAPIView,  delete_department ,  update_department, create_department , get_all_depts , get_department_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/" , say_hello) ,
    path("depts/" , render_departments , name="home") ,
    path("depts/update/<int:id>/" , update_department_template , name = "update_department") ,
    path("depts/delete/<int:id>/" , delete_department_template , name="delete_department") ,
    path("depts/add/" , add_department , name="create_department") ,
    path("departments/" , get_all_depts) ,
    path("apiview/departments/" , DepartmentAPIView.as_view()) ,
    path("apiview/departments/<int:id>/" , DepartmentDetail.as_view()) ,
    
    
    
    path("departments/create/" , create_department) ,
    path("departments/<int:id>" , get_department_by_id) ,
    path("departments/<int:id>/update/" , update_department) ,
    path("departments/<int:id>/delete/" , delete_department) ,
]
