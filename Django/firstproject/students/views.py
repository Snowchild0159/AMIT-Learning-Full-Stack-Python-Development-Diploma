from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest , JsonResponse
from .models import Department
from django.views import View



def render_departments(request) : 
    if request.method == "GET" :
        departments = Department.objects.all()
        
        return render(request , "snow.html" , {
            "departments" : departments
        } )
class departmentDetail(View):
    def get(self , request , id) :
        department = Department.objects.filter(id = id).first()

        if department :
                return JsonResponse({
                    "name" : department.name ,
                    "street" : department.street ,
                    "city" : department.city ,
                    "state" : department.state 
                })
        else :
                return JsonResponse({
                    "error" : "Not Found"
                })  
    def put(self , request , id) :
        department = Department.objects.filter(id = id).first()
        if department :

            import json
            data = json.loads(request.body)
            
            Department.objects.update(
                name = data.get("name") ,
                state = data.get("state") ,
                street = data.get("street") ,
                city = data.get("city") 
            )   
            return JsonResponse({"status" : "updated successfully"}) 
        else :
                return JsonResponse({
                    "error" : "Not Found"
                })  
    def patch(self , request , id) :
        department = Department.objects.filter(id = id).first()
        if department :
            import json
            data = json.loads(request.body)
            
            Department.objects.update(
                name = data.get("name" , department.name) ,
                state = data.get("state" , department.state) ,
                street = data.get("street" , department.street) ,
                city = data.get("city" , department.city) 
            )   
            return JsonResponse({"status" : "updated successfully"})
        else : 
            return JsonResponse({
                "error" : "Not Found"
            })  
    def delete(self , request , id) :
        department = Department.objects.filter(id = id).first()
        
        if department :
            import json
            data = json.loads(request.body)
            
            department.delete()   
            return JsonResponse({"status" : "deleted successfully"})
        else : 
            return JsonResponse({
                "error" : "Not Found"
            })  
        

def get_all_depts(request) : 
    depts = list(Department.objects.values())
    data = {
        "department" : depts
    }
    
    return JsonResponse(data)

def get_depts_by_id(request , id) : 
    department = Department.objects.filter(id = id).first()
    
    if department :
        return JsonResponse({
            "name" : department.name ,
            "street" : department.street ,
            "city" : department.city ,
            "state" : department.state 
        })
    else :
        return JsonResponse({
            "error" : "Not Found"
        })  
        
def create_department(request) : 
    if request.method == 'POST' : 
        body = request.body
        import json
        department = json.loads(body)
        Department.objects.create(
            name = department["name"] , 
            street = department["street"] , 
            city = department["city"] , 
            state = department["state"] 
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
                name = data.get("name") ,
                state = data.get("state") ,
                street = data.get("street") ,
                city = data.get("city") 
            )   
            return JsonResponse({"status" : "updated successfully"}) 
        elif request.method == "PATCH" :
            Department.objects.update(
                name = data.get("name" , department.name) ,
                state = data.get("state" , department.state) ,
                street = data.get("street" , department.street) ,
                city = data.get("city" , department.city) 
            )   
            return JsonResponse({"status" : "updated successfully"}) 
        else : 
            return JsonResponse({"status" : "error happened"}) 
               