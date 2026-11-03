# Interacción fluido-estructura estacionaria: Stokes + elasticidad lineal

Trabajo de grado de Matemáticas (Universidad de Cartagena, Facultad de Ciencias Exactas y Naturales).
Autora: Sharon Acosta.

Este repositorio contiene la tesis, los programas con los que se obtuvieron los resultados y las
instrucciones para volver a obtenerlos. No hace falta saber programar: basta con copiar y pegar los
comandos de esta guía.

## ¿De qué trata?

Imagina una cavidad llena de líquido con una viga elástica en el fondo. Cuando el líquido se mueve,
empuja la viga y la dobla. Pero al doblarse, la viga cambia el espacio por donde fluye el líquido.
Fluido y viga se influyen entre sí.

El trabajo resuelve ese problema en el computador con el **método de elementos finitos**. Primero
calcula el fluido, luego le pasa la fuerza a la viga, luego calcula cuánto se dobla, y repite hasta
que los dos resultados se ponen de acuerdo. Ese vaivén se llama **esquema particionado
Dirichlet-Neumann**. La tesis explica la teoría y los resultados.

## ¿Qué hay en cada carpeta?

| Carpeta | Qué contiene |
|---|---|
| `tesis/` | El texto de la tesis. `IFSA_Version_Final.pdf` es el documento final listo para leer; `IFSA_Version_Final.tex` es el código para volver a generarlo. |
| `programas/` | Los programas de cálculo. Ver la tabla de abajo. |
| `programas/salida_demo/` | Resultados ya calculados (mallas y campos de la simulación con N = 40) y las tres figuras que salen de ellos. |
| `imagenes/` | Las imágenes que usa la tesis. |
| `presentacion/` | Las diapositivas de la sustentación (`main.tex` y `frames.tex`), el guion y las hojas de repaso. |

### Los programas

| Archivo | Para qué sirve |
|---|---|
| `FSI_Particionado.edp` | **El programa principal.** Es el que produjo todos los resultados de la tesis (también aparece completo en el Anexo A). |
| `figuras_FSI.py` | Dibuja las tres figuras del Capítulo 3 a partir de lo que exporta el programa principal. |
| `Demo_Sustentacion.edp` | El mismo programa, pero muestra las gráficas en pantalla una por una. Se usó en la sustentación. |
| `figuras_demo.py` | Versión de `figuras_FSI.py` usada en la demostración. |
| `FluidoEstructura.edp` | Ejemplo previo, más sencillo, de una viga elástica. |
| `Poisson.edp` | Ejemplo de la documentación oficial de FreeFem++ (de Antoine Le Hyaric). Solo sirve para probar que la instalación funciona. |

## Qué instalar

Hay tres partes independientes. Instala solo la que necesites.

