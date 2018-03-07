import pandas as pd
from io import StringIO
from scipy.optimize import curve_fit

#min is 2 data for column
df = pd.read_table(StringIO('''
                 5        50        250       500       600
    5         7.168    6.7936  6.749333    6.4224     6.224
    50       6.7936       NaN       NaN       NaN       NaN
    250    6.749333    6.6274      6.42     6.224       NaN
    500      6.4224    6.2224     6.224    5.7224      5.72
    600         NaN       NaN       NaN       NaN       NaN
    700         NaN       NaN       NaN       NaN       NaN
    '''), sep='\s+')

# Do the original interpolation
df.interpolate(method='nearest', xis=0, inplace=True)

# Display result
print('Interpolated data:')
print(df)
print()

# Function to curve fit to the data
def func(x, a, b, c, d):
    return a * (x ** 3) + b * (x ** 2) + c * x + d

# Initial parameter guess, just to kick off the optimization
guess = (0.5, 0.5, 0.5, 0.5)

# Create copy of data to remove NaNs for curve fitting
fit_df = df.dropna()

# Place to store function parameters for each column
col_params = {}

# Curve fit each column
for col in fit_df.columns:
    # Get x & y
    x = fit_df.index.astype(float).values
    y = fit_df[col].values
    # Curve fit column and get curve parameters
    params = curve_fit(func, x, y, guess)
    # Store optimized parameters
    col_params[col] = params[0]

# Extrapolate each column
for col in df.columns:
    # Get the index values for NaNs in the column
    x = df[pd.isnull(df[col])].index.astype(float).values
    # Extrapolate those points with the fitted function
    df[col][x] = func(x, *col_params[col])

# Display result
print('Extrapolated data:')
print(df)
print()

print('Data was extrapolated with these column functions:')
for col in col_params:
    print('f_{}(x) = {:0.3e} x^3 + {:0.3e} x^2 + {:0.4f} x + {:0.4f}'.format(col, *col_params[col]))