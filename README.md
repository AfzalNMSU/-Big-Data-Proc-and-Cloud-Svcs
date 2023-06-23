# Title:  Taxi Trip Data Analysis in New York City

Brief summary: <br>
This folder contains code and datasets download link for testing and analyzing New York city taxi trips. The specific technique considered describe the geographic range of the taxi trips, average computed trip distance, and vizualize the results in graphs, plots, and indicate on the New York city map.

Team: <br>
Afzal Hossain
Department of Electrical and Computer Engineering
Dr. Tyler Conlon
Data Science Program
Clarkson university
Potsdam, New York 13699

Source Code Organization:
    source_code.ipynb - This Python file has the necessary code for automatically testing the taxi trip data and vizualizez the results.

map_NYC.png/: Sample image of New York city

dataset_drive_link.txt/: This file contains the drive link of the required data.

version_requirements.txt/: Verrsion required to run the code.

Disclaimer: 
There are no guarantees made about the accuracy or safety of this source code. This project was created for research purposes. The authors have attempted to produce code that is both accurate, efficient, and safe, but only limited testing has been performed. The authors of this code shall not be held accountable for any damage caused by using this code or any derivative works.

Platform and Installation:
Python is needed to run the code.
     a. Download Anaconda (https://docs.anaconda.com/anaconda/install/) or, Python 3.9.13
     b. Install the Python packages using the anaconda prompt according to the provided "version_requirements.txt" file.

Dataset: 
The dataset contains two csv files where information are provided of taxi trips in New york city. The files are uploaded to drive and the link is is provided in the "dataset_drive_link.txt/" file.

Usage:
     a. Download "source_code.ipynb" file and also download the data from the given drive link.
     b. Run the python file with the csv data file within the same folder location.

Commands:
source_code.py

CPU information:
		Processor- Intel(R) Core(TM) i7-10700K CPU @ 3.80GHz  3.79GHz
		RAM- 16.0 GB

# Analyzed results:  The followings provide information about the data and analyzed results from the New York city taxi trip data

1. The datetime range that the data covers and total available rows

![image](https://user-images.githubusercontent.com/83153124/197452289-44f10fab-02c2-48a1-8fe0-8feecaa80bde.png)

![image](https://user-images.githubusercontent.com/83153124/197452340-081926bf-bdb2-41ae-8eff-c6c77299fc8e.png)

2. Field names and descriptions for each field.

![image](https://user-images.githubusercontent.com/83153124/197452454-3887b2c9-a313-46b1-8dec-dbc10b99c8f4.png)

##### (a) 'medallion' — a license. Medallion licensees shall maintain and provide to the Department a telephone number at which the Department can reach the medallion licensee or its authorized agent within sixty (60) minutes on a 24- hour-per-day basis seven days a week.
##### (b) 'hack_license' — New York released taxi trip data via an information request, and they simply ‘hashed’ certain identifiable details: medallion numbers and another kind of license number called a ‘hack’ license
##### (c) 'vendor_id' — a code indicating the provider associated with the trip record. A code indicating the TPEP provider that provided the record. 1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.
##### (d) 'rate_code' — The final rate code in effect at the end of the trip. 1= Standard rate, 2=JFK, 3=Newark, 4=Nassau or Westchester, 5=Negotiated fare, 6=Group ride
##### (e) 'store_and_fwd_flag' — This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server — Y=store and forward; N=not a store and forward trip.
##### (f) 'pickup_datetime' — date and time when the meter was engaged
##### (g) 'dropoff_datetime' — date and time when the meter was disengaged
##### (h) 'passenger_count' — the number of passengers in the vehicle (driver entered value)
##### (i) 'trip_time_in_secs' — total time taken during the trip in seconds
##### (j) 'trip_distance' — total distance passed during the trip
##### (k) 'pickup_longitude' — the longitude where the meter was engaged
##### (l) 'pickup_latitude' — the latitude where the meter was engaged
##### (m) 'dropoff_longitude' — the longitude where the meter was disengaged
##### (n) 'dropoff_latitude' — the latitude where the meter was disengaged

3. Sample data for each field.

![image](https://user-images.githubusercontent.com/83153124/197454266-8c1d7f6a-d46c-4f03-a598-d29ce69863a1.png)


4. What MySQL data types / len would you need to store each of the fields? - int(xx), varchar(xx),date,datetime,bool, decimal(m,d)

##### 'medallion': varchar(50), 
##### 'hack_license':varchar(50), 
##### 'vendor_id': varchar(10), 
##### 'rate_code': int(5), 
##### 'store_and_fwd_flag': bool, 
##### 'pickup_datetime': datetime, 
##### 'dropoff_datetime': datetime, 
##### 'passenger_count': int(2), 
##### 'trip_time_in_secs': int(5), 
##### 'trip_distance': double(5,2), 
##### 'pickup_longitude': double(12,8), 
##### 'pickup_latitude': double(12,8), 
##### 'dropoff_longitude': double(12,8),
##### 'dropoff_latitude': double(12,8)

5. The geographic range of the data (min/max - X/Y)? (a) Plot (approximately on a map)

##### [COMMENT: There are some outliers in the datset. So, I use condition to remove those values. And represent area only of New York city or near New York city.]

![image](https://user-images.githubusercontent.com/83153124/197454511-ef1a95e7-fc06-4602-9fe1-6f2c2ce62662.png)

![image](https://user-images.githubusercontent.com/83153124/197454529-8da68548-40a0-491a-8a09-51b1473d7f23.png)

![image](https://user-images.githubusercontent.com/83153124/197454549-a345a1b9-3e6d-4c79-a45a-1d95b5ddbfd4.png)

6. Average computed trip distance (Haversine Distance). (a)Histogram of the trip distances binned anyway you see fit.

##### [COMMENT: There are some outliers in the datset. So, I use condition to remove those values. And take the distances only of New York city or near New York city.]

![image](https://user-images.githubusercontent.com/83153124/197454895-ccdfa176-c48f-4af9-91df-36ec361788f9.png)

![image](https://user-images.githubusercontent.com/83153124/197454960-cd27d654-cccd-462f-ace7-41c67e9ec91b.png)

7. Distinct values for each field

![image](https://user-images.githubusercontent.com/83153124/197455066-2b6febd8-be0c-468c-9269-1fb3c20060e2.png)

##### From the table we can see that the 'medallion' and 'hack_license' values are the distinct values for each field.

8. For other numeric types besides lat and lon, the min and max values.

##### From the 'Maximum Passenger Count' we find the value is too big which is 255. And we know there are no taxi exists whicn can have 255 passengers at a time. So, we understand that this is a outlier.

![image](https://user-images.githubusercontent.com/83153124/197455141-0926fab6-0cae-4a70-bc40-281c44e7e440.png)

![image](https://user-images.githubusercontent.com/83153124/197455170-2c5f5987-51de-41ff-9dc6-63e673c7e44b.png)

![image](https://user-images.githubusercontent.com/83153124/197455191-ae23f0de-5475-4c79-a533-d0fe20685da0.png)

9. Chart which shows the average number of passengers each hour of the day. (X axis have 24 hours)

![image](https://user-images.githubusercontent.com/83153124/197455502-03d54126-3038-4bcd-9eb3-b863b6fddad7.png)

10. CSV file which has only one out of every thousand rows.

##### A "output_file.csv" file will be created after running the code. Which contains only one out of every thousand rows. Here is a example of some of them.

![image](https://user-images.githubusercontent.com/83153124/197455701-3e47a53e-b203-40d1-88b3-58952740a513.png)

11. Repeatation of step 9 with the reduced dataset and comparison of the two charts.

![image](https://user-images.githubusercontent.com/83153124/197455502-03d54126-3038-4bcd-9eb3-b863b6fddad7.png) ![image](https://user-images.githubusercontent.com/83153124/197455794-96f119d3-16f8-4ba9-8573-ed05d0681e5a.png)

##### Here the left chart shows the average number of passengers each hour of the day for the total dataset. And the right chart shows the result with the reduced dataset. Comparing the two charts we can say that the first chart is more smooth. And there are ups and downs in the second chart. So the chart with the total dataset, from there we will be able to get more accurate result. However, from the other chart we will not be able to get accuarte information in some cases as there are a lot of sudden drops in the chart.
