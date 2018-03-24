# meet me

One of the problems with existing applications like when2meet, doodle, etc. that help users to coordinate meeting times is that they are so tedious to use repeatedly - users have to put in virtually the same information each time they want to use the app to meet with a new person. I want to create an application that will allow users to co-ordinate meeting times by uploading their ical calendars, and/or maybe create some 'default' times they're free that they can edit each time as needed.

## features

* import your schedule from an .ics file
* compare different schedules for compatible times
    * user specifies minimum amount of time they want to meet for
    * user specifies time frame they'd like to meet within (don't make them meet at night)
* maintain user profiles so that their schedules are saved
* (optional) have user change their schedule online

## what we'd need to build

* convert .ics files to java readable data structure
* store each person's data in some data structure (create a database somewhere?)
* have some way of comparing multiple peoples' calendars to find a time they are mutually free during
* have some way of displaying when people are free
* then show users when they are mutually free

