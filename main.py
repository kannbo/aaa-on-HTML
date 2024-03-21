def tagw(x):
    return (x,x)
html={"!":tagw("h1"),'"':tagw("strong"),"#":tagw("h2"),"|":tagw("style"),"'":tagw("under"),"%":tagw("code")}
def aaa_list(x: str,doHTML: bool=False) -> list:
    block=[]
    for i in range(len(x)):
        if doHTML:
            block.append(x[i])
        else:
            if x[i]==">":
                block.append("&gt;")
            elif x[i]=="<":
                block.append("&lt;")
            else:
                block.append(x[i])
    
    return block
def aaa(x: str,doHTML: bool=False,ui: bool=True) -> str:
    global html
    block=aaa_list(x,doHTML)
    flag=False
    text=""
    flag_text=""
    flag_name=[]
    flag2=False
    ii=0
    if not type(x)==type("a"):
        raise TypeError("x is not str.")
    if not doHTML in [True,False]:
        raise TypeError("doHTML is not bool.")
    for i in block:
        ii+=1
        #print(i)
        #print(flag)
        #print(len(flag_name))
        if i in html:
            flag2=True
        if len(flag_text)==1 and flag:
            if i=="(" and flag2:
                #print(flag2)
                text=text+"<"+html[flag_text][0]+">"
                flag_name.append(flag_text)
                flag_text=""
                flag2=False
                #print("gefgeegyyg")
            elif i=="(":
                #print("")
                text=text+flag_text+"("
            else:
                if len(flag_name)-1==0:
                    flag=False
                    #print("<big><gib>")
                text=text+flag_text
                flag_text=""
                flag2=False
        elif flag and i==")":
            #print(i)
            try:
                text=text+"</"+str(html[flag_name[-1]][1])+">"
                del flag_name[-1]
            except:
                text=text+")"
            #print(len(flag_name)-1)
            if len(flag_name)==0:
                flag=False
            flag_text=""
            #print("aa")
        elif i=="\n":
            try:
                if html[flag_name[-1]][0]=="style":
                    text=text+"\n"
                else:
                    text=text+"<br>"
            except:
                text=text+"<br>"
                print("a",ii)

        else:
            if not i in ("(",")"):
                #print(text)
                if not flag2:
                    text=text+i
        if i in html:
            flag2=True
            flag=True
            flag_text=i
            #print("fack",i)
        #print(flag_name,ii)
        #print(flag_name)
    webui=""
    if ui:
        webui="""
<style>
under {
  text-decoration: underline;
}
code {
	background: inherit;
	font-size: inherit;
	color: inherit;
	border: 0;
	padding: 0;
	margin: 0;
}
h2 {
  font-weight: bold;
  border-left: 5px solid #4c9ac0;
  border-bottom: 2px dashed #B4B4B4;
  padding: 0.25em 0 0.3em 0.5em;
}
</style>
"""
    return text+webui
if "__main__"==__name__:
    print(html["|"])
    print(aaa_list("hello<>"))
    print(aaa("""!(a"(a))"""))
