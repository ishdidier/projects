print("===================================" )
print("\nGAHANGA CELL SECURITY CONTRIBUTION")
print("\n===================================" )
def swicth():
    choice=int(input("\n ENTER YOUR CHOICE:"))
print("\n PLEASE ENTER YOUR CHOICE BELOW(1-4)")
print("\n\t\t 1.register payments")
print(" \n\t\t 2.list of leaders ")
print("\n\t\t 3.show record")
print("\n\t\t 4.exit")
choice=int(input("\n ENTER YOUR CHOICE:"))
import sys
if choice==1:
    result=input("\nEnter name of payer:")
    print(f"\n\t\tYOU Entered:{result}")
    results=input("Enter month of fees:")
    print(f"\n\t\tpaid month of:{results}")
    resultss=int(input("Enter amount paid:"))
    print(f"\n thank you,{result} Successuly registered for amount:,{resultss}")
    print("\n========================================\n")
    print("add another for continue and 2 for exit")
    press=list()
    user=str(input("NAME of payer:"))
    press.append(f"Name of payer:{user}")
    user=(input("Enter month of fees:"))
    press.append(f"month of payment:{user}")
    user=(input("Enter amount paid:"))
    press.append(f"Amount paid:{user}")
    for x in press:print(x)
        
elif choice==2:
    print("=======================================")
    print("\n\tThese are Leaders at cell level\n")
    print("=======================================")
    list1=["excutive:SHIMWA","secretary:MUSONI","security:MUSHIMI"]
    for x in list1:print(x)
    print("========================================")
    print("\n\tThese are Leaders at village level:\n")
    print("=========================================")
    list2=["Mapfundo:URAYENEZA","Rwamaraba:NYIRANUMA"]
    for y in list2:print(y)
    list3=["Mapfundo:079934526","Rwamaraba:0788843534"]
    for z in list3:print(z)
    print("==========================================")
elif choice==3:
    print("\nTHIS CHOICE STILL IN PROCESSING.....\n")
    
elif choice==4:
    print("WE ARE STILL WORKING ON IT")