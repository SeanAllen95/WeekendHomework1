# WRITE YOUR FUNCTIONS HERE
#1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
#2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#3
def add_or_remove_cash(pet_shop, change_in_cash):
    cash = (pet_shop["admin"]["total_cash"])
    cash += change_in_cash
    pet_shop["admin"]["total_cash"] = cash

    return cash

#4
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#5
def increase_pets_sold(pet_shop, num_of_pets):
    new_pet_num = pet_shop["admin"]["pets_sold"]
    new_pet_num += num_of_pets
    pet_shop["admin"]["pets_sold"] = new_pet_num
    return new_pet_num

#6
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#7
def get_pets_by_breed(pet_shop, breed):
    breed_list = []

    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(breed)

    return breed_list

#8
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

#9 
def remove_pet_by_name(pet_shop, pet_name):

     for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)
        

#10
def add_pet_to_stock(pet_shop, new_pet):

    new_pet_list = pet_shop["pets"].append(new_pet)
    return new_pet_list

#11
def get_customer_cash(customer):
    return customer["cash"]

#12
def remove_customer_cash(customer, amount):
    customer_balance = customer["cash"]
    new_customer_balance = customer_balance-amount
    customer["cash"] = new_customer_balance

    return customer["cash"]

#13
def get_customer_pet_count(customer):
    return len(customer["pets"])

#14
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

    


        

