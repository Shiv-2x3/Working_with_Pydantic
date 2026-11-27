# Importing base model.
from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Dict , Optional , Annotated

# defining class for our pydantic schema
class paitent(BaseModel): # This is our base model 
    # defining rules && Required feilds 
    name : Annotated[str , 
                     Field(max_length=50 , 
                           title="name of the paitent" , 
                           description="Add name of the paitent who are our regular consumers" , 
                           examples=["amit" , "shena"])]
    email : EmailStr 
    ig_url : AnyUrl
    age : int = Field(gt=0)
    weight : float
    sugar : Annotated[bool , Field(default=None , 
                                   title="Diabaities",
                                   description="Add Data about dibaitic paitent")]
    allergies : Optional[List[str]] = Field(max_length=20) # This is a optional feild
    contact : Dict[str , str]

# paitent data
paitent_info = {'name' : 'Shiv',
                'email' : 'Shiv@gmail.com',
                'ig_url' : "https://instagram?24344",
                'age' : 19,
                'weight' : 65.89,
                'sugar' : False,
                'allergies' : ['dust' , 'light'],
                'contact' : {'email' : 'xyz@gmail.com' , 'number' : '1234567899'}}



paitent1 = paitent(**paitent_info) # **-> unpack our dictnory


# Defining paitent function
def insert_paitent_data(paitent:paitent):
    print(paitent.name ,
          paitent.email ,
          paitent.ig_url,  
          paitent.age , 
          paitent.sugar , 
          paitent.weight , 
          paitent.allergies , 
          paitent.contact , sep='\n')
    print("!!data inserted sucessfully")


insert_paitent_data(paitent1)