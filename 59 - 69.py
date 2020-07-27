#59
import pandas as pd

#60
import pandas as pd
print(pd.__version__)

#61
import pandas as pd
df = pd.DataFrame(data, index=labels)

#62
print(df[col][row])


#63
pf = df.describe()
print(float(len(df[df["age"].notnull()])))
print(pf.loc[["75%"], "age"][0])

#64
print(df[:3])

#65
print(df.loc[df.index[[0, 2, 3]]])

#66
print(df.loc[:, ["name", "age"]])

#67
print(df.iloc[[0, 2, 3]][["name", "age"]])

#68
print(df[df["age"]>critical_age])

#69
print(df[pd.isnull(df["age"])])
