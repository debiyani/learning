def get_name(person):
    return (person["name"])

contact=[]
Ram ={"name":"Ram","phone number":"90001000"}
Sita={"name":"Sita","phone number":"10000001"}
Gita ={"name":"Gita","phone number":"110000123"}
contact=[Ram,Sita,Gita] #creating a list of dictionaries
i=0
update_contact = input("Do you want to add/delete a contact?: add/delete/no \n")


def get_name(person):
    return (person["name"])
# add new contact
if update_contact.lower() == "add":
    new_contact ={"name":input("Enter name:\n"),"phone number":input("Enter phone number")}
    contact.append(new_contact)

# delete contact
elif update_contact.lower() == "delete":
    which_del= input("Whose contact do you want to delete?:")

    for i,person in enumerate(contact):
        if person["name"].lower() == which_del.lower():
            del(contact[i])
            break  # Exit loop after deleting
#    display contact

sorted_contact = sorted(contact,key =get_name)
for i,person in enumerate(sorted_contact):
    # can also use for i in range len(contact):
    # enumerate more pythonic way for cleaner code
    # used to iterate over a collection (like a list, tuple, or string) while
    # simultaneously keeping track of the index
    print_contact = (f"{i+1}. Name: {person['name']}\n Phone number: {person['phone number']}")
    print(print_contact)
