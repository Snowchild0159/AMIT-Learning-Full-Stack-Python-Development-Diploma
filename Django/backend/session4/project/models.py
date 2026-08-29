
from json import loads , dumps 
data = []
import psycopg2

conn = psycopg2.connect(
    dbname = "pythonconn" ,
    host = "localhost" ,
    port = "5432" ,
    user = "postgres" ,
    password = "@2bdelfatta77"
)

cursor = conn.cursor()




# print(cursor.fetchall())
# def retrieve_data() :
#     global data 
    
#     cursor.execute("select * from student ;")
    
#     featched_data = cursor.fetchall()
    
    

    
    # with open("data.json") as file : 
    #     file_content = file.read() 
    #     file_dict = loads(file_content) 
        
    #     data = file_dict["students"]

def get_all() :
    try : 
        cursor.execute("select * from student;")
        student = cursor.fetchall()
        return student
    except : 
        return None
    

def get_by_id(id) :
    try : 
        cursor.execute(f"""
                       select * from student
                       where id = {id}
                       """)
        student = cursor.fetchone()
        return student
    except : 
        return None
    

def delete_record(id) :
    try : 
        cursor.execute(f""" 
                       delete from student 
                       where id = {id} ;
                       """)
        conn.commit()
        
        return True 
    except : 
        return False
    # global data 
    # try :
    #     data.remove(student)
    #     return True
    # except : 
    #     return False
# def save_data() :
#     global data 
#     stduents = {
#         "students" : data 
#     }
#     file_content = dumps(stduents)
#     with open("data.json" , "w") as file : 
#         file.write(file_content)


def store_data (name , age , address , phone_number , student = None) : 
    global data 
    if student : 
        id = student.get("id")
        cursor.execute(f"""
                       update student
                       set name = '{name}' ,
                       age = {age} ,
                       address = '{address}' ,
                       phone_number=  '{phone_number}'
                       where id = {id}
                       """)
        conn.commit()
        
        # student["name"] = name 
        # student["age"] = age 
        # student["address"] = address 
        # student["phone_number"] = phone_number 
    else : 
        cursor.execute("select max(id) from student")
        id = cursor.fetchone()[0] + 1
        cursor.execute(f"""insert into student (id,  name , age , address , phone_number)  
                       values({id} ,'{name}', {age} , '{address}' , '{phone_number}') """)
        conn.commit()
        # data.append({
        #     "id" : str(id) ,
        #     "name" : name , 
        #     "age" : age , 
        #     "address" : address , 
        #     "phone_number" : phone_number
        # }) 
    return id