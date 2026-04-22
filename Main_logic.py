import math
import re
from sympy import symbols, Eq, solve, sympify

print('Options: \n1. Calculate the area of a shape \n2. Solve a quadratic equation \n3. Calculate the factorial of a number \n4. Solve an algebraic expression \n5. Exit')
while True:
    input_option = input('Enter the number corresponding to the option you want to choose: ').lower()

    if input_option == '5' or input_option == 'exit':
        print('Exiting the program.....')
        break
    elif input_option not in ['1', '2', '3', '4', '5']:
        print('Invalid option. Please enter a number between 1 and 5.')
        continue

    elif input_option == '1':
        shape = input('Enter the shape you want to calculate the area of (circle 1, square 2, rectangle 3, right triangle 4, regular triangle 5, regular polygon 6): ').lower()
        try:
            if shape == 'circle' or shape == '1':
                radius_input = float(input('Enter the radius of the circle: '))
                if radius_input <= 0:
                    print('Invalid input.')
                    continue
                area = math.pi * radius_input ** 2
                print(f'The area of the circle is: {area}'.upper())
            elif shape not in ['circle', '1', 'square', '2', 'rectangle', '3', 'right triangle', '4', 'regular triangle', '5', 'regular polygon', '6']:
                print('Invalid input.')
                continue
            elif shape == 'square' or shape == '2':
                side_input = float(input('Enter the side length of the square: '))
                if side_input <= 0:
                    print('Invalid input.')
                    continue
                area = side_input ** 2
                print(f'The area of the square is: {area}'.upper())
            elif shape == 'rectangle' or shape == '3':
                length_input_rectangle = float(input('Enter the length of the rectangle: '))
                width_input_rectangle = float(input('Enter the width of the rectangle: '))
                if length_input_rectangle <= 0 or width_input_rectangle <= 0:
                    print('Invalid input.')
                    continue
                area = length_input_rectangle * width_input_rectangle
                print(f'The area of the rectangle is: {area}'.upper())
            elif shape == 'right triangle' or shape == '4':
                user_base_input = float(input('Enter the base of the triangle: '))
                user_height_input = float(input('Enter the height of the triangle: '))
                area = 0.5 * user_base_input * user_height_input
                print(f'The area of the triangle is: {area}'.upper())
            elif shape == 'regular triangle' or shape == '5':
                side_input = float(input('Enter one side length of the triangle: '))
                side_2_input = float(input('Enter the second side length of the triangle: '))
                angle_input = float(input('Enter the angle between the sides in degrees: '))
                if angle_input >= 0 and angle_input <= 180 and side_input > 0 and side_2_input > 0:
                    area = 0.5 * side_input * side_2_input * math.sin(math.radians(angle_input))
                    print(f'The area of the triangle is: {area}'.upper())

                    round_question = input('Do you want to round the area to the nearest tenth 1, hundredth 2, or thousandth 3? ').lower()
                    if round_question == 'tenth' or round_question == '1':
                        area = round(area, 1)
                        print(f'The area of the triangle rounded to the nearest tenth is: {area}'.upper())
                    elif round_question == 'hundredth' or round_question == '2':
                        area = round(area, 2)
                        print(f'The area of the triangle rounded to the nearest hundredth is: {area}'.upper())
                    elif round_question == 'thousandth' or round_question == '3':
                        area = round(area, 3)
                        print(f'The area of the triangle rounded to the nearest thousandth is: {area}'.upper())
                    else:
                        print('Invalid option.')
                else:
                    print('Invalid input.')
                    continue
            elif shape == 'regular polygon' or shape == '6':
                num_sides_input = int(input('Enter the number of sides of the polygon: '))
                side_length_input = float(input('Enter the side length of the polygon: '))
                apothem_input = float(input('Enter the apothem of the polygon: '))
                perimeter = num_sides_input * side_length_input
                area = 0.5 * perimeter * apothem_input
                print(f'The area of the polygon is: {area}'.upper())
            else:
                print('Invalid shape. Please enter one of the following: circle, square, rectangle, right triangle, regular triangle, regular polygon.')
        except ValueError:
            print('Invalid numeric input.')

    elif input_option == '2': #this is the quadratic equation thingy
        try:
            a_input = float(input('Enter the coefficient a: '))
            b_input = float(input('Enter the coefficient b: '))
            c_input = float(input('Enter the coefficient c: '))

            if a_input == 0:
                print('Not a quadratic equation.'.upper())
                continue
            discriminant = b_input ** 2 - 4 * a_input * c_input
            if discriminant > 0:
                root1 = (-b_input + math.sqrt(discriminant)) / (2 * a_input)
                root2 = (-b_input - math.sqrt(discriminant)) / (2 * a_input)
                print(f'The roots are: {root1} and {root2}'.upper())
            elif discriminant == 0:
                root = -b_input / (2 * a_input)
                print(f'The root is: {root}'.upper())
            else:
                print('The equation has no real roots.'.upper())
        except ValueError:
            print('Invalid numeric input.')

    elif input_option == '3':    #this is teh factorial option
        try:
            num_input = int(input('Enter a non-negative integer: '))
            if num_input < 0:
                print('Factorial is not defined for negative numbers.'.upper())
                continue
            factorial = math.factorial(num_input)
            print(f'The factorial of {num_input} is: {factorial}'.upper())
        except ValueError:
            print('Invalid numeric input.')

    elif input_option == '4': #algebra thingy
        user_expression_input = input('Enter a simple algebraic expression (Example: 2x-3=5): ')
        if '=' not in user_expression_input:
            print('Invalid expression.')
            continue
        if 'x' not in user_expression_input:
            print('Expression must contain variable x.')
            continue
        try:
            x = symbols('x')
            left_side, right_side = user_expression_input.split('=')
            left_side = re.sub(r'(\d)(x)', r'\1*\2', left_side.strip())
            right_side = re.sub(r'(\d)(x)', r'\1*\2', right_side.strip())
            equation = Eq(sympify(left_side), sympify(right_side))
            solution = solve(equation, x)
            if solution:
                print(f'The value of x is: {solution[0]}'.upper())
            else:
                print('No solution found.'.upper())
        except Exception as e:
            print(f'Invalid expression. Error: {e}')