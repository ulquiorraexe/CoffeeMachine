# Coffee Machine

This is a simple coffee machine simulation that allows users to choose from a selection of drinks, pay for them, and check the resources available. The program handles inventory (water, milk, coffee) and the cost of each drink.

## Project Overview

The coffee machine provides three types of coffee:

- **Espresso**
- **Latte**
- **Cappuccino**

Each coffee type requires different amounts of ingredients (water, milk, coffee) and has a specific cost. Users can:

- Choose their drink
- Pay using coins (quarters, dimes, nickels, pennies)
- Receive their coffee if there are enough resources available
- Get a report on available resources at any time

## Features

- **Check resources**: Displays the current stock of ingredients (water, milk, coffee).
- **Check money**: Handles the payment for drinks and provides change if necessary.
- **Make coffee**: Subtracts ingredients from stock and gives the user the coffee they selected.
- **End session**: Allows users to stop the machine at any time by typing "off".

## Installation

You can clone this repository to your local machine by running:

```bash
git clone https://github.com/ulquiorraexe/coffee-machine.git
```
After cloning, simply run the `main.py` file.
```bash
python main.py
```

## Usage

Once the program is running, you'll be able to:
  1. **Choose a drink:** Type one of the following options:
     - `espresso`
     - `latte`
     - `cappucino`
  2. **Check resources:** Type `report` to see the remaining resources.
  3. **End session:** Type `off` to turn off the machine.

## Payment Process

When a drink is selected, the user will be asked to insert coins. The program accepts:
  - **Quarters:** 0.25 each
  - **Dimes:** 0.10 each
  - **Nickels:** 0.05 each
  - **Pennies:** 0.01 each
After the payment is received, the program checks if it covers the cost of the selected drink. If not enough mooney is inserted, the program will request the user to insert more coins.

### Example Interaction:
```swift
What would you like? (espresso/latte/cappuccino) espresso
How many quarters? 2
How many dimes? 1
How many nickles? 1
How many pennies? 0
Here is $1.56 in change.
Here is espresso, bon appétit!
```

## Code Explanation

- `MENU`: A dictionary that contains the details of each drink, including ingredients and cost.
- `resources`: A dictionary that holds the current stock of ingredients.
- `profit`: Tracks the total profit from coffee sales.
- `check_item()`: Checks if there are enough resources to make the selected drink.
- `coin_say()`: Prompts the user to input coins and calculates the total money inserted.
- `return_money()`: Checks if the user has inserted enough money and gives change if necessary.
- `make_coffee()`: Subtracts the ingredients from stock and serves the coffee.

## License 

This project does not have a license.

