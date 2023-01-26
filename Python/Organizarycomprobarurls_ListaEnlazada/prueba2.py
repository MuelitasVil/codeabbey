import urllib.request

UrlEliminadas = False
try:
    datos = urllib.request.urlopen("https://raw.githubusercontent.com/PaolaGiraldo/codeabbey_solutions/master/Typescript/130/problem_130.ts")
except:
        UrlEliminadas = True
        print("No abre")
                

print("Funcuina".lower())