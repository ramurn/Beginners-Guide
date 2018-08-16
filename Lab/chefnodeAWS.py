def ipVal(obj):
    print ("Validating IP Address..")
    while True:
            count = 0
            for i in obj.split("."):
                if not i:
                    i=999
                if (int(i) >= 1 and int(i) <= 255):
                    count += 1
            if ((len(obj.split("."))) == 4 and count == 4):
                return obj
                break
            else:
                obj=input("Incorrect Option. enter Valid IP: ")

mpub=input("Enter ChefMaster Public IP: ")
mpub=ipVal(mpub)
mpvt=input("Enter ChefMaster Pvt IP: ")
mpvt=ipVal(mpvt)
wpub=input("Enter ChefWS Public IP: ")
wpub=ipVal(wpub)
wpvt=input("Enter ChefWS Pvt IP: ")
wpvt=ipVal(wpvt)


