# ‘bar’ or ‘barh’ for bar plots
# ‘hist’ for histogram
# ‘box’ for boxplot
# ‘kde’ or ‘density’ for density plots
# ‘area’ for area plots
# ‘scatter’ for scatter plots
# ‘hexbin’ for hexagonal bin plots
# ‘pie’ for pie plots

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close("all")
np.random.seed(123456)


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
plt.figure();
#ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()

#df.plot()

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=["B", "C"]).cumsum()
df3["A"] = pd.Series(list(range(len(df))))

#df3.plot(x="A", y="B")



# bar plot

df2 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
#df2.plot.bar()

#df2.plot.bar(stacked=True)

#df2.plot.barh(stacked=True)

df4 = pd.DataFrame(
    {
        "a": np.random.randn(1000) + 1,
        "b": np.random.randn(1000),
        "c": np.random.randn(1000) - 1,
    },
    columns=["a", "b", "c"],
)

#df4.plot.hist(alpha=0.5)

#df4.plot.hist(stacked=True, bins=20)

data = pd.Series(np.random.randn(1000))
data.hist(by=np.random.randint(0, 4, 1000), figsize=(6, 4))




# Box plots

df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])

color = {
    "boxes": "DarkGreen",
    "whiskers": "DarkOrange",
    "medians": "DarkBlue",
    "caps": "Gray",
}

#df.plot.box(color=color, sym="r+")





# Scatter matrix Plot

from pandas.plotting import scatter_matrix

df = pd.DataFrame(np.random.randn(1000, 4), columns=["a", "b", "c", "d"])

scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal="kde")

plt.show()