| Si quieres... | Instala | Versión usada |
|---|---|---|
| Volver a hacer el **cálculo** (archivos `.edp`) | [FreeFem++](https://freefem.org/) | **4.15** |
| Volver a dibujar las **figuras** (archivos `.py`) | [Python](https://www.python.org/) con los paquetes `numpy` y `matplotlib` | 3.x |
| Volver a generar la **tesis** o las diapositivas (archivos `.tex`) | [MiKTeX](https://miktex.org/) (Windows) o TeX Live (Linux/Mac). Trae `pdflatex` y `biber` | MiKTeX 24.1 |

Para instalar los paquetes de Python, abre una terminal y escribe:

```bash
pip install numpy matplotlib
```

## Cómo reproducir los resultados

Todos los comandos se escriben en una terminal (en Windows, PowerShell), **dentro de la carpeta
`programas/`**. Para entrar a ella:

```bash
cd ruta/donde/descargaste/trabajo-de-grado/programas
```

### Paso 1. Comprobar que FreeFem++ funciona (opcional)

```bash
FreeFem++ Poisson.edp
```

Debe abrirse una ventana con una gráfica. Si se abre, la instalación está bien.

### Paso 2. Correr la simulación de la tesis (Figuras 3.x)

```bash
FreeFem++ FSI_Particionado.edp -N 40 -out demo -export 1
```

Qué significa cada parte:

- `-N 40`: qué tan fina es la malla (40 subdivisiones por lado de la cavidad).
- `-out demo`: prefijo de los archivos que se generan (`demo_fluido.msh`, `demo_solido_campos.txt`, etc.).
- `-export 1`: guardar mallas y campos para poder dibujarlos después.

En pantalla aparecen las iteraciones con su residuo. Con el factor de relajación por defecto
(0,5) el residuo baja hasta 10⁻⁶ en 21 iteraciones, como dice la tesis.

### Paso 3. Dibujar las figuras

```bash
python figuras_FSI.py . demo figuras
```

Los tres argumentos son: carpeta donde están los datos (`.` es la carpeta actual), prefijo usado en el
paso 2 (`demo`) y carpeta donde se guardarán las imágenes (`figuras`, se crea sola).

Resultado: `FSI_velocidad_presion.png`, `FSI_desplazamiento_viga.png` y `FSI_malla_deformada.png`.

> **Atajo sin FreeFem++:** los datos del paso 2 ya están guardados en `programas/salida_demo/`.
> Puedes saltarte el paso 2 y hacer directamente
> `python figuras_FSI.py salida_demo demo figuras`.

### Paso 4. Estudio de convergencia (opcional, tarda más)

Este estudio compara mallas cada vez más finas contra una solución de referencia muy fina. Se
corren estos comandos **en este orden**:

```bash
FreeFem++ FSI_Particionado.edp -N 120 -ref 1
FreeFem++ FSI_Particionado.edp -N 10 -cmp 120
FreeFem++ FSI_Particionado.edp -N 20 -cmp 120
FreeFem++ FSI_Particionado.edp -N 40 -cmp 120
FreeFem++ FSI_Particionado.edp -N 80 -cmp 120
```

La primera línea calcula la referencia (`-ref 1` la guarda en `ref_u.txt` y `ref_d.txt`). Las demás
corren mallas más gruesas y miden el error contra ella. Busca en pantalla las líneas que empiezan
con `ERROR N=...`: son los errores de la tabla de convergencia de la tesis.

### Paso 5. Prueba sin relajación (opcional)

```bash
FreeFem++ FSI_Particionado.edp -N 40 -omega 1
```

Converge en 5 a 7 iteraciones y a la misma solución, como se explica en el Capítulo 3.

### La demostración con gráficas en pantalla

```bash
FreeFem++ Demo_Sustentacion.edp
```

Abre una ventana por cada gráfica; presiona ENTER para pasar a la siguiente.

## Cómo volver a generar la tesis en PDF

Desde la carpeta `tesis/`:

```bash
pdflatex IFSA_Version_Final.tex
biber IFSA_Version_Final
pdflatex IFSA_Version_Final.tex
pdflatex IFSA_Version_Final.tex
```

(Se corre `pdflatex` varias veces para que los índices y las referencias queden bien.) El resultado
es `IFSA_Version_Final.pdf` con 95 páginas.

Las diapositivas se generan igual, desde la carpeta `presentacion/`, con `pdflatex main.tex`. La
imagen decorativa de la portada original no se incluyó por su tamaño; sin ella las diapositivas
salen igual, solo que con la portada sin esa imagen.

## Qué se verificó y qué no

- **Verificado:** la tesis se compila desde cero (95 páginas, igual que el PDF incluido) y
  `figuras_FSI.py` regenera las tres figuras a partir de `programas/salida_demo/`.
- **No se pudo volver a verificar:** los programas `.edp`. Se corrieron con FreeFem++ para obtener
  los resultados de la tesis, pero al preparar este repositorio FreeFem++ ya no estaba instalado en
  el equipo de la autora. Los comandos de arriba son los que describe el Anexo A de la tesis.

## Qué no está en este repositorio

Por privacidad o tamaño se dejaron fuera las cartas y trámites administrativos, las
correcciones del jurado, las versiones anteriores de la tesis y los PDF pesados de la
presentación.

## Autoría y licencia

Todavía no se ha elegido una licencia. Mientras tanto, el código y el texto son de la autora y
cualquier reutilización requiere su permiso. `Poisson.edp` es un ejemplo de la documentación de
FreeFem++ y conserva su encabezado original.
