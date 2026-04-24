import customtkinter as ctk 
from PIL import Image, ImageSequence
import math
import re
from sympy import SympifyError, symbols, Eq, solve, sympify
after_id=None

window = ctk.CTk()
window.title('Showcase Algebra Calculator')
window.geometry("480x615")

def main_menu():
    global after_id
    if after_id:
        window.after_cancel(after_id)
    for widget in window.winfo_children():
        widget.destroy()
    
    frames = []
    gif = Image.open("Glitch_number.gif")
    for frame in ImageSequence.Iterator(gif):
        frame = frame.copy().convert("RGBA")
        r, g, b, a = frame.split()
        a = a.point(lambda x: x * 0.4)  
        frame.putalpha(a)
        frames.append(ctk.CTkImage(frame, size=(500, 615)))

    bg_label = ctk.CTkLabel(window, text="")
    bg_label.place(x=0, y=0)

    def animate(frame_index=0):
        global after_id
        bg_label.configure(image=frames[frame_index])
        after_id = window.after(20, animate, (frame_index + 1) % len(frames))
    animate()
    area_img = ctk.CTkImage(Image.open("Areaofcircle.png"), size=(100, 100))
    ctk.CTkButton(window, text='Calculate the \narea of a shape', command=calculate_area, width=223, height=223, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 12.5), image=area_img, compound = "top").place(x=10, y=46)
    quadratic_img = ctk.CTkImage(Image.open("quadratic.png"), size=(136, 51))
    ctk.CTkButton(window, text='Solve a \nquadratic \nequation', command=solve_quadratic, width=223, height=223, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 14), image=quadratic_img, compound='top' ).place(x=245, y=46)
    factorial_img = ctk.CTkImage(Image.open("Factorial.png"), size=(130, 130) )
    ctk.CTkButton(window, text='Calculate the \nfactorial \nof a number', command=calculate_factorial, width=223, height=223, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 12.5), image= factorial_img, compound='top').place(x=10, y=288)
    algebra_img  = ctk.CTkImage(Image.open ("Algebra_expression.png"), size=(180, 90))
    ctk.CTkButton(window, text='Solve an \nalgebraic \nexpression', command=solve_algebraic_expression, width=223, height=223, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 14), image= algebra_img, compound= "top").place(x=245, y=288)
    ctk.CTkButton(window, text='Exit', command=window.destroy, width=100, height=50, fg_color="#101111", border_color="#ffffff", corner_radius=10, bg_color='transparent', border_width=2.5, hover_color="#555555", font= ('Press Start 2P', 18)).place(x=187.5, y=535)  

def calculate_area():
    global after_id
    if after_id:
        window.after_cancel(after_id)
    for widget in window.winfo_children():
        widget.destroy()

    frames = []
    gif = Image.open("Glitch_number.gif")
    for frame in ImageSequence.Iterator(gif):
        frame = frame.copy().convert("RGBA")
        r, g, b, a = frame.split()
        a = a.point(lambda x: x * 0.4) 
        frame.putalpha(a)
        frames.append(ctk.CTkImage(frame, size=(500, 615)))

    bg_label = ctk.CTkLabel(window, text="")
    bg_label.place(x=0, y=0)

    def animate(frame_index=0):
        global after_id
        bg_label.configure(image=frames[frame_index])
        after_id = window.after(20, animate, (frame_index + 1) % len(frames))
    animate()
    area_img = ctk.CTkImage(Image.open("Areaofcircle.png"), size=(100, 100))
    ctk.CTkButton(window, text='Circle', command=go_to_circle_area, width=145, height=235, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 14), image=area_img, compound="top").place(x=10, y=5)
    ctk.CTkButton(window, text='Rectangle', command=go_to_rectangle_area, width=145, height=235, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 12)).place(x=165, y=5)
    ctk.CTkButton(window, text='Right \nTriangle', command=go_to_right_triangle_area, width =145, height=235, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 14) ).place(x=325 , y=5)
    ctk.CTkButton(window, text='Regular \nTriangle', command=go_to_regular_triangle_area, width=145, height=235, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 14)).place (x=66.16, y=250)
    ctk.CTkButton(window, text='Regular \nPolygon', command=go_to_regular_polygon_area, width=145, height=235, fg_color="#101111", border_color="#ffffff", corner_radius=20, bg_color='transparent', border_width=2.5, hover_color="#555555", font=('Press Start 2P', 14)).place(x=263.8, y=250)
    ctk.CTkButton(window, text='Exit', command=main_menu, width=100, height=50, fg_color="#101111", border_color="#ffffff", corner_radius=10, bg_color='transparent', border_width=2.5, hover_color="#555555", font= ('Press Start 2P', 18)).place(x=187.5, y=535)

