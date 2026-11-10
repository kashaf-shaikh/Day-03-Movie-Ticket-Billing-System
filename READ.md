# Day 03 - Movie Ticket Billing System

This is my Day 3 project from Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

In this project, I created a simple Movie Ticket Billing System using Python. It asks the user for their age and ticket type. It also checks if they want popcorn and calculates the final bill after applying an age-based discount.

## About the Project

The program has two types of movie tickets:

| Ticket Type | Price |
|---|---:|
| Regular (R) | $10 |
| Premium (P) | $15 |

### Age Discounts

| Age | Discount |
|---|---:|
| Below 13 | $3 |
| 60 or above | $2 |
| Other ages | No discount |

If the user wants popcorn, an extra $5 is added to the bill.

## Example

**Input:**

```text
What is your age?
65

What type of ticket do you want?
R

Do you want popcorn while watching a movie?
Y
```

**Output:**

```text
======= Final Bill ==========

Ticket: R
Popcorn: Y
Before Discount: $15
After Discount of 2
Final Bill: $13
```

## What I Learned

While making this project, I learned:

- Taking user input using `input()`.
- Converting values using `int()`.
- Using `if`, `elif` and `else`.
- Working with nested if statements.
- Using logical operators like `or`.
- Converting text to uppercase using `upper()`.
- Understanding `None` and `is None`.
- Updating variables using `+=`.
- Using conditions to calculate the final bill.

## Technologies Used

- Python 3
- PyCharm
- Git
- GitHub

## How to Run

1. Clone or download this repository.
2. Open the project folder in PyCharm or any Python editor.
3. Open `main.py`.
4. Run the program.
5. Enter your age, ticket type and popcorn choice.

You can also run it from the terminal:

```bash
python main.py
```

## Project Structure

```text
Day-03-Movie-Ticket-Billing-System/
│
├── main.py
│
└── README.md
```

## About My Learning

This is my third project in the 100 Days of Python course. I am learning Python by practising different concepts and making small projects every day.

I will keep uploading my daily projects to GitHub as I continue learning.