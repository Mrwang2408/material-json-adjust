#import json            ###有库我就是不用，欸嘿嘿就是玩###
import os

#keyWords = ['ESSL_310','Direct3D_SM40','Direct3D_SM50','Direct3D_SM60','Direct3D_SM65','Metal']

keyWords = ['ESSL_310','Metal']

directory = 'src' 
for filepath,dirnames,filenames in os.walk(directory):  
    for filename in filenames:
        if filename.endswith('.json'):  
            with open(os.path.join(filepath,filename), 'r', encoding='utf-8') as file: 
                print (filename)
                a = 0
                a2 = 0
                b = 1
                b2 = 0
                d1 = 0
                d2 = 0
                d3 = False
                p1 = 0
                q1 = 0
                p2 = 0
                q2 = 0
                k1 = False
                k2 = False
                k3 = False
                w0 = 0
                content1 = ''
                content2 = ''
                while True:
                    char = file.read(1)
                    if not char:
                        content1+='}'
                        print('Reached end of file,',b,'lines in total.','(',a,')')
                        with open(os.path.join(filepath,filename), 'w', encoding='utf-8') as file:
                            file.write(content1)
                        break
                    a+=1 
                    b2+=1 
                    if char == '\n': b+=1
                    elif char == '"': d3 = ~d3
                    elif char == '[': d2+=1
                    elif char == ']': d2-=1
                    elif char == '{':
                        d1+=1
                        if d2 == 2 and d1 == 3:
                            p1 = a 
                            q1 = b
                            k2 = True
                    elif char == '}':
                        d1-=1
                        if d2 == 2 and d1 == 2 and k2:
                            p2 = a
                            q2 = b
                            k2 = False
                            #print (p1,p2,q1,q2)  
                            if not k1:
                                w0 += 1
                                file.seek(a+7)
                                char4 = file.read(1)
                                #print (char4)
                                #w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0w0
                                if char4 == ']' or w0 == 2 :
                                    content2+='        }\n'
                                    w0 = 0
                                else:
                                    content2+='        },\n'
                                file.seek(a)
                                content1+=content2
                            k1 = False
                            #print (content2)
                            content2 = ''
                            k3 = True   
                    if d1 == 4 and d2 == 2 and d3:
                        a2+=1
                    elif a2 != 0:
                        file.seek(a-a2)
                        char2 = file.read(a2-1)
                        #print (char2)
                        if char2 in keyWords: 
                            k1 = True
                        file.seek(a)
                        a2 = 0
                    if char == '\n':
                        file.seek(a-b2)
                        char3=file.read(b2-1)
                        #print (char3)
                        #print (k2)
                        if not k2 and not k3:
                            content1+=(char3)
                            content1+='\n'
                        elif k2 and not k3 :
                            content2+=(char3)
                            content2+='\n'
                        file.seek(a)
                        b2 = 0 
                        k3 = False

                #file.close()
                #print('end')
                #print (content1)

    """
            break
            char2 = file.read(8)
            print (char2)
            file.seek(a)
            
            if char2 == 'ESSL_100':
                print ('yyyyyy')
                a+=8
            else
                file.seek(a)
     """              
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    