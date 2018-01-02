import os

codigo = [
"vx66cLsxoñU3ñp1;MLf*ÑlkBt3&dmqmFYY4iopCÑwÇs?9Py¿V9KKN00cRPF?jgR;ydwj2QÑ0w*!0kKlz2A$aO8aÑVoYsJU7QiI2q",
"Qm50QdjO@V7&9/QZCbrVM%VijS9%3;!xY3%b9Ñ*Çpg1Z1L^JbkSgs28@LMq¿ZnXmVR2uvyh5y?GU;M@RIWl33Z0zhbsXb%&WÑLS/",
"VGUsaVi!lnnoQY6@L!AP/2&%/Mb&zsx8?26w5sXhD*$rD*VñCa7ZWB!DI2B¿7vArZ@FRtHWJMx4m2ñ¿^?f3bGzCxPPlmbCofR;cY",
"UfGzaS3b7s¿/ñnLUu*ur4O?n¿KJXÇ6¿sSbhYUsQu78d&PY2A&Ck9w7uNcg1;xsc?rmKMyñ!k@Qbq9rnaO0b23S4P9UmMz¿w!3!Gn",
"ñQBJÑs6YI2&FZX5mAwm7W¿BqmaInzVwk;G*B7w6D;rvtpIrbjp//NKmWhJidzmruNzymCy4ÇadBwmuyochfVcopVVCooo40Yk!VÇ",
"fW!wjj@&Mh8C^oZD$XZDhm$!Zw^R&ngDNwh%dI3uiFHJP9mVGgqz&fRJ*mfNnosX/dI;yJWj$BKñcilu;MI?YNBXm$V&pBz?dRF7",
"uB3FNZU4rJHphmJkIi!dC;SÇ*ñF8&RPswpaysXbN¿2xpasB?BkiLIpGgFnjPGDVZ3319/6nbjOt3;UF4zfk!fnpvttFLcJaxCl^w",
"PjLG9ugKX¿wGM!F!zZVp1&mas4%*sMGddoBL1i^iPBY¿yYzfm8$*H$^/iKVt$Ç5P4PcCnd8wWKlX%3i8q3!nxYJICDi0rlaDt0qn",
"KwVZtcy!7yuI/OBWd*?X9j66Uc0VX2YoCñÑwUL18qpcD8ñSb!IJz^kFG4JNuw?¿%l^whaMNI1JqK/z?UQ$O8$5If1^IRD6q&nj8I",
"idÑ2;NU$6ÇItAzSHbwQsvV6$o0dioR!&?uwPOIah102AYif¿cHOwOt7;8;7pXa^%NLXjC9ofQ7XOV&tÇI$Çcx*WA$;%OñpKdScx6fmk",
"oP;SzbqDX!aZg?G9dUAwN@95Ls?¿7K?iS2SDLtrAO*R¿uQ8;VMñ6YdNuN3KCBnIÇzO6I;NstA1$bVqHY¿!jx@46Mzg0p¿nz08iXJ",
"u6kosZROv0$;6ARbLZt780nUo^VÇ2u?4zXq7UtÇ8Dddc¿p;2WLV!B0hpxñ%qFWuWs5;llh*%DsfJUo!wPbV78!g!/0Ñl1/IwMqqM",
"3GVqD;ZQ0UF9ls&@H%bOUKumZÑMX1K4!qVDÇQs$Pkqt!vLmD9DñXQ*5*?ni90&C$ml$BLkhBKq0HA3CaLQGi1FBF2QuIdrÑXhMHV",
"4/ñlhQyXazUG0yÇQmntgMcas^mjbÇz^9C0ij98J5HN40fÇvsM5p4%dVl;SsudP0xUCGJñ^jW6ñUqIwx$mtdÑÇñziAj*;vIGoYÇZb",
"J¿sñy¿VYQ%uB5pQÑM4Ç4cGgAf6%rGÑqñrg8JñPAC3HaNV;kBlOo¿twzBaQ3&RPaÇZ$/zym^LL9fvGJÇfXO6v2QDwÇuYxñPw;Vwvc",
"sd^ñ39rpÇ&08axDCyWz¿4d6AÇN6s01Kx2y%s0ks0NiG8O&dÑq/6¿7%d9;7ÇcgR*sFtV55NwxjtL2*PV3jshHiX5¿zQP/Y7K7m!2¿",
"rtñ4KlÑgyÇ2tAnar4*7xb*s;yXOuBa2WcO4@!pFZCqYGKkq65Zom%;vPYClO5cHxOFV/n0K/Pk9u3oOñ4k;GQzM¿5?wvOt@s&XDF",
"jHhNcO$PN9b1pajRSUÑx;*YySrpn93&5HC&S/4i@Çg1bR@arM*ñmaV0nrxdJO4watvG7Psf?9qf7XgKp@ÑÑm4nOKGIN*D^JkkFnt",
"7SBSd$D?9xO^hlznCX!sbZDs%@PfrfgwIkd6&6gyNÑ3M^gvZ^rFh5;xY?jx@w&MZ¿SBCIJj22hO/27wV4GX4ñKlñcwHCu;ss9rDn",
"¿&R5xuxCoÇm^0qKkF9g4y41¿ñm6WFk9lhVZÑ&IuLb?FdzxmB;ogoñPfFkcJaf@LGSf7!jSKB?l;nwDakCQ?!pMn$JkAgzpIIIMCn",
"¿wqA%YK37192p;u!*F;o!h¿MOgU;fHCAQmF2y2MK4Md5wXGB9gb5MvmisvqiSj%&?h?^%HZx7QKziVnwuÇyS@v9UBncuhYHY*CjA",
"ztR1CJH@ñp%$Zoma*R$VPjxNPRSnFdZZkiw&RY7klIKZoI^6Ñ0W7OZPcgd?cU2s%y1?5xNI36sI2GQQ8odwp;?mR@96Ñ%hXÑmS2J",
"3CIqOPS3A7XBZb&LrasYMo0h4M?3ZQfdyjf3F8Ç?frhN@/nGP3¿?!87RS*J$6bMzK$kPkKR?d99g3QñB4XQmr%u*UYxÇy7%vBpxo",
"ks&OfYxOoVru$Nts&h1fÇo9P/FKFCvÇ5Vp^ihdK!FUqnV9NXF$Ç*ñsaBiUK$69S&@2l25IWWdmvRÑawsOhMDNYhV/;z^lG3d$Onm",
"Sñ7DC!M$9DB68hñu?uu9GÑZLPmñyrLKDZ71ZFr¿!Ñ0dhxrC1YzCisÇN1FJq6IZrxr8k;kXSC4kgkLlLpv8ox0&InKÇtNcQUgv%nD",
"ARJotyYa^OuB39Fi%?qBX4GpNPD2XJSR^ñÇj@xa?d&HnZ!g1m4M6rbcñsXMmt4F*!vlrjCUr^6caGDOIlÑpVHdhpd¿66vtzwU/rD",
"NxOgñxfñnñCnjsdwx22v@$NLdAcUq$1UWjkÇoX?I&H?4Dh$3kñ8;ñHIg$fwD;ÇrNsIHuYi&yLHvQ04&9kP^6J$qHlIF1kVf5fbI$",
"HIkJAG/VK*xlM;%p9LxcoKtnMsJ6*L8WBÑ7Ç¿nZ%CNVJw9GZaÑjñ7QKiarrtWlXZ2%dD0ÇzJrXf5ñBV6jd!¿ipIBwM&QhWP1OÇxL"
]

