#!/usr/bin/env python
# coding: utf-8

# # 1. What datetime range does your data cover?  How many rows are there total?

# In[1]:


import csv

fn = 'trip_data_1.csv'

f = open(fn, 'r')
reader = csv.reader(f)

for row in reader:
#     print(row)
    break


# In[2]:


import csv

fn = 'trip_data_1.csv'

f = open(fn, 'r')
reader = csv.reader(f)
n = 0
for row in reader:
#     print(row)
    n+=1
    if n>5 :
        break


# In[3]:


import datetime, csv

# fn = 'trip_data_1.csv'
f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

minval= None
maxval = None
n = 0

for row in reader:
    if n > 0:
        pickup_dto = None
        dropoff_dto = None
        pickup_dts = row[5]
        dropoff_dts = row[6]

        try:
            pickup_dto = datetime.datetime.strptime(pickup_dts, "%Y-%m-%d %H:%M:%S")
            dropoff_dto = datetime.datetime.strptime(dropoff_dts, "%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print(e)

#         if dto is not None:
        if maxval is None or dropoff_dto > maxval:
            maxval = dropoff_dto
        elif minval is None or pickup_dto < minval:
            minval = pickup_dto
    n += 1

f.close()
print("Datetime Range:",minval, maxval)


# In[4]:


print("Total number of rows:", n)


# In[ ]:





# # 2. What are the field names?  Give descriptions for each field.

# In[5]:


fn = 'trip_data_1.csv'

f = open(fn, 'r')
reader = csv.reader(f)

for row in reader:
    print(row)
    break


# In[ ]:





# # 3. Give some sample data for each field.

# In[6]:


fn = 'trip_data_1.csv'

f = open(fn, 'r')
reader = csv.reader(f)
n = 0
for row in reader:
    print(row)
    n+=1
    if n>5 :
        break


# In[ ]:





# # 4. What MySQL data types / len would you need to store each of the fields?
# int(xx), varchar(xx),date,datetime,bool, decimal(m,d)
# 

# In[7]:


# 'medallion': varchar(50), 
# 'hack_license':varchar(50), 
# 'vendor_id': varchar(10), 
# 'rate_code': int(5), 
# 'store_and_fwd_flag': bool, 
# 'pickup_datetime': datetime, 
# 'dropoff_datetime': datetime, 
# 'passenger_count': int(2), 
# 'trip_time_in_secs': int(5), 
# 'trip_distance': double(5,2), 
# 'pickup_longitude': double(12,8), 
# 'pickup_latitude': double(12,8), 
# 'dropoff_longitude': double(12,8),
# 'dropoff_latitude': double(12,8)


# In[ ]:





# # 5. What is the geographic range of your data (min/max - X/Y)?
# Plot this (approximately on a map)

# In[8]:


# import datetime, csv

# # fn = 'trip_data_1.csv'
# f = open('trip_data_1.csv', 'r')
# reader = csv.reader(f)

# longitude_minval= None
# longitude_maxval = None
# latitude_minval= None
# latitude_maxval = None

# n = 0
# for row in reader:
#     if n > 0:
#         pickup_longitude = None
#         pickup_latitude = None
#         dropoff_longitude = None
#         dropoff_latitude = None
        
#         pickup_longitude = row[10]
#         pickup_latitude = row[11]
#         dropoff_longitude = row[12]
#         dropoff_latitude = row[13]

# #         try:
# #             pickup_dto = datetime.datetime.strptime(pickup_dts, "%Y-%m-%d %H:%M:%S")
# #             dropoff_dto = datetime.datetime.strptime(dropoff_dts, "%Y-%m-%d %H:%M:%S")
# #         except Exception as e:
# #             print(e)

# #         if dto is not None:
#         if longitude_maxval is None or pickup_longitude > longitude_maxval or dropoff_longitude > longitude_maxval:
#             if pickup_longitude > dropoff_longitude:
#                 longitude_maxval = pickup_longitude
#             else:
#                 longitude_maxval = dropoff_longitude
                
#         if longitude_minval is None or pickup_longitude < longitude_minval or dropoff_longitude < longitude_minval:
#             if pickup_longitude < dropoff_longitude:
#                 longitude_minval = pickup_longitude
#             else:
#                 longitude_minval = dropoff_longitude
        
        
#         if latitude_maxval is None or pickup_latitude > latitude_maxval or dropoff_latitude > latitude_maxval:
#             if pickup_latitude > dropoff_latitude:
#                 latitude_maxval = pickup_latitude
#             else:
#                 latitude_maxval = dropoff_latitude
                
#         if latitude_minval is None or pickup_latitude < latitude_minval or dropoff_latitude < latitude_minval:
#             if pickup_latitude < dropoff_latitude:
#                 latitude_minval = pickup_latitude
#             else:
#                 latitude_minval = dropoff_latitude
#     n += 1

# f.close()
# print("longitude_maxval:", longitude_maxval)
# print("longitude_minval:", longitude_minval)
# print("latitude_maxval:", latitude_maxval)
# print("latitude_minval:", latitude_minval)


# calculating max min pickup_longitude

# In[9]:


states_10 = {}

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

for i, row in enumerate(reader):
    if i > 0:
        k = row[10]
        if float(k)>=-75.000000 and float(k)<=-73.935242:
            if k in states_10:
                states_10[k] += 1
            else:
                states_10[k] = 1

#         if n%100000 == 0:
#             print(n)
#         n+=1
# print(states)


# In[10]:


#printing dictionay
# print(states_10)

#converting dictionary to list
pickup_longitude = list(states_10.keys())
# print(pickup_longitude)

#deleting the first column name value
pickup_longitude.pop(0)
# print(pickup_longitude)

#converting from str type to float type
pickup_longitude = [float(i) for i in pickup_longitude]
# print(type(pickup_longitude[0]))

#getting the min & max pickup_longitude value
min_pickup_longitude = min(pickup_longitude)
# print(min_pickup_longitude)

max_pickup_longitude = max(pickup_longitude)
# print(max_pickup_longitude)


# calculating max min pickup_latitude

# In[11]:


states_11 = {}

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

for i, row in enumerate(reader):
    if i > 0:
        k = row[11]
        if float(k)>=40.493669 and float(k)<=40.915477:
            if k in states_11:
                states_11[k] += 1
            else:
                states_11[k] = 1


# In[12]:


pickup_latitude = list(states_11.keys())

pickup_latitude.pop(0)

pickup_latitude = [float(i) for i in pickup_latitude]

min_pickup_latitude = min(pickup_latitude)
# print(min_pickup_latitude)
max_pickup_latitude = max(pickup_latitude)
# print(max_pickup_latitude)


# calculating max min dropoff_longitude

# In[13]:


states_12 = {}

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

for i, row in enumerate(reader):
    if i > 0:
        k = row[12]
        if k!='' and float(k)>=-75.000000 and float(k)<=-73.935242:
            if k in states_12:
                states_12[k] += 1
            else:
                states_12[k] = 1


# In[14]:


dropoff_longitude = list(states_12.keys())

dropoff_longitude.pop(0)

#removing some extra null values that exists 
# dropoff_longitude.remove('' '') #removing some extra null values that exists 

dropoff_longitude = [float(i) for i in dropoff_longitude]

min_dropoff_longitude = min(dropoff_longitude)
# print(min_dropoff_longitude)
max_dropoff_longitude = max(dropoff_longitude)
# print(max_dropoff_longitude)


# calculating max min dropoff_latitude

# In[15]:


states_13 = {}

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

for i, row in enumerate(reader):
    if i > 0:
        k = row[13]
        if k!='' and float(k)>=40.493669 and float(k)<=40.915477:
            if k in states_13:
                states_13[k] += 1
            else:
                states_13[k] = 1


# In[16]:


dropoff_latitude = list(states_13.keys())

dropoff_latitude.pop(0)

#removing some extra null values that exists 
# dropoff_latitude.remove('' '') #removing some extra null values that exists 

dropoff_latitude = [float(i) for i in dropoff_latitude]

min_dropoff_latitude = min(dropoff_latitude)
# print(min_dropoff_latitude)
max_dropoff_latitude = max(dropoff_latitude)
# print(max_dropoff_latitude)


# In[17]:


min_longitude = None
if min_pickup_longitude < min_dropoff_longitude:
    min_longitude = min_pickup_longitude
else:
    min_longitude = min_dropoff_longitude

max_longitude = None
if max_pickup_longitude > max_dropoff_longitude:
    max_longitude = max_pickup_longitude
else:
    max_longitude = max_dropoff_longitude


# In[18]:


print("Minimum Longditude:",min_longitude)
print("Maximum Longditude:",max_longitude)


# In[19]:


min_latitude = None
if min_pickup_latitude < min_dropoff_latitude:
    min_latitude = min_pickup_latitude
else:
    min_latitude = min_dropoff_latitude

max_latitude = None
if max_pickup_latitude > max_dropoff_latitude:
    max_latitude = max_pickup_latitude
else:
    max_latitude = max_dropoff_latitude


# In[20]:


print("Minimum Latitude:",min_latitude)
print("Maximum Latitude:",max_latitude)


# https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db

# In[21]:


BBox = (min_longitude,   max_longitude, min_latitude, max_latitude)
        
# print(BBox)


# In[22]:


import matplotlib.pyplot as plt

ruh_m = plt.imread('\\Users\\afhossa\\Documents\\courses\\3rd\\BigData IA626\\ass_4\\map_NYC.png')


# In[23]:


fig, ax = plt.subplots(figsize = (20,10))
# ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting Spatial Data on New York City Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')


# In[ ]:





# # 6. What is the average computed trip distance? (You should use Haversine Distance)
# Draw a histogram of the trip distances binned anyway you see fit.
# 

# https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points/4913653#4913653

# In[24]:


from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


# In[25]:


import csv,datetime

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

trip_distance = 0
no_of_trips = 0

for i, row in enumerate(reader):
    if i > 0:
        n = 0
        
        j = row[10]
        if j!='' and float(j)>=-75.000000 and float(j)<=-73.935242:
            lon1 = float(row[10])
        else:
            n+=1
        
        if n!=1: 
            k = row[11]
            if k!='' and float(k)>=40.493669 and float(k)<=40.915477:
                lat1 = float(row[11])
            else:
                n+=1
                
        if n!=1:    
            l = row[12]
            if l!='' and float(l)>=-75.000000 and float(l)<=-73.935242:
                lon2 = float(row[12])
            else:
                n+=1
        
        if n!=1:
            m = row[13]
            if m!='' and float(m)>=40.493669 and float(m)<=40.915477:
                lat2 = float(row[13])
            else:
                n+=1
            
        if n!=1:
            trip_distance += haversine(lon1,lat1,lon2,lat2)
            no_of_trips += 1

avg_trip_dist = trip_distance/no_of_trips


# In[26]:


print("Average Computer Trip Distance:",avg_trip_dist)


# In[27]:


import matplotlib.pyplot as plt
import numpy as np

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

n = 0
trip_distance = []
for i, row in enumerate(reader):
    if i > 0:
        dist = row[9]
        if dist!='' and float(dist) >=50:
            trip_distance.append(0)
        else:
            trip_distance.append(dist)
    n += 1


# In[28]:


plt.hist(trip_distance, density=True, bins=30)


# In[ ]:





# #  7. What are the distinct values for each field? (If applicable)

# In[29]:


import csv

fn = 'trip_data_1.csv'

f = open(fn, 'r')
reader = csv.reader(f)
n = 0
for row in reader:
    print(row)
    n+=1
    if n>5 :
        break


# In[30]:


print("From the table we can see that the \'medallion\' and \'hack_license\' values are the distinct values for each field")


# In[ ]:





# # 8. For other numeric types besides lat and lon, what are the min and max values?

# In[31]:


passenger_count = {}

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

for i, row in enumerate(reader):
    if i > 0:
        k = row[7]
        if k!='':
            if k in passenger_count:
                passenger_count[k] += 1
            else:
                passenger_count[k] = 1
                
passenger_count = list(passenger_count.keys())

# dropoff_latitude.pop(0)
 
passenger_count = [float(i) for i in passenger_count]

min_passenger_count = min(passenger_count)
print("Minimum Passenger Count:",min_passenger_count)
max_passenger_count = max(passenger_count)
print("Maximum Passenger Count:",max_passenger_count)


# In[32]:


print("COMMENT: Here we can see that the \'Maximum Passenger Count\' is a outlier")


# In[33]:


trip_time = {}

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

for i, row in enumerate(reader):
    if i > 0:
        k = row[8]
        if k!='':
            if k in trip_time:
                trip_time[k] += 1
            else:
                trip_time[k] = 1
                
trip_time = list(trip_time.keys())

# dropoff_latitude.pop(0)
 
trip_time = [float(i) for i in trip_time]

min_trip_time = min(trip_time)
print("Minimum Trip Time in Seconds:",min_trip_time)
max_trip_time = max(trip_time)
print("Maximum Trip Time in Seconds:",max_trip_time)


# In[ ]:





# In[34]:


trip_distance = {}

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

for i, row in enumerate(reader):
    if i > 0:
        k = row[9]
        if k!='':
            if k in trip_distance:
                trip_distance[k] += 1
            else:
                trip_distance[k] = 1
                
trip_distance = list(trip_distance.keys())

# dropoff_latitude.pop(0)
 
trip_distance = [float(i) for i in trip_distance]

min_trip_distance = min(trip_distance)
print("Minimum Trip Distance:",min_trip_distance)
max_trip_distance = max(trip_distance)
print("Maximum Trip Distance:",max_trip_distance)


# In[ ]:





# # 9. Create a chart which shows the average number of passengers each hour of the day. (X axis should have 24 hours)

# In[35]:


f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

n = 0
hr_count = [0] * 23
passengers_count = [0] * 23
avg_passengers_count = [0] * 23

for i, row in enumerate(reader):
    if i > 0:
# for row in reader:
        n += 1
        try:
            each_hour = datetime.datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S').hour
            hr_count[each_hour] = hr_count[each_hour] + 1
            passengers_count[each_hour] =  passengers_count[each_hour] + int(row[7])

        except Exception as e:
            e

for j in range(0,23):
    if  hr_count[j] > 0:
        avg_passengers_count[j] = passengers_count[j] / hr_count[j]

plt.plot(range(0,23), avg_passengers_count)
plt.show()


# In[ ]:





# # 10. Create a new CSV file which has only one out of every thousand rows.

# In[38]:


import os

f = open('trip_data_1.csv', 'r')
reader = csv.reader(f)

if os.path.exists("output_file.csv"):
    os.remove("output_file.csv")

output_file = 'output_file.csv'
n = 0

with open(output_file, "a") as o:
    for row in reader:
        if n%1000 == 0:
            writer = csv.writer(o, lineterminator = "\n")
            writer.writerow(row)
        n+=1


# In[ ]:





# # 11. Repeat step 9 with the reduced dataset and compare the two charts

# In[39]:


f = open('output_file.csv', 'r')
reader = csv.reader(f)

n = 0
hr_count = [0] * 23
passengers_count = [0] * 23
avg_passengers_count = [0] * 23

for i, row in enumerate(reader):
    if i > 0:
        n += 1
        try:
            each_hour = datetime.datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S').hour
            hr_count[each_hour] = hr_count[each_hour] + 1
            passengers_count[each_hour] =  passengers_count[each_hour] + int(row[7])

        except Exception as e:
            e

for j in range(0,23):
    if  hr_count[j] > 0:
        avg_passengers_count[j] = passengers_count[j] / hr_count[j]

plt.plot(range(0,23), avg_passengers_count)
plt.show()


# In[ ]:





# In[ ]:




