# UserTracker
The main puspose of this project is to create a couple of custom django managements commands, which would give access to owner of this to 
create a user and update their activity data from terminal.<br />
An end user can fetch user and their activity period details on internet in json format.

## Commands are
* **newusercreation**<br /><br />
This commands is for creating a new user.
To create a new user hit command in below format:<br /><br />
python manage.py newusercreation ***username***  ***password***  ***real_name*** ***Time_zone***<br /><br />
example: python manage.py newusercreation james ward@1234 "James Ward" "United Kingdom"<br /><br />

* **addtimeperiodsofuser**<br /><br />
This commands is for add activity periods of any exesting user. 
To add activity periods of any existing user hit the command in below format:<br /><br />
python manage.py addtimeperiodsofuser  ***username*** ***start_time*** ***end_time*** <br /><br />
example: python manage.py addtimeperiodsofuser james "2020-10-25 09:25:45" "2020-10-25 18:25:20"<br /><br />
**Note: Date-Time format is "YYYY-MM-DD 00:00:00"**<br /><br /><br />

## endpoint for fetching users details is:<br /><br />
/userdetails
