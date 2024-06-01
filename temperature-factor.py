
ampiant_temperature = float(input("Enter the ambiant temperature (c) : "))
catalog_temperature = float(input("Enter catalog temperature (c) : "))
c_c = float(input("Enter the cooling capacity (TR) : "))
temp_factor = ampiant_temperature/catalog_temperature
new_cc = temp_factor * c_c
print("the selection cooling load is ",new_cc)
