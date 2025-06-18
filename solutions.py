
def greet(name: str) -> str:
  """Function produces a greeting string with. It uses an f-string in the
  return statement, that inserts the value of parameter {name} to the 
  produced string."""
  return f"Hello {name}. How are you?"

# Create a list of friends to use in the next method. It would be nice if your 
# list was not the same as mine -- unless you are into LOTR as much as I am
# and you can prove it by reciting the One Ring's Tengwar in Black Speech.
my_friends = ["Frodo", "Sam", "Gandalf", "Saruman", "Elrond"]


def greet_friends(friends: list[str]) -> None:
  """Function takes a list of strings, parses it one string at a time, and
  passes the strign to the greet function whose output is then passed to
  the print statement, for display."""
  for name in friends:
    print(greet(name))


# We need the math module to computer square roots
import math

def solve_quadratic(a: float, b: float, c: float) -> None:
  """Basic solution to the quadratic equation. The equation
  a*x*x + b*x + c = 0
  has solutions in the real numbers if its discriminant is not negative.
  The discriminant is the quantity b*b-4*a*c. The function below computes
  the discriminant first. It then checks its sign -- if it's negative, the
  function prints "no real solutions" and stops. If the discriminant is not
  negative, the function computes the two solutions for the equation and 
  prints them. """
  # Compute the discriminant -- it's important to determine if the equation 
  # has no real solutions
  discriminant = b * b - 4 * a * c
  # Check for real solutions
  if discriminant < 0:
    print ("no real solutions")
  else:
    # Group common operations together
    common_factor = math.sqrt(discriminant)/(2*a)
    x1 = - b + common_factor # alternative x1 = (-b + math.sqrt(discriminant))/(2*a)
    x2 = - b - common_factor # alternative x2 = (-b - math.sqrt(discriminant))/(2*a)
    print(f"{x1=}\n{x2=}")

  def draw_diamond(height):
    # I drew a few on paper first and noticed that:
    # - The middle line has the most hashes
    # - The number of spaces goes down until the middle, then goes back up
    # - The number of hashes goes up by 2 until the middle, then down by 2

    mid = height // 2  # This is the middle line (like line 2 in a 5-line diamond)

    for i in range(height):
        if i <= mid:
            # Top half of the diamond, including the middle line
            num_spaces = mid - i
            num_hashes = i * 2 + 1
        else:
            # Bottom half of the diamond
            num_spaces = i - mid
            num_hashes = (height - i - 1) * 2 + 1

        # Build the full line by adding the correct number of spaces first, then the hash marks
        line = " " * num_spaces + "#" * num_hashes
        print(line)

  def draw_right_triangle(height):
    # The first line starts with 1 hash mark
    # Each line after adds one more hash
    # The triangle is aligned to the left and grows line by line

    for i in range(1, height + 1):
        # Print i hash marks for the current line
        # This builds the triangle from top (1 hash) to bottom (height hashes)
        print("#" * i)

def compound_interest(principal, rate, years):
    # This function adds interest to the starting amount once per year.
    # That interest is added to the principal, the new total is used to get the next year's interest.
    # This creates compound growth, where each year grows from the last.

    for i in range(1, years + 1):
        # Find interest for this year
        interest = principal * rate
        # Add the interest to the current total
        principal = principal + interest
        print(f"After year {i}: {principal:.2f}")

    return principal

def draw_hollow_square(size, thickness):
    # This function makes a square with a thick border and an empty middle.
    # The top and bottom parts are just full lines of hashes.
    # The lines in the middle only have hashes on the left and right sides.

    for i in range(size):
        if i < thickness or i >= size - thickness:
            # Top or bottom border lines
            print("#" * size)
        else:
            # Middle lines with spaces in the center
            side = "#" * thickness
            middle_space = " " * (size - 2 * thickness)
            print(side + middle_space + side)

# Basic testing - This assignment 
draw_diamond(5)
draw_right_triangle(5)
compound_interest(1000, 0.05, 5)
draw_hollow_square(8, 2)

# Basic testing
solve_quadratic(1,2,3)
solve_quadratic(1,5,1)
greet_friends(my_friends)

Reflection

I noticed a few differences in my code that helped me understand what I can improve.

F-strings:
In my original greet function, I used the `format()` method to build the string:
    return "Hello {}. How are you?".format(name)
I did not use an f-string, mostly because I wasn’t sure how they worked. Now I understand that an f-string is a cleaner and more readable way to have variables directly inside a string. For example:
    return f"Hello {name}. How are you?"
does the same thing but is easier to write and understand. I also learned that f-strings work with harder expressions too, like:
    f"The result is {5 + 3}"
which would print: The result is 8. I now feel more confident using f-strings. 

For-loops and lists:
I already used a for loop to go through a list of names, like this:
    for friend in friend_list:
        print(greet(friend))
But looking at the solution, I now better understand what’s happening. The loop goes one item at a time, and on each loop, the variable (friend) takes on the value of the current item in the list. I realize I could describe this process more clearly and even use type hints like list[str] to make my function more readable and specific.

Discriminant and repeated calculations:
In my solution for the quadratic equation, I calculated the discriminant as:
    d = b**2 - 4*a*c
But I used the formula directly again later inside the square root instead of storing the value. In the posted solution, the discriminant is saved in a variable and reused. This makes the code cleaner and easier to follow, and also stops repeating the same operation multiple times. Good habit I will try to follow going forward.

Comments:
Also I did not include any comments in my original code. The solutions.py file had good examples of helpful, non-trivial comments like:
    # compute the discriminant to use later for finding the real solutions
I now understand that comments should not  just restate the code, but should explain why something is happening. In my new code for this assignment, I tried to include comments that explain my logic more clearly.

Overall, reviewing the posted solutions helped me understand not just what works in Python, but how to write code that is more readable and easy to understand.
"""