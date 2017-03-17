import sys
import os
import string
import io

if(len(sys.argv) != 6):
	os._exit(0)

workforlder=sys.argv[1]
versionCode=sys.argv[2]
versionString=sys.argv[3]
versionDate=sys.argv[4]
buildNumber=sys.argv[5]

versionCode='%d' %(int(versionCode) + 1)
buildNumber='%03d' %(int(buildNumber) + 1)

def outputDate( raw_date ):
	year_month_day = raw_date.split('/')
	year = year_month_day[0]
	year = year[2:]
	month = year_month_day[1].zfill(2)
	day=year_month_day[2].zfill(2)
	return year + month + day


versionName=versionString + outputDate(versionDate) + buildNumber;

file_object=open(workforlder + 'vblVersionCode.txt', 'w')
file_object.write(versionCode)
file_object.close()

file_object=open(workforlder + 'vblVersionName.txt', 'w')
file_object.write(versionName)
file_object.close()

file_object=open(workforlder + 'vblBuildNumber.txt', 'w')
file_object.write(buildNumber)
file_object.close()