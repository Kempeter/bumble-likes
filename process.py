import json
import os
import sys
import time

import requests


def load_configs(file: str):
    try:
        with open(file, "r", encoding="utf-8") as f:
            configs = json.load(f)
    except Exception as e:
        print(f"Could not open/read the file: {file} : {e}")
        sys.exit(0)

    return configs

def get_encounters():
    try:
        with open("encounters.json", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Could not open/read the file: {"encounters.json"} : {e}")
        sys.exit(0)
    

def process(data, download: bool, headers: dict[str, str]):

    for index, user in enumerate(data["body"][0]["client_encounters"]["results"]):
        user_id = user["user"]["user_id"]


        about = dict()
        for i in range(len(user["user"]["profile_fields"])):
                about[user["user"]["profile_fields"][i]["name"]] = user["user"]["profile_fields"][i]["display_value"]

        photos = []
        
        for i in range(len(user["user"]["albums"][0]["photos"])):
                photos.append(user["user"]["albums"][0]["photos"][i]["large_url"][2:])
                


        # print infos
        liked = "🟢" if user["has_user_voted"] else "🔴"
        name = user["user"]["name"]
        age = user["user"]["age"]
        print(index + 1, ":")
        print(f"{liked} {name}, {age}")
        for i in about.keys():
            print(f"\t{i}: {str(about[i]).replace("\n", " ")}")


        # write infos to file
        saved_profiles = []
        try:
            with open("saved_profiles.txt", "r", encoding="utf-8") as f:
                saved_profiles = [line.strip() for line in f.readlines()]
        except OSError:
            pass
        
        if user_id not in saved_profiles:
            print("Profile is saved")
            info = str()
            info += f"{liked} {name}, {age}\n"
            for i in about.keys():
                info += f"\t{i}: {str(about[i]).replace("\n", " ")}\n"
            

            with open("profiles.txt", "a", encoding="utf-8") as f:
                f.write(info + "\n")

            with open("saved_profiles.txt", "a", encoding="utf-8") as f:
                f.write(user_id + "\n")

        else:
            print("Profile is already saved")

        success = True
        saved = []
        try: 
            with open("saved.txt", "r", encoding="utf-8") as f:
                saved = [i.strip() for i in f.readlines()]
        except OSError:
            pass

        if download and user_id not in saved:
            for index, i in enumerate(photos):
                response = requests.get(f"https://{i}", headers=headers)

                if response.status_code == 200:
                    
                    if not os.path.exists("images"):
                        os.makedirs("images")

                    with open(f"images/{name}_{index}_{user_id}.jpeg", "wb") as f:
                        f.write(response.content)
                    print(f"Image saved as {name}_{index}.jpeg")

                else:
                    print("Failed to download:", response.status_code)
                    success = False

        elif download and user_id in saved:
            print("Pictures are already saved: " + user_id)
            print()

        else:
            print()

        if success and user_id not in saved:
            with open("saved.txt", "a", encoding="utf-8") as f:
                f.write(user_id + "\n")

                time.sleep(0.1)
