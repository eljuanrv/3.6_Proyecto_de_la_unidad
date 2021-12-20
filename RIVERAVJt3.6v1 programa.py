
import numpy as np
import cv2
import os
#LIMPIAR LA CONSOLA
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#CAPTURAR IMAGEN
def capturar():
	cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
	ret,frame = cap.read() # return a single frame in variable `frame`
	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cap.release()
	cv2.destroyAllWindows()
	return frame

#OBTENER LA HORA
def hora(gray):
	clearConsole()
	img=gray
	ret,gray = cv2.threshold(gray,70,255,cv2.THRESH_BINARY)
	edges = cv2.Canny(gray, 230, 255, apertureSize = 3)

	lines = cv2.HoughLines(edges, 1, np.pi/180, 50)
	angulos=[]
	for line in lines:
	    rho, theta = line[0]
	    try:
	      if (theta > angulos[-1]+0.4 or theta < angulos[-1]-0.4 ) and len(angulos)<2:
	        angulos.append(theta)

	    except:
	      angulos.append(theta)

	if len(angulos)==2:

		horas=str((angulos[1]*6/np.pi)+6)
		if horas[1]=='.':
			horas=horas[0]			
		else:
			horas=horas[0:2]

		minutos=round((angulos[0]*30/np.pi)+30)

		print(f'Angulo minutos = {round(angulos[0]*180/np.pi + 90)}')
		print(f'Angulo horas = {round(angulos[1]*180/np.pi + 90) }')
		print(f'{horas} : {minutos}')
		print()

	else:
		print(f'error longitud de {len(angulos)}')
		print(angulos)





#PRUEBA 1
input('Presiona enter')
hora(capturar())
#PRUEBA 2
input('Presiona enter')
hora(capturar())
#PRUBA 3
input('Presiona enter')
hora(capturar())

