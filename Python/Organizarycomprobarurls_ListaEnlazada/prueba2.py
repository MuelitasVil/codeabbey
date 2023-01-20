import urllib.request

for x in range(1000):
    UrlEliminadas = False
    try:
        datos = urllib.request.urlopen("https://www.google.com")
    except:
            UrlEliminadas = True
            contador = contador + 1 
                
    if(UrlEliminadas == True):
        print("Esto no deberia pasar"+str(x))

print("Funcuina".lower())