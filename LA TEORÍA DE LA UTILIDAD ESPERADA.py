import numpy
n = int(input('ingrese el numero de iteraciones'))


R = []
a = -1
for i in range(0,n):
  print('PARA a',i)
  x = float(input('ingresa elvalor de xi1: '))
  px = float(input('ingresa elvalor de pxi1: '))
  y = float(input('ingresa elvalor de xi2: '))
  py = float(input('ingresa elvalor de pxi2: '))


  r = ((x**(1/3))*px)+((-y)*py)


  print('Los valores de a', i ,'son',x,px,y,py)
  print('El valor maximo esperado es: ',r)
  
  
  R.append(r)

  

  
Rf = numpy.array(R)
Rfmax = Rf.max()
ps = numpy.where( Rf == Rfmax)
print('La Utlidad mas alta esperada es',Rfmax, 'Por lo tanto se suguiere elegir la opcion  a', ps[0])