#76
print(df[(df[filter_names[0]] == filter_values[0]) & (df[filter_names[1]] < filter_values[1])])

#77
print(df[df.age.between(*age_between)])

#78
df.loc[index, "age"] += 1
print(df)

#79
df['age'] += 1
print(df)

#80
print(df.age.sum())

#81
for name in df.columns.values.tolist():
    if df.dtypes[name] in [np.float64, np.int64]:
        print(name, ':', df[name].sum(), sep='')

#82
print(df.groupby(group_by)['age'].mean())

#83
df.loc[new_index] = new_data
df.drop(del_index, axis=0, inplace=True)
print(df)

#84
print(df[group_by].value_counts())

#85
print(df.sort_values(sort_by, ascending=[False, True]))

#86
df[column] = df[column].map({'yes': True,'no': False,1: True,0: False})
print(df)

#87
df[column].replace(old_value, new_value, inplace=True)
print(df)