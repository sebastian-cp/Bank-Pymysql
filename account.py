import pymysql

class Account: 
    def __init__(self):
        self.connection=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="banco"
        )
        self.cursor=self.connection.cursor()

    def register_account(self, account_number, account_type, rut, cash):
        sql = "INSERT INTO account(account_number, account_type, rut, cash) VALUES('{}','{}','{}','{}')".format( account_number, account_type, rut, cash)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise       
    

    def delete_account(self, rut):
        sql = "DELETE FROM account WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def consultation_account(self, rut):
        sql = "SELECT * FROM account WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            acc = self.cursor.fetchone()

            print("Account number: ", acc[0])
            print("Account type: ", acc[2])
            print("Available balance:", acc[3])

        except Exception as e:
            raise

    def cash(self, rut):
        sql = "SELECT cash FROM account WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            sal = self.cursor.fetchone()

        except Exception as e:
            raise
        return sal[0]

    def deposit(self,cash, rut):
        sql = "UPDATE account SET cash='{}' WHERE rut='{}'".format(cash, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def extract(self,cash, rut):
        sql = "UPDATE account SET cash='{}' WHERE rut='{}'".format(cash, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise 

    def consultation_account_number(self, rut):
        sql = "SELECT account_number FROM account WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            acc = self.cursor.fetchone()

        except Exception as e:
            raise
        return acc[0]
    
account=Account()
