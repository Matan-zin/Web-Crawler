class Paste:

  

    def get_title(self) -> str:

        return self.title

    

    def set_title(self, title : str) -> None:

         self.title = title



    def get_author(self) -> str:

        return self.author


    
    def set_author(self, author : str) -> None:

         self.author = author
    



    def get_content(self) -> str:

        return self.content



    
    def set_content(self, content : str) -> None:

         self.content = content




    def get_date(self) -> str:

        return self.date



    
    def set_date(self, date : str) -> None:

         self.date = date



    def get_hash(self) -> str:

        return hash((self.title, self.author, self.date, self.content))



    def __str__(self):
        _str = ''
        _str += '-------------------------\n'
        _str += ('Title: ' + self.title + '\n')
        _str += ('Author: ' + self.author + '\n')
        _str += ('Date: ' + str(self.date) + '\n')
        _str += ('Contnent:\n' + self.content + '\n')
        _str += '-------------------------\n'

        return _str
