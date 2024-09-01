import hashlib
import sys
import time

print(''' \033[0;31m                                                                                         
                                          ::::::.                                         
                                  :-+*#%@@@@@@@@@@@#**=:                                  
                               -*@@@@@@@@@@@@@@@@@@@@@@@@#=                               
                             =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+                             
                           .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.                           
                           %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                          
                          #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                          
                         :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:                         
                         =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                         
                         *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                         
                         =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                         
                         :@@@@@@@%++*#%%@@@@@@@@@@%%#*++%@@@@@@@-                         
                          @@@@@#:         *@@@@#         :*@@@@@                          
                          :@@@@%           *@@%.          #@@@@=                          
                           -@@@@          =%@@@+          @@@@+                           
                   .+.     .@@@@#-      =@@@+=@@@+      :#@@@@:      =:                   
                     #*:   *@@@@@@@@@@@@@@@:  .%@@@@@@@@@@@@@@@   .*%:                    
                      +@#: :%@@@@@@@@@@@@@:    .@@@@@@@@@@@@@%- .*@#                      
                       -@@#: =%@@@@@@@@@@@- ++ :@@@@@@@@@@@%= .*@@+                       
                        :@@@#: :--+*%@@@@@@%@@@@@@@@@@*+--: .*@@@-                        
                 :-=+*#%@@@@@@#:    =@@@@@@@@@@@@@@@@+    .*@@@@@@%#*+=-:                 
                 -*%@@@@@%%##**+=   :@@+@@-%@@@=@@=@@=   :+**##%%@@@@@%#=                 
                    :=*@@@+:         =+.@% +@@% #@:=+.        .+%@@#=:                    
                        :=#@%+.            .--:            .=%@#+:                        
                   =%=.     -+%%+.                       =#%*-      ::                    
                   +@@@%-      .-*#=.                 =##=.     :*@@@@@.                  
                   =@@@@@%.    +=- :+=              =+: .-=+#@@ #@@@@@@-                  
                   =@%==%@@:   %@@.  :#**. -+=   -#%*#= -@@@%** *@@-=@@:                  
                   =@@.  %@#  =@@@#  -@@%* *@# .#@@+*@@--@@:.:. +@@:*@@                   
                   =@@:  +@% .@@*@@: -@@%@#*@% +@@.-=+=.-@@%@@# +@@@@@:                   
                   -@@= -%@* #@@*@@* :@@.#@@@# +@@ +@%@-+@@-:.. *@@-*@@.                  
                   -@@%@@%= +@@#=#@@-:@@  #@@*  *@@@@@@==@@@%%% #@@  %@+                  
                    ....     ..   ... .:   .      .: ..  ..::::  ..    .      ''')
print("\033[0;33m [+]Created by R4vas")
time.sleep(1)
print("\033[0;33m [+]This tool for cracking")
time.sleep(1)
print("\033[0;33m [+]Algorithme available:MD5 |SHA1 |SHA224 |SHA512 |SHA224 |SHA384")
time.sleep(1)
print("\033[0;33m [+]Start*.*")
print("\033[0;32m 1 ")
time.sleep(1)
print("\033[0;32m 2")
time.sleep(1)
print("\033[0;32m 3")
time.sleep(1)
hash_type= (input("\033[0;32m Hash type:"))
hash1=str(input("\033[0;32m enter your hash:"))
wordlist_location =str(input("\033[0;32m enter your wordlist location:"))
word_list = open(f"{wordlist_location}").read()
lists = word_list.splitlines()

for word in lists:
    if hash_type =="MD5" :
        hash_object =hashlib.md5(f"{word}".encode('utf-8'))
        hashed =hash_object.hexdigest()
        if hash1 ==hashed:
            print(f"\033[34m Hash Found:{word}")
    elif hash_type == "SHA1":
        hash_object =hashlib.sha1(f"{word}".encode('utf-8'))
        hashed =hash_object.hexdigest()
        if hash1 ==hashed:
            print(f"\033[34m Hash Found:{word}")
    elif hash_type =="SHA224":
        hash_object =hashlib.sha224(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash1 ==hashed:
            print(f"\033[34m Hash Found:{word}")
    elif hash_type == "SHA512":
        hash_object =hashlib.sha512(f"{word}".encode('utf-8'))
        hashed =hash_object.hexdigest()
        if hash1 ==hashed:
            print(f"\033[34m Hash Found:{word}")
    elif hash_type =="SHA224" :
        hash_object =hashlib.sha224(f"{word}".encode('utf-8'))
        hashed =hash_object.hexdigest()
        if hash1 ==hashed:
            print(f"\033[34m Hash Found:{word}")
    elif hash_type =="SHA384" :
        hash_object =hashlib.sha384(f"{word}".encode('utf-8'))
        hashed =hash_object.hexdigest()
        if hash1 ==hashed:
            print(f"\033[34m Hash Found:{word}")
    else:
        print("this type of hash doesn't exist")
        exit()
