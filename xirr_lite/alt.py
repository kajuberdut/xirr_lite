"""
https://stackoverflow.com/a/61722558
"""

import numpy as np


EPSILON = 0.0001
LIMIT = 1000

"""
Explanation:

In the test block, it checks whether increasing the discounting rate increases the discounted value or reduces it. Based on this test, it is determined which direction the guess should move. This block makes the function handle cashflows regardless of direction assumed by the user.

The np.sign(residual) != np.sign(prev_residual) checks when the guess has increased/decreased beyond the required XIRR rate, because that's when the residual goes from negative to positive or vice versa. The step size is reduced at this point.

The numpy package is not absolutely necessary. without numpy, np.sign(residual) can be replaced with residual/abs(residual). I have used numpy to make the code more readable and intuitive

I have tried to test this code with a variety of cash flows. If you find any cases which are not handled by this function, do let me know.

Edit: Here's a cleaner and faster version of the code using numpy arrays. In my test with about 700 transaction, this code ran 5 times faster than the one above:
"""


def xirr(df, guess=0.05, date_column="date", amount_column="amount"):
    """Calculates XIRR from a series of cashflows.
    Needs a dataframe with columns date and amount, customisable through parameters.
    Requires NumPy libraries"""

    df = df.sort_values(by=date_column).reset_index(drop=True)

    amounts = df[amount_column].values
    dates = df[date_column].values

    years = np.array(dates - dates[0], dtype="timedelta64[D]").astype(int) / 365

    step = 0.05

    residual = 1

    # Test for direction of cashflows
    disc_val_1 = np.sum(amounts / ((1 + guess) ** years))
    disc_val_2 = np.sum(amounts / ((1.05 + guess) ** years))
    mul = 1 if disc_val_2 < disc_val_1 else -1

    # Calculate XIRR
    for i in range(LIMIT):
        prev_residual = residual
        residual = np.sum(amounts / ((1 + guess) ** years))
        if abs(residual) > EPSILON:
            if np.sign(residual) != np.sign(prev_residual):
                step /= 2
            guess = guess + step * np.sign(residual) * mul
        else:
            return guess