from sympy import symbols, Eq, solve, sympify, SympifyError
import re

def solve_algebraic_expression():
    for widget in window.winfo_children():
        widget.destroy()
    ctk.CTkLabel(window, text='Enter an algebraic expression to solve (Use x as the variable)').pack(pady=10)
    expression_entry = ctk.CTkEntry(window, placeholder_text='Enter expression')
    expression_entry.pack(pady=10)
    result_label = ctk.CTkLabel(window, text='')
    result_label.pack(pady=10)
    ctk.CTkButton(window, text='Return to Main Menu', command=main_menu).pack(pady=10)
    ctk.CTkButton(window, text='Solve Expression', command=lambda: solve_and_display_expression(expression_entry.get(), result_label)).pack(pady=10)

def solve_and_display_expression(expression, result_label):
    try:
        x = symbols('x')
        expression = re.sub(r'(\d)(x)', r'\1*\2', expression)
        left_side, right_side = expression.split('=')
        equation = Eq(sympify(left_side), sympify(right_side))
        solution = solve(equation, x)
        if solution:
            result_label.configure(text=f'The value of x is: {solution[0]}')
        else:
            result_label.configure(text='No solution found.')
    except (ValueError, SympifyError):
        result_label.configure(text='Invalid input. Please enter a valid algebraic expression or use x as the variable.')

def calculate_factorial():
    for widget in window.winfo_children():
        widget.destroy()
    ctk.CTkLabel(window, text='Enter a non-negative integer to calculate its factorial').pack(pady=10)
    factorial_entry = ctk.CTkEntry(window, placeholder_text='Enter number')
    factorial_entry.pack(pady=10)
    ctk.CTkButton(window, text='Return to Main Menu', command=main_menu).pack(pady=10)
    ctk.CTkButton(window, text='Calculate Factorial', command=lambda: calculate_and_display_factorial(factorial_entry.get())).pack(pady=10)

def calculate_and_display_factorial(n):
    try:
        n = int(n)
        if n < 0:
            ctk.CTkLabel(window, text='Invalid input. Please enter a non-negative integer.').pack(pady=10)
            return
        factorial = math.factorial(n)
        ctk.CTkLabel(window, text=f'The factorial of {n} is: {factorial}').pack(pady=10)
    except ValueError:
        ctk.CTkLabel(window, text='Invalid input. Please enter a non-negative integer.').pack(pady=10)

def solve_quadratic():
    for widget in window.winfo_children():
        widget.destroy()
    ctk.CTkLabel(window, text='Enter the coefficients of the quadratic equation ax^2 + bx + c = 0').pack(pady=10)
    a_entry = ctk.CTkEntry(window, placeholder_text='a')
    a_entry.pack(pady=10)
    b_entry = ctk.CTkEntry(window, placeholder_text='b')
    b_entry.pack(pady=10)
    c_entry = ctk.CTkEntry(window, placeholder_text='c')
    c_entry.pack(pady=10)
    ctk.CTkButton(window, text='Return to Main Menu', command=main_menu).pack(pady=10)
    ctk.CTkButton(window, text='Solve Equation', command=lambda: solve_equation(a_entry.get(), b_entry.get(), c_entry.get())).pack(pady=10)

