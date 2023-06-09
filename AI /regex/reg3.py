import sys; args = sys.argv[1:]
idx = int(args[0])-50

myRegexLst = [

#regex3
r'/(\w)+\w*\1\w*/i',
r'/(\w)+(\w*\1){3}\w*/i',
r'/^(0[01]*0|1[01]*1|[01])$/',
r'/\b(?=\w*cat)\w{6}\b/i',
r'/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i',
r'/\b(?!\w*cat)\w{6}\b/i',
r'/\b((\w)(?!\w*\2))+\b/i',
r'/(?!.*10011.*)^[01]*$/',
r'/\w*([aeiou])(?!\\1)[aeiou]\w*/i',
r'/^(?!.*1.1)[01]*$/',


#regex4
r"/^((?!010)\d)*$/",                               
r"/^(?!(.*010|101))[01]*$/",      
r"/\b(?!(\w)+\w*\1\b)\w+/i",      
#r"/\w*((\w)(?=\w*\2))\w*((\1\w*){3}|(?!\2)(\w)(?=\w*\5)\w*)\b/i",     #4
r"/(\w)+((?=(\w*\1){3}|\w*\1)(\w)+\w*(?!\1)\4)\w*/im",
r"/\b(?=(\w)+(\w*\1){2})((\w)(?!\w*\4)|\1)+\b/im",    
r"/\b([^iouae\s]*([iouae])(?!\w*\2)){5}\w*?\b/i",    
r"/^(?=.(..)*$)0*(10*10*)*$/",   
r"/^(0$|1(01*0)*10*)+$/", 
r"/^1(10*1|01*0)*(01*)?$/",
r"/^1(10*1|01*0)*(01*)?$/", 

#regex5
r"/^([a-z]*([aeuio])(?!\w*\2)){5,}[a-z]*$/m",                    #70
r"/^([^\WaeuioA-Z]*[aeuio]){5}[^\Waeuio]*$/m",                   #71
r"/^(?=[a-z]*$).*(?!.{,3}[aeiou]).w.+$/m",                       #72
r"/^(a|(?=(.)(.)([a-z])).*\4\3\2|(.)\5)$/m",  #73
r"/^[ac-su-z]*(tb|bt)[ac-su-z]*$/m",          #74
r"/^[a-z]*(.)\1[a-z]*$/m",                    #75
r"/.*(\w)(\w*\1){5}[a-z]*$/m",                #76
r"/^[a-z]*((.)\2){3,}[a-z]*$/m",              #77      
r"/^([a-z]*[^aeuoi\W]){13}[a-z]*$/m",         #78   
r"/^(([a-z])(?!.*\2.*\2))+$/m",               #79



]



if idx < len(myRegexLst):
   print(myRegexLst[idx])


#Siddhant Sood Period 7 2024