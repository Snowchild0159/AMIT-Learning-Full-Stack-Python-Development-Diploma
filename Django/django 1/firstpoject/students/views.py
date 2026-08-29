from django.shortcuts import render , redirect

# # Create your views here.
from django.http import HttpResponse , JsonResponse 
from .models import Department 

from django.views import View 
from .forms import DepartmentForm 


def render_departments(request) : 
    if request.method == "GET" : 
        search = request.GET.get("q")
        if search : 
            departments = Department.objects.filter(is_delete = False , name__contains = search)
        else : 
            departments = Department.objects.filter(is_delete = False)
        
        return render(request , "index.html" , {
            "departments" : departments ,
            "title" : "Home page"
        } )
def add_department(request) : 
    if request.method == "GET" : 
        form = DepartmentForm()
        
        return render(request , 'create.html' , {"form" : form ,  "title" : "Add new department"} )
        
    elif request.method == "POST" : 
        data = request.POST
 
        form = DepartmentForm(data) 
        
        if form.is_valid() : 
            form.save()
            return redirect("home")
        else : 
            return render(request , 'create.html' , {"form" : form , "title" : "Add new department"} )
                     
        
def delete_department_template(request, id) : 
    if request.method == "GET" : 
        department = Department.objects.filter(id = id).first() 
        if department : 
            return render(request , 'delete.html' , {"department" : department , "title" : "Delete Department"})
    elif request.method == "POST" : 
        Department.objects.filter(id = id).update(is_delete = True)
        return redirect("home")
        
def update_department_template(request , id) : 
    if request.method == "GET" : 
        department = Department.objects.filter(id = id , is_delete = False).first() 
        form = DepartmentForm(instance=department)
        return render(request , 'update.html' , {'form' : form ,  "title" : "Update department"})
        # return render(request , 'update.html' , {'form' : form})
    elif request.method == "POST" : 
        department = Department.objects.filter(id = id).first() 
        # print(request.body)
        # print(request.POST)
        form = DepartmentForm(request.POST , instance=department)
        if form.is_valid() : 
            form.save()
            
            return redirect("home")
        else : 
            return render(request , 'update.html' , {'form' : form ,   "title" : "Update department"})
            
        
  
  
        
class DepartmentAPIView(View) : 
    def get(self, request) : 
        depts = list(Department.objects.values())
        data = {
            "departments" : depts
        }
        return JsonResponse(data )
    def post (self , request) : 
        body = request.body 
        import json 
        department = json.loads(body)
        Department.objects.create(
            name = department["name"] , 
            streat = department["streat"] ,
            city = department["city"] , 
            state = department['state']
        )
        return JsonResponse({"status" : "created successfully"})

class DepartmentDetail(View) : 
    def get(self , request , id) : 
        department = Department.objects.filter(id = id).first()
        
        if department : 
            return JsonResponse({
                "name" : department.name ,
                "streat" : department.streat,
                "city" : department.city,  
                "state" : department.state
            })
        else : 
            return JsonResponse({
                "error" : "Not found"
            })
            
    def put(self, request , id) : 
        department = Department.objects.filter(id = id).first() 
        if department : 
            import json 
            data = json.loads(request.body)
    
            Department.objects.update(
                name=  data.get("name") , 
                state=  data.get("state") , 
                streat = data.get("streat") , 
                city = data.get("city")
            )
            return JsonResponse({"status" : "updated successfully"})
        else : 
            return JsonResponse({
                "error" : "Not found"
            })
    def patch(self , request , id) :
        department = Department.objects.filter(id = id).first() 
        if department : 
            import json 
            data = json.loads(request.body)
    
            Department.objects.update(
                name=  data.get("name" , department.name) , 
                state=  data.get("state" , department.state) , 
                streat = data.get("streat" , department.streat) , 
                city = data.get("city" , department.city)
            )
            return JsonResponse({"status" : "updated successfully"})
        else : 
            return JsonResponse({
                "error" : "Not found"
            })
    def delete(self, request , id) : 
        
        department = Department.objects.filter(id = id).first()
        if department : 
            department.delete() 
            return JsonResponse({"status" : "deleted successfully"})
        else : 
            return JsonResponse({"status" : "error happen"})
    
        
# api method 


def get_all_depts(request) : 
    depts = list(Department.objects.values())
    data = {
        "departments" : depts
    }
    # departments = json.dumps(data)
    # print(departments)
    return JsonResponse(data )

def get_department_by_id(request , id) : 
    department = Department.objects.filter(id = id).first()
    
    if department : 
        return JsonResponse({
            "name" : department.name ,
            "streat" : department.streat,
            "city" : department.city,  
            "state" : department.state
        })
    else : 
        return JsonResponse({
            "error" : "Not found"
        })

def create_department(request) : 
    if request.method == 'POST': 
        body = request.body 
        import json 
        department = json.loads(body)
        Department.objects.create(
            name = department["name"] , 
            streat = department["streat"] ,
            city = department["city"] , 
            state = department['state']
        )
        return JsonResponse({"status" : "created successfully"})
    else : 
        return JsonResponse({"status" : "bad method"})
    

def update_department(request , id) : 
    department = Department.objects.filter(id = id).first() 
    if department : 
        import json 
        data = json.loads(request.body)
        
        if request.method == "PUT" : 
                Department.objects.update(
                    name=  data.get("name") , 
                    state=  data.get("state") , 
                    streat = data.get("streat") , 
                    city = data.get("city")
                )
                return JsonResponse({"status" : "updated successfully"})
        elif request.method == "PATCH" : 
                Department.objects.update(
                    name=  data.get("name" , department.name) , 
                    state=  data.get("state" , department.state) , 
                    streat = data.get("streat" , department.streat) , 
                    city = data.get("city" , department.city)
                )
                return JsonResponse({"status" : "updated successfully"})
            
    else : 
        return JsonResponse({"Status" : "erorr happen"})
        
        
def delete_department(request , id) :
    if request.method == "DELETE" : 
        department = Department.objects.filter(id = id).first()
        if department : 
            department.delete() 
            return JsonResponse({"status" : "deleted successfully"})
        else : 
            return JsonResponse({"status" : "error happen"})