caracteres = [" ","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m"]
"""
es = "vx66cLsxoñU3ñp1;MLf*ÑlkBt3&dmqmFYY4iopCÑwÇs?9Py¿V9KKN00cRPF?jgR;ydwj2QÑ0w*!0kKlz2A$aO8aÑVoYsJU7QiI2q"
q = "Qm50QdjO@V7&9/QZCbrVM%VijS9%3;!xY3%b9Ñ*Çpg1Z1L^JbkSgs28@LMq¿ZnXmVR2uvyh5y?GU;M@RIWl33Z0zhbsXb%&WÑLS/"
w = "VGUsaVi!lnnoQY6@L!AP/2&%/Mb&zsx8?26w5sXhD*$rD*VñCa7ZWB!DI2B¿7vArZ@FRtHWJMx4m2ñ¿^?f3bGzCxPPlmbCofR;cY"
e = "UfGzaS3b7s¿/ñnLUu*ur4O?n¿KJXÇ6¿sSbhYUsQu78d&PY2A&Ck9w7uNcg1;xsc?rmKMyñ!k@Qbq9rnaO0b23S4P9UmMz¿w!3!Gn"
r = "ñQBJÑs6YI2&FZX5mAwm7W¿BqmaInzVwk;G*B7w6D;rvtpIrbjp//NKmWhJidzmruNzymCy4ÇadBwmuyochfVcopVVCooo40Yk!VÇ"
t = "fW!wjj@&Mh8C^oZD$XZDhm$!Zw^R&ngDNwh%dI3uiFHJP9mVGgqz&fRJ*mfNnosX/dI;yJWj$BKñcilu;MI?YNBXm$V&pBz?dRF7"
y = "uB3FNZU4rJHphmJkIi!dC;SÇ*ñF8&RPswpaysXbN¿2xpasB?BkiLIpGgFnjPGDVZ3319/6nbjOt3;UF4zfk!fnpvttFLcJaxCl^w"
u = "PjLG9ugKX¿wGM!F!zZVp1&mas4%*sMGddoBL1i^iPBY¿yYzfm8$*H$^/iKVt$Ç5P4PcCnd8wWKlX%3i8q3!nxYJICDi0rlaDt0qn"
i = "YWRfPP$iPgÑasv1ñ?HV@$A3j!5RHG@/vzz7iuÑFbopX;HP41sJHflGXohuLlxiAFu/uiñUQ?8;$RupCfxRHBD@R2Dd1vAv1WJ?YQ"
o = "S?h6G^GwV/pcg3NsknMk8zñgÑ$Kgx¿swuHHVFGGYW&HvglK08@N¿Bpb*uLuk%ym^QWxA@qfggjiA3;OVK8xlv¿nvbStq*S^8FYyS"
p = "vMYdk5/SCysñO9d;0@sfsIQhBco$vhñ5vqPÑ6bWJt2@9N71szHkfrZD3aMRGi/8dkHBMgW53wQWq5JGDwx96HKm0s7K3XyH2/N&I"
a = "Gg15ANhM6NlB$htu7ii1%kFQMPjfIfl@rMs52Lp^lñoO@Ñ%JG$RlMxwQÑAwFvP3!olbrWqNl/ÇzÑjXS/7By¿/Ojx364UYUDoML2?"
s = "&;tA*xyJbX@k6ZK¿vY3tvIñ1Ipgq8FgQSaVYfÇa?nvWabLFVi*lQñ&I1CudD2ZM$RiSiUF^H1Z3G556mCz$4$qul¿QDk;YzMq4y9"
d = "2yDMLyk@t*UsqJFyoLñ2¿J!JAW@sVM;uZG4OZNmXZJONl8JB0/o!3?rrÑUMBGvÑQyuply¿F*ÑtcVBIX?GZñjsl7YfWrAxm1UfNQg"
f = "nVhhgypBx6ybuCs23Og*;bnbs/7lV1!n$Suw5JR554uVWHsv?yuMvb87Gjñ%xFg40HDLlmlñqqj1IÑj3mqB0DñAmahIzHO3%iÑh*"
g = "RyI^q32aXÑVXCMXG@z3;2^moZW6RXyP¿!RgÑfS&;X^yzn%XAdPQDh;zcR/%3QffMXÇv&mxN*7*pZLnjCÑr^GC0?1x$NC7^n*500M"
h = "*%AowQrNtmVxRtw!@kr@sa*;WlHÇ%yaYjAw1BZN2I5ñzt!100HR0sj^RWabVK3bHgMj4hS@J5!H;OQRBvwvsYzxcRbup$zRHoLXW"
j = "ñV*2MglJA6uj&UyoOz3Wtn@RQJV8cZPY5lQy5/89K2ñAd6lnK2wXU^sopxJJiI9CAZXlZP*^3MVvW%Vgafñjo4H7ujPMBIa;0*Uq"
k = "jAXy5OX$gSmdgv/c@/^YOrWqQjCc¿jhbvk*UZ9R?85Z3vu120xM^m2tuX/w67a@r&@^Y%J8WL2AxFro5oA2SWlÇm@7FmUj25V;ng"
l = "0cYHnVO*8jP!yd;rvÇAoSQ9V?Bd0?qñ@l7ñd!4R6JfhRnaBCZDBmj&ñ6k$VblFfrs^ñRñVpWzÑIJn$FbzX6¿*uPns75HSQkGUHqG"
ñ = "W2D%3y^1%bY6VMq?2CzZ/ugVtht^IP8Pñ@^&¿o;v0NBZFV3W5ñ7hZ&w1MS^ñmv?1/VIOCat&C%5pA3$&l7^FW/x9a8^8fLÑKrSrG"
z = "4GÑJmKn&UR9nJm!4Çu*RRc15jÑjRhñÑAYo^fYFn!UIqwxdSKcñ2@D2f%^W@svkqW@NGODñ¿DO8mN5yV*U4pobIMwXH8M44AVZ!PF"
xi = "UoLÑZ//M!ly6d4gfy3/A5@XBPa!8ñxaZlg/PDAvt?ñIQGMW^^jgdI4r;JNp3DXwcvGlnHFiqdjCN&lbXFFxlpWfiñ¿%0C1?23Fm^"
c = "rÑhp¿rHd5C?nOKoOCoPjd!B!9?YPa3ZtJÑlÑcÑ9!SdjñYAN&jaLF3cZN^ñqAxzmIJ@¿q6k0vÑGqiS2yD*8I!Yl@9*GC4yR3t1cci"
v = "@s?pchR9CSBocqxp3ZLIC;usubRNCg/Ç?F64uWYcKh;4sÑ8ruSWWl!r9VO3lNHGrro?;VñkQL!nlg4r2Cag73%XtZÑ;2%D¿Wc¿c@"
b = "qNhPWA!¿9kxmgFY!yN¿dgXñN¿tM$3S2I;hyUm&kqMa9ArX5Cx4ÇWRyj3¿ñ1xBoñI@kW¿d$C2hW^uUNwhZNlWqsÇa8Km6MlQ@A¿h4"
n = "0¿t2nkñaN&mU5F/Zl$1Çy6now2jH6ya?s*%^*a5cUAQb6pJo2rR^iBrIWÑSXOy5!cNA6f^Zjabk¿;J5@i2Fkx??jF0GNy@kIddN%"
m = "ytis65X4?ÑAht$F6?ZLW0ñÇaq36&WQxfLo8r2D$i^^ÇG$ChlfdDCNÇW5achZbtqyg/ltÇ¿5P4FV9tGK1Ñ7ñfSPYC*J90?c^2QUhL"
"""

