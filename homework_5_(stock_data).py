import os

directory = os.path.join("C:/Users/kater/Documents/Stock_data/")
for root,dirs,files in os.walk(directory):
  for file in files:
    if file.endswith(".csv"):
      try:
        f = open("C:/Users/kater/Documents/Stock_data/" + file, 'r')
        print("Opened " + file + "...")
        g = open("C:/Users/kater/Documents/Stock_data/" + file[:len(file)-4] +"1.csv", 'w')
        lines = f.readlines()
        header = True
        for line in lines:
          line = line.replace('\n', '')
          L = line.split(',')
          if header:
            header = False
            L.append("Change")
          else:
            change = round( ( float(L[4]) - float(L[1]) ) / float(L[1]) , 6)
            L.append( str( change ) )
          g.write( ','.join(L) + "\n" )
        g.close()
        f.close()
      except:
        print("Can't open file " + file)