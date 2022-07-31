import pymysql

class Client:
    def __init__(self):
        self.connection=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bank"
        )
        self.cursor=self.connection.cursor()
    
    def register_client(self,name, last_name, rut, city, direction, phone, email, pswrd, pswrd2):
        sql = "INSERT INTO client(name, last_name, rut, city, direction, phone, email, pswrd, pswrd2) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name, last_name, rut, city, direction, phone, email, pswrd, pswrd2)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise
        
    def modify_name(self, name, rut):
        sql = "UPDATE client SET name='{}' WHERE rut='{}'".format(name, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def modify_last_name(self, last_name, rut):
        sql = "UPDATE client SET last_name='{}' WHERE rut='{}'".format(last_name, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def modify_rut(self, ruts, rut):
        sql = "UPDATE client SET rut='{}' WHERE rut='{}'".format(ruts, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def modify_city(self, city, rut):
        sql = "UPDATE client SET city='{}' WHERE rut='{}'".format(city, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise

    def modify_direction(self, direction, rut):
        sql = "UPDATE client SET direction='{}' WHERE rut='{}'".format(direction, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def modify_phone(self, phone, rut):
        sql = "UPDATE client SET phone='{}' WHERE rut='{}'".format(phone, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise
    
    def modify_email(self, email, rut):
        sql = "UPDATE client SET email='{}' WHERE rut='{}'".format(email, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise

    def modify_pswrd(self, pswrd, rut):
        sql = "UPDATE client SET pswrd='{}' WHERE rut='{}'".format(pswrd, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def delete_client(self, rut):
        sql = "DELETE FROM client WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise
    
    def consultation_client(self, rut):
        sql = "SELECT * FROM client WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            clte = self.cursor.fetchone()

            print("-----------------------------------")
            print("Name: ", clte[1])
            print("Last name: ", clte[2])
            print("Rut: ", clte[3])
            print("City: ", clte[4])
            print("Direction: ", clte[5])
            print("Phone ", clte[6])
            print("Email: ", clte[7])
            print("-----------------------------------")

        except Exception as e:
            raise
    
    
    def consultation_rut(self, rut):
        sql = "SELECT rut FROM client WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            self.cursor.fetchone()

        except Exception as e:
            raise


    def confirm_login(self, rut):
        sql = "SELECT pswrd FROM client WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            self.cursor.fetchone()
  
        except Exception as e:
            raise

    def confirm_pswrd(self, rut):
        sql = "SELECT pswrd2 FROM client WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            self.cursor.fetchone()

        except Exception as e:
            raise

    def update_pswrd(self, pswrd2, rut):
        sql = "UPDATE client SET pswrd2='{}' WHERE rut='{}'".format(pswrd2, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def consultation_registrations(self):
        sql = "SELECT * FROM client"
        try:
            self.cursor.execute(sql)
            cltes = self.cursor.fetchall()

            for clte in cltes:

                    print("-----------------------------------")
                    print("Name: ", clte[1])
                    print("Last name: ", clte[2])
                    print("Rut: ", clte[3])
                    print("City: ", clte[4])
                    print("Direction: ", clte[5])
                    print("Phone ", clte[6])
                    print("Email: ", clte[7])
                    print("-----------------------------------")

        except Exception as e:
            raise

client=Client()
