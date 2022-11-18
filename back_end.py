Name=input("Please Enter SALESMAN Name : ");
print ("Hello, ",Name)
print("\n")

SerialNo1=1

InitialCityLudhiana = {"LUDHIANA" : 0, "JALANDHAR" : 61, "PATIALA" : 93, "CHANDIGARH" : 106, "AMRITSAR" : 140}
InitialCityJalandhar = {"JALANDHAR" : 0, "LUDHIANA" : 61, "AMRITSAR" : 80, "CHANDIGARH" : 149, "PATIALA" : 154}
InitialCityAmritsar = {"AMRITSAR" : 0, "JALANDHAR" : 80, "LUDHIANA" : 140, "CHANDIGARH" : 229, "PATIALA" : 235}
InitialCityPatiala = {"PATIALA" : 0, "CHANDIGARH" : 75, "LUDHIANA" : 93, "JALANDHAR" : 154, "AMRITSAR" : 235}
InitialCityChandigarh = {"CHANDIGARH" : 0, "PATIALA" : 75, "LUDHIANA" : 106, "JALANDHAR" : 149, "AMRITSAR" : 229}

print ("Please enter from which city You are traveling")
print (" ")
UserResponce=input("City Name : ")


if UserResponce=="LUDHIANA" or UserResponce=="ludhiana" or UserResponce=="Ludhiana":
    print (" ")
    print ("SHORTEST DISTANCE - From 'LUDHIANA' ")
    print ("------------------------------------------")
    print (" ")
    for City in InitialCityLudhiana:
        print (SerialNo1,". ",City," : ",InitialCityLudhiana[City],"Kilo Meters")
        SerialNo1=SerialNo1+1

    print (" ")
    print ("After visiting 'AMRITSAR' you will come back to 'LUDHIANA' again.")
    print (Name," (SALESMAN) - You have to cover '140 KM' to return back.")

if UserResponce=="JALANDHAR" or UserResponce=="jalandhar" or UserResponce=="Jalandhar":
    print (" ")
    print ("SHORTEST DISTANCE - From 'JALANDHAR' ")
    print ("------------------------------------------")
    print (" ")
    for City in InitialCityJalandhar:
        print (SerialNo1,". ",City," : ",InitialCityJalandhar[City],"Kilo Meters")
        SerialNo1=SerialNo1+1

    print (" ")
    print ("After visiting 'PATIALA' you will come back to 'JALANDHAR' again.")
    print (Name," (SALESMAN) - You have to cover '154 KM' to return back.")

if UserResponce=="AMRITSAR" or UserResponce=="amritsar" or UserResponce=="Amritsar":
    print (" ")
    print ("SHORTEST DISTANCE - From 'AMRITSAR' ")
    print ("------------------------------------------")
    print (" ")
    for City in InitialCityAmritsar:
        print (SerialNo1,". ",City," : ",InitialCityAmritsar[City],"Kilo Meters")
        SerialNo1=SerialNo1+1

    print (" ")
    print ("After visiting 'PATIALA' you will come back to 'AMRITSAR' again.")
    print (Name," (SALESMAN) - You have to cover '235 KM' to return back.")

if UserResponce=="PATIALA" or UserResponce=="patiala" or UserResponce=="Patiala":
    print (" ")
    print ("SHORTEST DISTANCE - From 'PATIALA' ")
    print ("------------------------------------------")
    print (" ")
    for City in InitialCityPatiala:
        print (SerialNo1,". ",City," : ",InitialCityPatiala[City],"Kilo Meters")
        SerialNo1=SerialNo1+1

    print (" ")
    print ("After visiting 'AMRITSAR' you will come back to 'PATIALA' again.")
    print (Name," (SALESMAN) - You have to cover '235 KM' to return back.")

if UserResponce=="CHANDIGARH" or UserResponce=="chandigarh" or UserResponce=="Chandigarh":
    print (" ")
    print ("SHORTEST DISTANCE - From 'CHANDIGARH' ")
    print ("------------------------------------------")
    print (" ")
    for City in InitialCityChandigarh:
        print (SerialNo1,". ",City," : ",InitialCityChandigarh[City],"Kilo Meters")
        SerialNo1=SerialNo1+1

    print (" ")
    print ("After visiting 'AMRITSAR' you will come back to 'CHANDIGARH' again.")
    print (Name," (SALESMAN) - You have to cover '229 KM' to return back.")

print (" ")
print ("Thank-You")