import sys

lines = [ line.strip() for line in sys.stdin ]

s = int(lines[0])
print(lines[0] + ":")
for i in range(2,s):
    
    if s%(2*i-1) == 0:
        print(f"{i},{i-1}") 

    if (s-1+i)%(2*i-1) == 0:
        print(f"{i},{i-1}")     
       
    if s%(2*i) == 0 :
        print(f"{i},{i}")  
          
    if (s+i)%(2*i) == 0 :
        print(f"{i},{i}")
       
    
       
          
      
   
    #   
    #if a ,b all has x row , a = i  , b = i or i-1
    #i*x + (i-1)*x = s
    #2*i*x = s
    
    
    #if a has x row , b has x-1 row ,a = i ,b = i or i-1
    #i*x + (i-1)*(x-1)  = s  
    #i*x + i*(x-1) = s


          

            
    
            
        
    
        
   