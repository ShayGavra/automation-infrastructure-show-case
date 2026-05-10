class DBActions:
    def __init__(self,data_base):
        self.data_base=data_base



    def close_db(self):
        self.data_base.close


    def get_products(self):
        query = "SELECT * FROM ProductsTable "
        my_cursor= self.data_base.cursor()
        my_cursor.execute(query)
        my_result= my_cursor.fetchall()
        return my_result
       
            
        