def iniciar(directorio):
 fitxategia = input("fitxategiaren izena jarri:")
 kodi_deskodi = input("kodifikatu edo deskodificatu ko/des:")
 os.chdir(directorio);
 if kodi_deskodi == "ko":
  fichategia = open(fitxategia,'rt')
  irakurri =  fichategia.read()
  lotura = kodifikatu(irakurri)
  fichategia.close()
  idatzi(lotura,directorio)
 elif kodi_deskodi == "des":
  fichategia = open (fitxategia,'rt')
  irakurri =  fichategia.read() 
  lotura = deskodifikatu(irakurri)
  print(lotura)
  fichategia.close()
  idatzi(lotura,directorio)
 
#kodificatu 
def kodifikatu(irakurri):
 luzehera = len(irakurri)
 luzehera2 = len(caracteres)
 lotura = ""
 for x in range(luzehera): 
  letrak = irakurri[x]
  for t in range(luzehera2):
   if caracteres[t] == letrak:
    lotura += codigo[t] 
 return lotura

#descodificatu
def deskodifikatu(irakurri):
 luzehera = len(irakurri)
 luzehera2 = len(codigo)
 le = ""
 lotura = ""
 for x in range(luzehera):
  le += irakurri[x]
  for t in range(luzehera2):
   if le == codigo[t]:
    lotura += caracteres[t]
    le = ""
 return lotura
 
 
def idatzi(lotura,directorio):
 os.chdir(directorio)
 fichategia = open ('a.txt','wt')
 fichategia.write(lotura)
 fichategia.close()
 
#programa
directorio = input("aukeratu directorio bat fitsategiak kodifikatzeko edo deskodifikatzeko:")
iniciar(directorio)