def solve_equation(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a == 0:
            ctk.CTkLabel(window, text='Coefficient a cannot be 0.').pack(pady=10)
            return
        x = symbols('x')
        equation = Eq(a * x**2 + b * x + c, 0)
        solutions = solve(equation, x)
        ctk.CTkLabel(window, text=f'The solutions are: {solutions}').pack(pady=10)
    except ValueError:
        ctk.CTkLabel(window, text='Invalid input.').pack(pady=10)
# the classes in order of logic code
class regular_polygon_area(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.area = 0
        self.num_sides_label = ctk.CTkLabel(self, text='Enter the number of sides of the regular polygon')
        self.num_sides_label.pack(pady=10)
        self.num_sides_entry = ctk.CTkEntry(self, placeholder_text='Number of sides')
        self.num_sides_entry.pack(pady=10)
        self.side_length_label = ctk.CTkLabel(self, text='Enter the length of one side of the regular polygon')
        self.side_length_label.pack(pady=10)
        self.side_length_entry = ctk.CTkEntry(self, placeholder_text='Side length')
        self.side_length_entry.pack(pady=10)
        self.apothem_label = ctk.CTkLabel(self, text='Enter the apothem of the regular polygon')
        self.apothem_label.pack(pady=10)
        self.apothem_entry = ctk.CTkEntry(self, placeholder_text='Apothem')
        self.apothem_entry.pack(pady=10)
        self.result_label = ctk.CTkLabel(self, text='')
        self.result_label.pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)

    def calculate_area(self):
        try:
            num_sides = int(self.num_sides_entry.get())
            side_length = float(self.side_length_entry.get())
            apothem = float(self.apothem_entry.get())
            if num_sides <= 0 or side_length <= 0 or apothem <= 0:
                self.result_label.configure(text='Invalid input.')
                return
            self.area = 0.5 * num_sides * side_length * apothem
            self.result_label.configure(text=f'The area of the polygon is: {round(self.area, 4)}')
        except ValueError:
            self.result_label.configure(text='Invalid input.')

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()
class regular_triangle_area(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.area = 0
        self.side_1_label = ctk.CTkLabel(self, text='Enter the first side length of the triangle')
        self.side_1_label.pack(pady=10)
        self.side_1_entry = ctk.CTkEntry(self, placeholder_text='Side 1')
        self.side_1_entry.pack(pady=10)
        self.side_2_label = ctk.CTkLabel(self, text='Enter the second side length of the triangle')
        self.side_2_label.pack(pady=10)
        self.side_2_entry = ctk.CTkEntry(self, placeholder_text='Side 2')
        self.side_2_entry.pack(pady=10)
        self.angle_label = ctk.CTkLabel(self, text='Enter the angle between the sides in degrees')
        self.angle_label.pack(pady=10)
        self.angle_entry = ctk.CTkEntry(self, placeholder_text='Angle')
        self.angle_entry.pack(pady=10)
        ctk.CTkLabel(self, text='Would you like to round to the nearest tenth (1), hundredth (2), or thousandth (3)?').pack(pady=10)
        self.round_entry = ctk.CTkEntry(self, placeholder_text='Round to')
        self.round_entry.pack(pady=10)
        self.result_label = ctk.CTkLabel(self, text='')
        self.result_label.pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)
        ctk.CTkButton(self, text='Round Area', command=self.round_area).pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)

    def calculate_area(self):
        try:
            side_1 = float(self.side_1_entry.get())
            side_2 = float(self.side_2_entry.get())
            angle = float(self.angle_entry.get())
            if side_1 <= 0 or side_2 <= 0 or angle < 0 or angle > 180:
                self.result_label.configure(text='Invalid input.')
                return
            self.area = 0.5 * side_1 * side_2 * math.sin(math.radians(angle))
            self.result_label.configure(text=f'The area of the triangle is: {round(self.area, 4)}')
        except ValueError:
            self.result_label.configure(text='Invalid input.')

    def round_area(self):
        if self.area == 0:
            self.result_label.configure(text='Calculate area first.')
            return
        if self.round_entry.get() == 'tenth' or self.round_entry.get() == '1':
            self.result_label.configure(text=f'Area rounded to the nearest tenth: {round(self.area, 1)}')
        elif self.round_entry.get() == 'hundredth' or self.round_entry.get() == '2':
            self.result_label.configure(text=f'Area rounded to the nearest hundredth: {round(self.area, 2)}')
        elif self.round_entry.get() == 'thousandth' or self.round_entry.get() == '3':
            self.result_label.configure(text=f'Area rounded to the nearest thousandth: {round(self.area, 3)}')
        else:
            self.result_label.configure(text='Invalid input. Please enter tenth, hundredth, or thousandth.')

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()

