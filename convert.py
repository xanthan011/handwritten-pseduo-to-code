import re
newf = open("b.cpp",'w')

# Function for adding return datatype to a function
def modifyfunction(line):
    if line[:4]=='main':
        print('int '+line+'{', file=newf)
    else:
        print('void '+line+'{', file=newf)
    # print('void '+line+'\n')

# Function for assigning datatype (here int for specific)
def datatypeassign(line):
    print('int '+line+';', file=newf)

# Function for modifying if statement
def addifsyntax(line):
   # words = re.split("\s",line)
    print(line+'{', file=newf)

def modifyifthen(line):
    line = line.replace('then ','')
    printword = re.search(r'\Aprint', line)
    if printword:
        printstatement(line)
    # print(line+'\n}', file=newf)

def modifyelse(line,nextline):
    print(line + '{', file=newf)
    printword = re.search(r'\Aprint', nextline)
    if printword:
        printstatement(nextline)
    # print(nextline+'\n}', file=newf)

def closefunction(line):
    line = line.replace('end','}')
    print(line,file=newf)

def printstatement(line):
    line = line.replace('print ','std::cout<<')
    print(line+';\n}',file=newf)


def convert_code():
	
	cnt = 0
	

	f = open("a.txt", "r")
	while 1:
	    if cnt == 0:
        	print("#include<bits/stdc++.h>\n", file=newf)
	        cnt = cnt + 1
        	# #include<iostream>
	        # using namespace std;
	    line = f.readline()
	    line = line.rstrip('\n')

	    paranthesis_of_function = re.search(r'\(\)', line)
	    character = re.search(r'\A[a-z]',line)
	    ifstatement = re.search(r'\Aif',line)
	    ifthenline = re.search(r'\Athen',line)
	    elseword = re.search(r'\Aelse',line)
	    endofdef = re.search(r'\Aend', line)
	    # printword = re.search(r'\Aprint', line)
	
	    # print(character)
	    # print(line[-1])
	    if not line:
	        break
	    if paranthesis_of_function:
	        modifyfunction(line)
	    elif ifstatement:
	        addifsyntax(line)
	    elif ifthenline:
	        modifyifthen(line)
	    elif elseword:
	        nextline = f.readline()
	        nextline = nextline.rstrip('\n')
	        modifyelse(line,nextline)
	    elif endofdef:
	        closefunction(line)
	    elif character:
	        datatypeassign(line)



	f.close()
	newf.close()




