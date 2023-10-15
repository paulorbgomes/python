'''
Crie um código em python que teste se o site Pudim está acessível
pelo computador usado.
'''
print("")

#import urllib
#import urllib.request
import webbrowser

try:
    #site = urlib.request.urlopen("http://www.pudim.com.br")
    site = webbrowser.open("http://www.pudim.com.br")
except:
    print("O site não está acessível no momento!")
else:
    print("Site acessível no momento!")
    