class right_triangle_area(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_label = ctk.CTkLabel(self, text='Enter the base of the triangle')
        self.base_label.pack(pady=10)
        self.base_entry = ctk.CTkEntry(self, placeholder_text='Base')
        self.base_entry.pack(pady=10)
        self.height_entry = ctk.CTkEntry(self, placeholder_text='Height')
        self.height_label = ctk.CTkLabel(self, text='Enter the height of the triangle')
        self.height_label.pack(pady=10)
        self.height_entry.pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)

    def calculate_area(self):
        try:
            base = float(self.base_entry.get())
            height = float(self.height_entry.get())
            if base <= 0 or height <= 0:
                ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)
                return
            area = 0.5 * base * height
            ctk.CTkLabel(self, text=f'The area of the triangle is: {round(area, 4)}').pack(pady=10)
        except ValueError:
            ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()

class rectangle_area(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.length_entry = ctk.CTkEntry(self, placeholder_text='Length')
        self.length_label = ctk.CTkLabel(self, text='Enter the length of the rectangle')
        self.length_label.pack(pady=10)
        self.length_entry.pack(pady=10)
        self.width_entry = ctk.CTkEntry(self, placeholder_text='Width')
        self.width_label = ctk.CTkLabel(self, text='Enter the width of the rectangle')
        self.width_label.pack(pady=10)
        self.width_entry.pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)

    def calculate_area(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            if length <= 0 or width <= 0:
                ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)
                return
            area = length * width
            ctk.CTkLabel(self, text=f'The area of the rectangle is: {round(area, 4)}').pack(pady=10)
        except ValueError:
            ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()

class CircleArea(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.radius_entry = ctk.CTkEntry(self, placeholder_text='Enter radius')
        self.radius_label = ctk.CTkLabel(self, text='Enter the radius of the circle')
        self.radius_label.pack(pady=10)
        self.radius_entry.pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)

    def calculate_area(self):
        try:
            radius = float(self.radius_entry.get())
            if radius <= 0:
                ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)
                return
            area = math.pi * radius ** 2
            ctk.CTkLabel(self, text=f'The area of the circle is: {round(area, 4)}').pack(pady=10)
        except ValueError:
            ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()

def go_to_circle_area():
    for widget in window.winfo_children():
        widget.destroy()
    CircleArea(window).pack(fill="both", expand=True)

def go_to_rectangle_area():
    for widget in window.winfo_children():
        widget.destroy()
    rectangle_area(window).pack(fill="both", expand=True)

def go_to_right_triangle_area():
    for widget in window.winfo_children():
        widget.destroy()
    right_triangle_area(window).pack(fill="both", expand=True)

def go_to_regular_triangle_area():
    for widget in window.winfo_children():
        widget.destroy()
    regular_triangle_area(window).pack(fill="both", expand=True)

def go_to_regular_polygon_area():
    for widget in window.winfo_children():
        widget.destroy()
    regular_polygon_area(window).pack(fill="both", expand=True)

main_menu()
window.mainloop()