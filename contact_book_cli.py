contact=[]
Ram ={"name":"Ram","phone number":"90001000"}
Sita={"name":"Sita","phone number":"10000001"}
Gita ={"name":"Gita","phone number":"110000123"}
contact=[Ram,Sita,Gita] #creating a list of dictionaries
i=0
add_new_contact = input("Do you want to add new number?: yes/no\n")
if add_new_contact.lower() == "yes":
    new_contact ={"name":input("Enter name:\n"),"phone number":input("Enter phone number")}
    contact.append(new_contact)

def get_name(person):
    return (person["name"])

   
sorted_contact = sorted(contact,key =get_name)
for i,person in enumerate(sorted_contact):
    # can also use for i in range len(contact):
    # enumerate more pythonic way for cleaner code
    # used to iterate over a collection (like a list, tuple, or string) while
    # simultaneously keeping track of the index
   
    print(f"{i+1}. Name: {person['name']}\n Phone number: {person['phone number']}")
    i+=1
