Autor: Efrain Noa
Oregon State University

Este es un instructivo para el codigo "curva_alt_vol_1"

Descripción:
	- Este codigo calcula el volumen que hay por debajo de uno o varios poligonos.
	- Estos poligonos pueden representar lagunas, wetlands, lagos, etc

Informacion requerida:
	- Un archivo Raster del terreno (DEM)
	- Un archivo vector con poligonos cerrados. Verificar que cada linea de atributo
	  debe representar un solo poligono.
	- Estos DOS archivos de preferencia deben ser almacenados en una carpeta "data"

Forma de ingresar base de datos:
	- Hay dos formas de ingresar los archivos requeridos (DEM and SHAPEFILE)
	- External Input: mediante function BOX. El ingreso se hace interactivo con el usuario
	- Internal Input: El ingreso se hace dentro del codigo

Importante:
	- El archivo raster y vector deben estar proyectados en la misma coordenada.
	- La coordenada debe ser caulquier "Projected coordinate system" y NO "Geographic coordinate system"

Funciones:
	- main_code: volumen_cal.py
	- box1.py: USer interface code. Para solicitar los nombres de los archivos externos
	- Vol.py: Calculo volumenes mediante numpy
	- add_fiel_way2.py: adiciona un campo en los atributos del shapefile, para almacenar el volumen calculado
	
Salidas:
	- El mismo archivo "shapefile" con un campo conteniendo los volumenes por cada poligono
	- Un folder "scratch" con un archivo raster y otro vector. Estos archivos no son importantes,
	  fueron calculos provisionales.
	
