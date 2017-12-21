# Website Blocker

This is a simple web blocker written in python that runs in the background. This script will block access to any websites that falls within a daily time period. It works by adding forbidden website addresses to the hosts files during the time interval where you wish to go undisturbed. This is perfect for staying focused during work hours instead of wasting hours browsing Facebook, Amazon or your_other_vice.


### How to use

-  To run the program for Windows, run the program as an administrator. For Linux or  Mac use:
```python
sudo python3 web_blocker.py
```

- Specify which sites to block and which timeframe by filling out the variables at the top of the file.
- Once you have run the script make sure to restart your browser for the blocking to take effect. Now if you try to visit a blocked page, during work hours the page will not load.
- (optional) If you would like to run this every time that your computer boots up then you can add this script to crontab. Add the line:
```python
 @reboot python3 path_to_script
```

