import uuid;

class Account:
    def __init__(self, initial_amount, minimum, interest_rate, good_standing = True, is_active = True):
        if (initial_amount < minimum):
            raise ValueError("When creating this account, the initial amount must be >= {}.".format(minimum))
        self._id = str(uuid.uuid4())[:5]
        self._minimum       = minimum
        self._amount_held   = initial_amount
        # Add the other data members and initialize them from the parameters of __init__
        self._interest_rate = interest_rate
        self._min_ever_held = initial_amount
        self._good_standing = good_standing
        self._is_active = is_active

    def get_amount_held(self):
        # return the amount held
        return self._amount_held

    def get_minimum(self):
        # return minimum to be held in the account
        return self._minimum

    def get_min_ever_held(self):
        # return the minimal ammount ever held
        return self._min_ever_held

    def get_interest_rate(self):
        # return the interest rate on the account
        return self._interest_rate

    def is_in_good_standing(self):
        # return the value of the boolean variable which tracks the standing of the account
        return self._good_standing

    def is_active(self):
        # return the boolean member which tracks whether the account is active
        return self._is_active

    def withdraw(self, w_amount):
        # 1) if the withdrawal amount is > than the amount held in the
        #   account throw the exception:
        #   raise ValueError("Cannot withdraw more than you have.")
        if w_amount > self.get_amount_held():
            raise ValueError("Cannot withdraw more than you have.")

        # 2) diminish the amount held in the account by the withdrawal amount
        else:
            self._amount_held -= w_amount


        # 3) if after subtracting the withdrawal amount the held amount in the account
        #    is  less than minimum -- i.e., < self._minimum, set the _good_standing member
        #    to False
        #    self._good_standing = False
        if self._amount_held < self._minimum:
        		self._good_standing = False
         

        # 4) Finally if the self._amount_held is < the minimum amount ever held
        #    adjust the _min_ever_held member
        if self._amount_held < self._min_ever_held:
        		self._min_ever_held = self._amount_held


    def deposit(self, d_amount):
        # 1) increase the amount held by the deposit amount
        self._amount_held += d_amount

        # 2) if after adding the deposit amount the amount held is > than the minimum
        #    amount to be held in the account set the _good_standing member to True
        if self._amount_held > self._minimum:
            self._good_standing = True

    def close_account(self):
        # 1) Set the _is_active member to False as the account as we are
        #    closing the account
        self._is_active = False
        # 2) Since we are closing the account we need to give the interest to
        #    the customer. Both checking and the savings accounts add
        #    (mimimal amount held througout the year) * (interest rate on the account)
        #    Hence add that amount here
        self._amount_held += (self._min_ever_held * self._interest_rate)

        # Simply return the final amount held
        return self._amount_held

    # This function is fully implemented: simply remove the first column of "#" signs and
    # correct indentation. Do that as the last step in your solution process
    def __lt__(self, other):
        if not (isinstance(self, Account) and isinstance(other, Account)):
           raise TypeError
        # # Are we comparing accounts of the same type?
        if (self._interest_rate == other._interest_rate):
        	return ( self._min_ever_held <= self._min_ever_held )
        else:
          raise TypeError("Cannot compare checking accounts with savings accounts.")
  

    def __eq__(self, other):
        if not (isinstance(self, Account) and isinstance(other, Account)):
            raise TypeError

        # Declare accounts equal if simultaneously their amounts held are equal,
        # their minimum amounts every held are equal, and their interest rates are equal

        if self._amount_held == other._amount_held:
            return True
        else:
            return False
        

