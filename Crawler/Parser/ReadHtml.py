class ReadHtml:


    def __init__(self, html_data: str):
        
        self.index: int = -1
        
        self.length: int = len( html_data )

        self.html_data: str = html_data


    
    def get_next_char(self, val = 1) -> chr:

        self.index += val

        if( self.index >= self.length ):

            return None

        return self.html_data[ self.index ]



    def go_to_previous_char(self, step = 1) -> None:

        self.index -= step


    
    def skip_until_match(self, char) -> None:

        while True:

            if self.html_data[self.index] == char:

                return

            self.index += 1 



    def get_data(self) -> str:

        return self.html_data



    def get_index(self) -> int:

        return self.index
