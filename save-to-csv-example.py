import requests
import time
import dashhacks

FORM_URL = "http://api.cloudstitch.com/vitamintk/magic-form/datasources/sheet"
def post_remote(button):
	data = {"Timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "Button": button}
	x=requests.post(FORM_URL, data)

def post_local(button):
	data = "{}, {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), button)
	with open("data.csv", "a+") as f:
		f.write(data)

def post_both(button):
	post_remote(button)
	post_local(button)

dashhacks.go(post_both)