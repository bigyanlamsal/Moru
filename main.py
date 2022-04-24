import mysql.connector as c
import keyboard

class DBHelper:
    def __init__(self):
        self.conn = c.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root',
            database='nepal'
        )
        query = 'CREATE TABLE if not exists details(ProId int primary key, province varchar(50)) '
        #here table name details is changed to provinceDetails using SQL CLI
        query1 = 'CREATE TABLE if not exists districtDetails (ProvinceId int primary key, FOREIGN KEY(ProvinceId) REFERENCES provinceDetails(ProId), districtId int,district varchar(50))'
        query2 = 'CREATE TABLE if not exists municipalityDetails (ProvinceId int primary key, FOREIGN KEY(ProvinceId) REFERENCES provinceDetails(ProId), MunicId int,municipality varchar(50))'

        cur = self.conn.cursor()
        #cur.execute(query)
        #cur.execute(query)
        cur.execute(query2)


        # manipulating province  in table

        print("#########-- For Province see here--#####\n")

        print("Enter 1a to store province to database\n")
        print("Enter 1b to display province\n")
        print("Enter 1c to modify province\n")

        print("###########--For District see below--#####\n") 

        ###for manipulation of district data

        print("Enter 2a to store district to database\n")
        print("Enter 2b to display district\n")
        print("Enter 2c to modify district\n") 

        ###for creating/updating/deleting municipality

        

        while True:
          try: 

              ###task 1: Press 1 for creating/updating/deleting Province

            if keyboard.is_pressed('1'):
                #for storing province
                if keyboard.is_pressed('a'):
                  provinceId = int(input("Enter province id:\n"))
                  provinceName = input("Enter province name:\n")
                  
                  insertData = "INSERT INTO provinceDetails VALUES(%s,%s)"
                  data=(provinceId,provinceName)
                  cur = self.conn.cursor()
                  cur.execute(insertData,data)
                  self.conn.commit()
                  print("Province is stored to database...")
                  break
                 
                 #for viewing province
                elif keyboard.is_pressed('b'):
                    print("---->Province available in our database are listed as:")
                    cur=self.conn.cursor()
                    cur.execute("SELECT * FROM provinceDetails;")
                    showProvince = cur.fetchall()
                    for x in showProvince:
                        print(x)
                    break
                 
                 #for updating province
                elif keyboard.is_pressed('c'):
                    print("---->Update your province here:")
                    
                    proId = int(input("Enter province id you want to change:\n"))
                    province = (input("Enter the new province name:\n"))
                    modifyProvince = "update provinceDetails set province='{}' where ProId='{}'".format(province,proId)
                    cur=self.conn.cursor()
                    cur.execute(modifyProvince)
                    self.conn.commit()
                    
                    if cur.rowcount>0:
                        print("Province updated successfully...")
                    else:
                        print("Please provide valid province name\n...update error")
                    
                    break
                #-------------------For District------------------##

            #####task 2:Press 2 for creating/updating/deleting District
            if keyboard.is_pressed('2'):
                #for storing district
                if keyboard.is_pressed('a'):
                  provinceId = int(input("Enter province id:\n"))
                  districtId = int(input("Enter district id:\n "))
                  district = input("Enter district name:\n")
                  
                  insertData = "INSERT INTO districtDetails VALUES(%s,%s,%s)"
                  data=(provinceId,districtId,district)
                  cur = self.conn.cursor()
                  cur.execute(insertData,data)
                  self.conn.commit()
                  print("District is stored to database...")
                  break
                 
                 #for viewing district
                elif keyboard.is_pressed('b'):
                    print("---->District available in our database are listed as:")
                    cur=self.conn.cursor()
                    cur.execute("SELECT * FROM districtDetails;")
                    showDistrict = cur.fetchall()
                    for x in showDistrict:
                        print(x)
                    break
                 
                 #for updating district
                elif keyboard.is_pressed('c'):
                    print("---->Update your districts here:")
                    
                    districtId = int(input("Enter district id you want to change:\n"))
                    districtName = (input("Enter the new district name:\n"))
                    modifyProvince = "update provinceDetails set districtName='{}' where districtId='{}'".format(districtName,districtId)
                    cur=self.conn.cursor()
                    cur.execute(modifyProvince)
                    self.conn.commit()
                    
                    if cur.rowcount>0:
                        print("District updated successfully...")
                    else:
                        print("Please provide valid dstrict name\n...update error")
                    
                    break
            
            ######task 3: creating/updating/deleting municipality
            if keyboard.is_pressed('3'):
                if keyboard.is_pressed('a'):
                    print("The district that are present in database are:\n")
                    cur=self.conn.cursor()
                    cur.execute("SELECT * FROM districtDetails;")
                    showDistrict = cur.fetchall()
                    for x in showDistrict:
                        print(x)
                    print("Please provide district name:\n")
                    districtName = (input("Enter the valid district name:\n"))
                    
                    query = "SELECT district from districtDetails where district=districtName "
                    cur=self.conn.cursor()
                    cur.execute(query)
                    self.conn.commit()
                    if cur.rowcount==0:
                        print("please provide valid distric name as listed\n")

                elif keyboard.is_pressed('b'):
                    print("---->Update your municipality here:")
                    
                    MunicId = int(input("Enter municipality id you want to change:\n"))
                    municipality = (input("Enter the new municipality name:\n"))
                    modifyMunic = "update provinceDetails set municipality='{}' where MunicId='{}'".format(municipality,MunicId)
                    cur=self.conn.cursor()
                    cur.execute(modifyMunici)
                    self.conn.commit()
                    
                    if cur.rowcount>0:
                        print("Municipality updated successfully...")
                    else:
                        print("Please provide valid Municipality name\n...update error")
                    
                    break
                
                elif keyboard.is_pressed('c'):
                    print("The municipality available in the list are:\n")
                    cur.self.conn.cursor()
                    cur.execute("SELECT * FROM municipalityDetails;")
                    sgowMunicipality = cur.fetchall()
                    for x in showMunicipality:
                        print(x)
                    print("Please provide municipality name:\n ")
                    municName=(input("Enter the valid municipality name:\n"))

                    query = ("SELECT municipality from municipalityDetails where municipality='{}'").format(municName)  
                    cur=self.conn.cursor()
                    cur.execute(query)
                    self.conn.commit()
                    if cur.rowcount==0:
                        print("please provide valid municipality name as listed\n")
                    break
            
            ## task 4: press 4 for listing province district

            if keyboard.is_pressed('4'):
                print("---->Province available in our database are listed as:\n")
                cur=self.conn.cursor()
                cur.execute("SELECT * FROM provinceDetails;")
                showProvince = cur.fetchall()
                for x in showProvince:
                    print(x)
                province = (input("Enter the province name to list the district associated with it:\n"))
                query = "SELECT district FROM province where province='{}';".format(province)
                cur=self.conn.cursor()
                cur.execute(query)
                self.conn.commit()
                if cur.rowcount==0:
                    print("please provide valid province name\n")
                break

            ## task 5: press 5 for listing District Municipality

            if keyboard.is_pressed('5'):
                print("--->The availabe district in our database are:\n")
                cur=self.conn.cursor()
                cur.execute("SELECT * FROM districtDetails;")
                showDistrict = cur.fetchall()
                for x in showDistrict:
                    print(x)
                district = (input("Enter the valid distric name:\n"))
                query="SELECT municipality FROM districtDetails where district='{}' ".format(district)
                cur=self.conn.cursor()
                cur.execute(query)
                self.conn.commit()
                if cur.rowcount==0:
                    print("please provide valid district name\n")
                break 


          except:
              break  


# calling the db connector
helper = DBHelper()        