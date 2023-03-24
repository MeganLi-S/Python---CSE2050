import unittest
from Accounts import Account, CheckingAccount, SavingsAccount

class TestAccounts(unittest.TestCase):
    def test_init(self):

        # 1) Implement the minimal functionality in the Accounts.py file
        #    that make the below test block pass

        a1 = CheckingAccount(120);
        self.assertEqual(a1.get_amount_held(), 120)
        self.assertEqual(a1.get_minimum(), 100)
        self.assertEqual(a1.get_min_ever_held(), 120)
        self.assertEqual(a1.get_interest_rate(), 0.05)
        self.assertEqual(a1.is_in_good_standing(), True)
        self.assertEqual(a1.is_active(), True)

        # 2)  Write a similar test as above for the SavingsAccount and then
        #     implement the required functionality in Accounts.py (implement only the
        #     minimal functionality that passes that test)
        #      *USE DIFFERENT NUMBERS*

    def test_creation_minimums(self):

        # 3) Look at the "with" block below and write a test similar to the one below to see
        #    whether the constructor for the CheckingAccount throws an exception when that
        #    account is initialized with too small a value (i.e., below the allowed minimum)
        #     *USE DIFFERENT NUMBERS*

        with self.assertRaises(ValueError):
             a2 = SavingsAccount(900)

    def test_withdrawals_and_deposits(self):

        # 4) Look at the code below and write a similar code testing CheckingAccount's
        #    deposit and withdrawal functionality. Make sure to test that after 5
        #    deposits the deposit method throws an exception by first calling
        #    for i in a range(5)
        #        a1.deposit(10)
        #    and then "depositing" one more time in the "with" block as below
        #    *USE DIFFERENT NUMBERS*

        s1 = SavingsAccount(1250);
        s1.withdraw(300);
        self.assertEqual(s1.get_amount_held(), 950);
        self.assertEqual(s1.is_in_good_standing(), False);
        self.assertEqual(s1.get_num_withdrawals(), 1);
        s1.deposit(100);
        self.assertEqual(s1.get_amount_held(), 1050);
        self.assertEqual(s1.is_in_good_standing(), True);

        with self.assertRaises(ValueError):
            s1.withdraw(25)   # For savings account cannot withdraw the second time

    def test_account_closing(self):
        a1 = CheckingAccount(1500);
        a1.withdraw(200);
        a1.deposit(700);
        self.assertEqual(a1.get_min_ever_held(), 1300)
        self.assertEqual(a1.is_active(), True)
        final_amount_c = a1.close_account();
        self.assertEqual(final_amount_c, 2065);
        self.assertEqual(a1.is_active(), False)

        # 5) Look at the code above and write a similar code testing SavingsAccount's
        #    closure functionality. Remember that Savings account has a different reward
        #    scheme from that of the Checking account
        #    *USE DIFFERENT NUMBERS*

    def test_equality(self):
        # 6) Write a test for the magic method Account.__eq__
        #    Use one line to
        #    self.assertEqual(a1 == a2, True);
        #    and one line to
        #    self.assertEqual(s1 == s1, False);
        pass;


if (__name__ == '__main__'):
    unittest.main()
