import json
import sys
import requests
import os


def checkwebhook(w):
    try:
        check = requests.get(w, params={'wait': True})
        if check.ok or check:
            return True
        else:
            return False
    except:
        return False


def sendmessage(w, m):
    r = requests.post(
        w,
        json={
            "content": m,
            "name": "Who am I",
            "avatar_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.sGYwF587OI6VL508fRNtzwHaLH%26pid%3DApi&f=1"
        },
        params={'wait': True}
    )
    if r.ok:
        pass
    else:
        print(f" --- Message failed to sent --- ")


def main(webhook):
    os.system(
        f'title [ Webhook: {str(webhook.split("/")[5])}  ^|  {str(webhook.split("/")[6])} ]'
    )
    try:
        if checkwebhook(webhook):
            while True:
                message = input(f" > ")
                sendmessage(webhook, message)
        else:
            print(f" --- Invalid Webhook, press [ENTER] to return --- ")
            input()
            main()
    except KeyboardInterrupt:
        sys.exit()
    except:
        main()


if __name__ == "__main__":
    os.system("cls")
    with open("b-config.json", "r") as f:
        data = json.load(f)
        if len(data["webhooks"]) >= 2:
            webhooks = data["webhooks"]
            for i, webhook in enumerate(webhooks):
                print(
                    f'  [{i+1}] Webhook: {str(webhook).split("/")[5]}  |  {str(webhook.split("/")[6])}'
                )

            opt = input(" > ")
            os.system("cls")
            webhook = webhooks[int(opt)-1]
            main(webhook)
        else:
            main(data["webhooks"][0])
