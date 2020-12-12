import matplotlib.pyplot as plt


# Canada:
years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984,1988, 1992, 1994, 1998, 2002, 2006,2010, 2014]

medals = [9, 12, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 37, 40, 49, 75, 68, 91, 90]

plt.plot(years, medals, color=(255/255, 100/255, 100/255), linewidth=4.0)

plt.show()

values = [315, 203, 107]
colors = ['gold', 'silver', '#cd7f32']
labels = ["Gold", "Silver", "Bronze"]

plt.pie(values, labels=labels, colors=colors)

plt.show()


# Finland:
years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

medals = [15, 4, 3, 9, 9, 12, 12, 13, 15, 8, 10, 16, 12, 19, 34, 13, 31, 59, 13, 43, 50, 34, ]

plt.plot(years, medals, color=(255/255, 100/255, 100/255), linewidth=4.0)

plt.show()

values = [66, 147, 221]
colors = ['gold', 'silver', '#cd7f32']
labels = ["Gold", "Silver", "Bronze"]

plt.pie(values, labels=labels, colors=colors)

plt.show()

# Germany:
years = [1928, 1932, 1936, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

medals = [5, 21, 7, 38, 40, 44, 61, 54, 54, 36]

plt.plot(years, medals, color=(255/255, 100/255, 100/255), linewidth=4.0)

plt.show()

values = [137, 126, 97]
colors = ['gold', 'silver', '#cd7f32']
labels = ["Gold", "Silver", "Bronze"]

plt.pie(values, labels=labels, colors=colors)

plt.show()

