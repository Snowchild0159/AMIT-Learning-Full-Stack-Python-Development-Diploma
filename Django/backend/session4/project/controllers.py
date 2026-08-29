
from models import store_data , delete_record ,get_by_id


def validate_student(name , age ,address , phone_number , student = None) :
    erorrs = []
    try : 
        # validate name 
        if len(name.strip()) < 3 : 
            erorrs.append("name")
        if not age.isdigit() or int(age) < 0 or int(age) > 150 : 
            erorrs.append("age")
        if len(address.strip()) < 3 : 
            erorrs.append("address") 
        if len(phone_number.strip()) != 11 : 
            erorrs.append("phone_number") 
            
        # ["age"]
        if len(erorrs) == 0 :
            id = store_data(name , age , address , phone_number , student)
            return True , id
        else : 
            return False , erorrs
    except Exception as ex  :
        return False , str(ex)
    
def valide_id(id) : 
    student = get_by_id(id)
    if student : 
        return  True , {
            "id" : student[0],
            "name" : student[1],
            "age" : student[2],
            "address" : student[3],
            "phone_number" : student[4],
        }
    else : 
        return False , None
    # from models import data  
    
    # for student in data : 
    #     if student["id"] == id :
    #         return True , student
        
    # return False , None

def delete_id(student) : 
    delete_record(student["id"])
