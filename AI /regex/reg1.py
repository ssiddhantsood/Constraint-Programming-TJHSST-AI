import sys; args = sys.argv[1:]
idx = int(args[0])-30

myRegexLst = [

#regex1
r"/^10[01]$|^0$/",                     
r"/^[01]*$/",                            
r"/0$/",                                
r"/\w*[aeiou]\w*[aeiou]\w*/i",            
r"/^1[01]*0$|^0$/",                    
r"/^[01]*110[01]*$/",                    
r"/^.{2,4}$/s",                           
r"/^\d{3} *-? *\d\d *-? *\d{4}$/",  
r"/^.*?d\w*/im",                           
r"/^0[01]*0$|^1[01]*1$|^[10]?$/",
#regex2
r"/^[x.o]{64}$/i",
r"/^[xo]*\.[xo]*$/i",
r"/^(x+o*)?\.|\.(o*x+)?$/i",
r"/^(..)*.$/s",
r"/^(0|1[01])([01]{2})*$/",
r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
r"/^(1?0)*1*$/",
r'/^\b[bc]*a?[bc]*$/',
r"/^(a[bc]*a|[bc])+$/",
r"/^((2|1[02]*1)[02]*)+$/"
r"/.*(.).*\1",
#regex3



]

if idx < len(myRegexLst):
   print(myRegexLst[idx])


#Siddhant Sood Period 7 2024


