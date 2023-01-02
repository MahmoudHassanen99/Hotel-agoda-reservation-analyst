import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("hotels.csv")

# exploreing data
# print(df.shape)
# print(df.describe())

# check if anly values missed
# print(df.isnull().sum())

##Manipulating Data

# Q1: numbers of reservation for each places
most = df['place'].value_counts()
#df['most']=most
print(most)

# most three reserved hotels
most_hotels_res= df['hotel_name'].value_counts().nlargest(3)
#df['most_hotels_res'] =most_hotels_res
#print(hotels)

# most five wanted places
most_wanted_places = df['place'].value_counts().nlargest(5)
#df['most_places']=most_wanted_places
#print(most_places)

# most five hotel reserved by each place
most_hotels_res_each_place= df.groupby(['hotel_name']).count()['place'].nlargest(5)
#df['hotel_by_places'] =most_hotels_res_each_place
#print(hotel_by_places)

# top five places customers spend time
top_places_spend_time = df.groupby(['place']).count()['days'].nlargest(5)
#df['most_time_places']=top_places_spend_time
#print(most_time_places)

# prices for every places descending
prices_for_every_places= df.groupby(['place']).count().sort_values('price', ascending=False)['price']
#df['prices_for_every_places'] =prices_for_every_places
#print((prices_for_every_places))



#total price per year
total_price=df.groupby('year').sum()['total']
#print(total_price)


plt.plot(most)
plt.ylabel('numbers of reservation for each places')
plt.xlabel('Hotel Names')
plt.show()


#df.to_csv('new_hotel.csv', encoding='utf-8', index=False)
