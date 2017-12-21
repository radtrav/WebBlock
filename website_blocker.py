import time
from datetime import datetime as dt

#Fill out only the variables below

hosts_path="/etc/hosts"
redirect="127.0.0.1"
websites_list=["www.facebook.com", "facebook.com", "www.lifehacker.com", "lifehacker.com"]
start_time = 0
end_time=17

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_time) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time):
        print("Working Hours ...")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        print("Fun Hours ... No Sites Will Be Blocked")
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()


    time.sleep(5)

