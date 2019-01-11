## 1. The Time Module ##

import time
current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time

current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

## 3. UTC ##

import datetime

current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime

kirks_birthday = datetime.datetime(year = 2233, month = 3, day = 22)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff

## 5. Formatting Dates ##

import datetime

print(mystery_date)

mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date_2)

## 8. Reformatting Our Data ##

import datetime

for post in posts:
    post[2] = datetime.datetime.fromtimestamp(float(post[2]))
    

## 9. Counting Posts from March ##

march_count = 0

for post in posts:
    if post[2].month == 3:
        march_count += 1

## 10. Counting Posts from Any Month ##

def posts_nb_per_month (month):
    posts_nb = 0
    for post in posts:
        if post[2].month == month:
            posts_nb += 1
    return posts_nb

feb_count, aug_count = posts_nb_per_month(2), posts_nb_per_month(8)
