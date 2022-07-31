import pymysql

class Mov: 
    def __init__(self):
        self.connection=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="banco"
        )
        self.cursor=self.connection.cursor()

    def register_deposit(self, account_number, rut, deposit, cash):
        sql = "INSERT INTO deposit(account_number, rut, deposit, cash) VALUES('{}','{}','{}','{}')".format(account_number, rut, deposit, cash)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise

    def register_extract(self, account_number, rut, extract, cash):
        sql = "INSERT INTO extract(account_number, rut, extract, cash) VALUES('{}','{}','{}','{}')".format(account_number, rut, extract, cash)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise       

    def set_deposit(self, rut):
        sql = "SELECT * FROM deposit WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            movi = self.cursor.fetchall()

            for mov in movi:
                print("-----------------------------------")
                print("Movement number: ", mov[0])
                print("Account number: ", mov[1])
                print("Client rut: ", mov[2])
                print("Deposit: ", mov[3])
                print("Cash: ", mov[4])
                print("-----------------------------------")

        except Exception as e:
            raise

    def set_extract(self, rut):
        sql = "SELECT * FROM extract WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            movi = self.cursor.fetchall()

            for mov in movi:
                print("-----------------------------------")
                print("Movement number: ", mov[0])
                print("Account number: ", mov[1])
                print("Client rut: ", mov[2])
                print("Extract: ", mov[3])
                print("Cash: ", mov[4])
                print("-----------------------------------")

        except Exception as e:
            raise
    
mov=Mov()
