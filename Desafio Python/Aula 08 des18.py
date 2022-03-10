from math import radians, sin,tan,cos
num = float(input('digite o ângulo '))
seno = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))
print('O ângulo de {}º, o seu seno vale  {:.2f},\n o cosseno vale {:.2f},\n e a sua tangente vale {:.2f}. '.format(num, seno, cos, tan))
