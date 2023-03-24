# Mod 2 Homework: Accounts
## Goal
In this assignment you will implement a class hierarchy with one base and two derived classes. The hierarchy will facilitate management of hypothetical bank accounts in a place called Strangeland. The common functionality will be implemented in the parent class, while any specialized code will be owned by the derived classes. You will see in this way multiple examples of the "is a" and "has a" relationships as well as methods of reusing the code already written. All this will be done in order to solve a problem that is quite similar to those encountered in practice.


## The Problem
In a country called Strangeland a bank offered exceptional rates on their deposit accounts. The checking account paid 5%, while the savings account 10% per annum. Here are the conditions they offered

 * There were only two types of accounts: checking and savings. In all accounts the money was held for exactly 1 year.
 * A checking account's minimum was $100, while for a savings account the minimum was $1000. When a customer fell below the minimum their account was considered in bad standing.
 * Since rewards of a savings account were greater than those of a checking account, the bank allowed only one withdrawal from a savings account.
 * Because of a rush in money laundering lawsuits against the bank, all of which involved frequent deposits to checking accounts, the bank limited deposits to checking accounts to only 5 throughout the year. 
 * At the end of the year both types of accounts paid interest only on the minimum amount held during the year. For example, if the amounts held in a savings account throughout the year were 1000, 800, 1200, then the amount 800 x 0.05 was added to a customer's holdings at the end of the year: 1200 + 800 x 0.1 = 1280. The savings account required a higher minimum and thus offered the rate of 10%. The checking account offered only 5%.
 * To reward the savings account owners, the bank added additional bonus of 15% (calculated off of the minimum amount held throughout the year) PLUS a fixed amount of $100. Hence, for example, if the holdings were as before, 1000, 800, 1200, the owner of a savings account got 1200 + 800 x 0.1 + 800 x 0.15 + 100 = 1500.

 
The bank needed a Python programmer to implement all these conditions and hired you.


## Your Approach
As shown in the image link below you decided to create a parent class `Account` which holds the functionality common to both the checking and savings accounts (the `Account` was not meant to be instantiated by itself, but you decided not to enforce that initially counting on other programmers' heeding your comments to that effect). Then you derived from `Account` the `CheckingAccount` and `SavingsAccount` classes which hold the functionality particular to those accounts.

[Please see the image of the employed class hierarchy](https://drive.google.com/file/d/1YunaYbIZyf8Iq7nHxu_hnc0JSqJmh21e/view?usp=sharing)

 * Note that since only the savings account was "interested" in the number of withdrawals, you decided to put `_num_withdrawals` member in the `SavingsAccount` and not in the base class. Similarly, the `_num_deposits` variable is in the `CheckingAccount` because only that account was interested in tracking of the deposits.
 * An account is active after creation and becomes inactive once it is closed.

## `Accounts.py`
This file contains a skeleton of the `Account` class and the derived classes `CheckingAccount` and `SavingsAccount`. Your task is to fill that file with code which implements the account behavior described above. When implementing data members of the `Account`, `CheckingAccount`, and `SavingsAccount` classes use exactly the same names as on the diagram. Be sure to follow the instructions/hints in the mutliple comments provided in `Accounts.py`. The order in which you should code your implementation is described in the `TestAccounts` section and follows the Test Driven Development paradigm.

 * Note that an account should have an id, and we generate one using the uuid module's function uuid.uuid4() and then, for clarity, take only the first 5 characters of the produced id. There is no need to modify that part of code; it is included for completeness only.
 * If the `Account` class is initialized with an amount smaller than the minimum, we throw the exception.
 * Since a lot of functionality has been implemented in the base class, some methods in the derived classes reuse the parent's implementations. They do so by calling the function `super()` which returns a handle to the parent class.
 

## `TestAccounts.py`

This file contains a skeleton code plus hints to create a testing script based on Python's unittest module. When working on this assignment, follow the steps indicated in the comments. Each step asks to create a testing block in `TestAccounts.py`, and then to write code in `Accounts.py` that passes that block. Strive to implement the minimal functionality that is necessary to pass the current test block. Then proceed to the next step indicated in the `TestAccounts.py` file. This way you will follow the TDD approach in which you will first write tests for unimplemented code (causing Python generate a lot of "red" errors), then implement the required functionality (causing Python generate a "green" success compilation statement), and finally you will spruce your code by removing any duplications or inefficiencies. 


## Submitting
At a minimum, submit the following files:
   * `Accounts.py`
   * `TestAccounts.py`

Students must submit to Mimir individually by the due date (typically, the Wednesday after this module at 11:59 pm EST) to receive credit.

## Grading

* 50 - `Accounts.py`
* 50 - `TestAccounts.py`

## Feedback
If you have any feedback on this assignment, please leave it [here](https://s.uconn.edu/cse2050_feedback).

We check this feedback regularly, and it has resulted in many improvements.
