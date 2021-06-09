class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        '''
        Returns a string that represents the shape using lines of \*. The number of lines should be equal to
        the height and the number of \* in each line should be equal to the width. There should be a new line
        at the end of each line. If the width or height is larger than 50, return string "Too big for picture"
        '''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            output = ''
            for i in range(self.height):
                output += ('*' * self.width + '\n')
                i += 1
            return output

    def get_amount_inside(self, shape):
        '''
        Returns the number of times the passed in shape could fit inside the shape. Ex: a rectangle with a width
        of 4 and a height of 8 could fit in 2 sqaures with sides of 4
        '''



class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def set_side(self, side_length):
        super().set_width(side_length)
        super().set_height(side_length)