# Japan-WHV-Check
Tool for alerting me to the change in status for Japan accepting Working Holiday Visas 

Repos used: requests, bs4, notify-py

Formatted in cron to run every 30 minutes with the following:
*/30 * * * * sudo -u sam DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus python ~/Japan-WHV-Check/WHV.py

