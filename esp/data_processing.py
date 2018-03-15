import pandas as pd
from io import StringIO
from scipy.optimize import curve_fit
from df_average_speed import speed_frame

df = speed_frame

#min is 2 data for column
#df = pd.read_table(StringIO('''
#                 5        50        250       500       600       700       800
#    5         7.168    6.7936       NaN       NaN     6.224  6.749333    6.4224
#    50       6.7936       NaN       NaN       NaN       NaN       NaN       NaN
#    250    6.749333    6.6274       NaN       NaN       NaN      6.42     6.224
#    500      6.4224    6.2224       NaN       NaN      5.72     6.224    5.7224
#    600         NaN       NaN       NaN       NaN       NaN       NaN       NaN
#    700         NaN       NaN       NaN       NaN       NaN       NaN       NaN
#    '''), sep='\s+')
#df = pd.DataFrame(data={'1': [7.168, 6.7936, 6.749333, 6.4224, NaN],'2': [],'3': [],'4': [],'5': []})

# Do the original interpolation
df.interpolate(method='nearest', xis=0, inplace=True)
print('df1:\n', df)
df.interpolate(method='linear', axis=1, inplace=True)

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

#with open('extrapolated_data.txt', 'w') as file:
#    file.write(str(df))

print('Data was extrapolated with these column functions:')
for col in col_params:
    print('f_{}(x) = {:0.3e} x^3 + {:0.3e} x^2 + {:0.4f} x + {:0.4f}'.format(col, *col_params[col]))

df.to_csv('extrapolated_data.csv', sep=',', encoding='utf-8', index=False)