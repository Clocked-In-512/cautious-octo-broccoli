##Robert Fernandez
##Complete/Incomplete
##Write numbers 50 to 100 inclusive to file number_list.

def main():
    
  #Open file
    outfile = open('number_list.txt', 'w')
    
  #Write numbers 50 to 100 to file
    for i in range(50, 101):
        outfile.write(str(i) + '\n')
        
  #Close file
    outfile.close()  

main()
