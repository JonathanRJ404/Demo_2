import math
import numpy as np

h= 1.53*10**-3
Er=4.4
f=2.45*10**9
tand=0.018
c=3*10**8

### Calcul des dimensions du rectangle
W= (c/(2*f))*np.sqrt(2/(Er+1))

print('base du rectangle',W,'m')

Eff=((Er+1)/2)+((Er-1)/2)*(1+12*h/(W))**(-0.5)                          
dL= 0.412*h*((Eff+0.3)*((W/h)+0.264)/((Eff-0.258)*((W/h)+0.813)))
L=(c/(2*f*(Eff)**(0.5)))-2*dL

print('La hauteur du rectangle',L,'m')

### Calcul de la longueur de la ligne quart d'onde
lamda= (c/(f*np.sqrt(4.4)))
print('lamda=',lamda)
Lquart= lamda/4
print('la longueur de la ligne quart d onde ',Lquart,'m')

### Calcul de la hauteur des encoches

Yo= (10**(-4))*(0.001699*(Er)**7+0.13761*(Er)**(6)-6.1783*(Er)**(5)+93.187*(Er)**(4)-682.69*(Er)**(3)+2561.9*(Er)**(2)-4043*Er+6697)*(L/2)
print('la hauteur des encoches',Yo,'m')

### Calcul des dimensions du triangle
a= (2*c)/(3*f*np.sqrt(Er))

H= np.sqrt(a*a-(0.5*a)**2)

Y1= (10**(-4))*(0.001699*(Er)**7+0.13761*(Er)**(6)-6.1783*(Er)**(5)+93.187*(Er)**(4)-682.69*(Er)**(3)+2561.9*(Er)**(2)-4043*Er+6697)*(H/2)

print('longueru des cotés du triangle ', a,'m')

print('hauteur du triangle',H'm')

print(' Hauteur des encoches du triangle',Y1'm')

