
## Basic Dataframe commands

To select rows whose column value equals a scalar, some_value, use ==:
```
df.loc[df['column_name'] == some_value]
```
To select rows whose column value is in an iterable, some_values, use isin:

```
df.loc[df['column_name'].isin(some_values)]
```
Combine multiple conditions with &:

```
df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]
```