class CheckingAccount(Account):
    def __init__(self, initial_amount, max_num_deposits = 5,
                       minimum = 100, interest_rate = 0.05, num_deposits=0):
        # Notice how we call here the parent's constructor to initialize
        # all the necessary data members
        super().__init__(initial_amount, minimum , interest_rate)
        self._max_num_deposits = max_num_deposits
        self._num_deposits = num_deposits
        # Set the members of "self" for the maximal number of allowed deposits and for the
        # number of deposits so far
        

    def get_num_deposits(self):
        # return the number of deposits
        return self._num_deposits
        

    def deposit(self, d_amount):
        # 1) if the number of deposits is >= than maximal number of deposits allowed
        #  raise an exception:
        #  raise ValueError("Checking accounts allow only {} deposits.".format(self._max_num_deposits))
        if self._num_deposits >= self._max_num_deposits:
            raise ValueError("Checking accounts allow only {} deposits.".format(self._max_num_deposits))

        # 2) call the parent's implementation of the deposit method as that implementation
        #    already does a bunch of things we need
        super().deposit(d_amount)

        # 3) increment the number of deposits by 1
        self._num_deposits += 1
        

    # Below, fill out the empty strings with suitable data members to be printed
    def __str__(self):
        return \
            "\n********************************\n" \
            " id = {}\n amount held = {}\n min. amount held = {}\n" \
            " good standing = {}\n num. deposits = {}\n interest_rate = {}\n" \
            " is active = {}".format(self._id, self._amount_held, self._min_ever_held,
                                                self._good_standing, self._num_deposits,
                                                self._interest_rate, self._is_active)

class SavingsAccount(Account):
    def __init__(self, initial_amount, max_num_withdrawals=1,
                 minimum=1000, interest_rate=0.10,
                 bonus_contribution=0.15, num_withdrawals = 0):
        # Notice how we call the parent classe's constructor to initialize
        # a number of usefull members
        super().__init__(initial_amount, minimum, interest_rate)
        self._num_withdrawals = num_withdrawals
        self._max_num_withdrawals = max_num_withdrawals
        self._bonus_contribution = bonus_contribution

        # 1) Set the number of withdrawals to 0 (only SavingsAccounts track the number of
        #    of withdrawals

        # 2) Set the _max_num_withdrawals member to the value given in the parameters
        #    of the constructor 

        # 3) Set the bonus contribution to the value given in the parameters of
        #    the constructor

    def get_num_withdrawals(self):
        # Simply return the number of withdrawals
        return self._num_withdrawals

    def withdraw(self, w_amount):
        # 1) If the number of withdrawals is >= than the maximal number of
        #    withdrawals allowed throw and exception:
        if self._num_withdrawals >= self._max_num_withdrawals:
            raise ValueError("Savings accounts allow only {} withdrawals.".format(self._max_num_withdrawals))

        # 2) Increase the withdrawal counter by 1
        self._num_withdrawals += 1

        # 3) Call the parent's implementation of withdraw as it does the rest of
        #    things for us
        return super().withdraw(w_amount)
        

    def add_bonus(self):
        # According to the banks rewards scheme, increase the amount held by the
        # (percent bonus contribution) * (minimal amount ever held) + 100
        self._amount_held += ((self._bonus_contribution * self._min_ever_held) + 100)

    def close_account(self):
        # 1) Add bonus
        self.add_bonus()
				
        # 2) Call the parent's close_account method as it does lots of stuff already
        return super().close_account();  # Fine point: calling self.close_account
                                              # causes infinite recursion

    # Fill in the missing variables; remember that in contrast to CheckingAccount the
    # SavingsAccount track the number of withdrawals
    def __str__(self):
        return \
            "\n********************************\n" \
            " id = {}\n amount held = {}\n min. amount held = {}\n"\
            " good standing = {}\n num. withdrawals = {}\n interest_rate = {}\n"\
            " is active = {}".format(self._id, self._amount_held, self._min_ever_held,
                                      self._good_standing, self._num_withdrawals,
                                      self._interest_rate, self._is_active)

if (__name__ == "__main__"):
    a1 = CheckingAccount(230)
    print(str(a1))

    s1 = SavingsAccount(1350)
    print(str(s1))

    a1 = CheckingAccount(140)
    a2 = CheckingAccount(160)
    a2.withdraw(20)
    print(str(a2))
    s1 = SavingsAccount(1400)
    s2 = SavingsAccount(1400)
    s2.withdraw(200)
    

    


    
