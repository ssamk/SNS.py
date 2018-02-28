import requests, time, re, sys, random
#reload(sys)
#sys.setdefaultencoding('utf-8')
url = 'https://raffle.sneakersnstuff.com/country_eu-AQ0818-100'
print("SNS raffle script for the Mars Yard sneakers written by @fockniketalk")
print("If u bought this from some1 please contact me on twitter @fockniketalk")
print("btw if u need verified nike accounts usa & eu hit my dm @fockniketalk")

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

list1 = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]		   
sizes = ['US 6','US 7', 'US 8', 'US 8.5', 'US 9', 'US 9.5', 'US 10' ,'US 10.5' ,'US 11' ,'US 11.5' ,'US 12', 'US 13']

def main(limit):
    for i in range(0, limit):
        payload ={
            'form[email:Fi1mS3bZn3VF]': 'sam.thomas80@hotmail.co.uk', #change to your email
			'form[list:56641463][choices]': sizes[random.randint(0, 11)], # don't change
            'form[landed_at]': '1500901708', # don't change
            'form[language]': 'en', # don't change
            'form[terms:QS4P6gmSVp8s]': '1', # don't change
            'form[textfield:Boa0BNN75u6R]': 'London', # change to ur city
            'form[textfield:EKZm78mYLBbE]': '5 Links Road', # change to ur streetname + number
            'form[textfield:IIdtgeMwp8Gp]': list1[random.randint(0, 99)], # DO NOT CHANGE !
            'form[textfield:MQfwQiem4TEw]': 'KT17 3PP', # change to ur zip code
            'form[textfield:bHSS1rapvhha]': list1[random.randint(0, 99)], # DO NOT CHANGE
            'form[textfield:n3yXjbpstFmJ]': 'None', # change to ur state, if EU set: None
            'form[textfield:u9og65Z22NNB]': 'United Kingdom', # change to ur country
            'form[token]': 'e5455f13bd09203c7f5f0b433129e116$2y$11$e2dJZC0zIXZQK1pxbSZbL.LzJE2QS5SFRX2Z7Lk/oL/j6JicEpiXS', # don't change
            'form[yes-no:warE3SilldbG]': '1', # don't change
              }
        resp = requests.post(url, data=payload, headers=headers)
        if any(re.findall(r'succes', str(resp.text), re.IGNORECASE)):
            print(time.strftime("%H:%M:%S") + " / Successfully entered SNS raffle off white Nike, written by @fockniketalk" )
        else:
            print(time.strftime("%H:%M:%S") + " / Could not enter!")

main (10) # change to the amount u want, currently 100 times.
exit()
