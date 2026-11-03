# Explicaciones sencillas y variables de la presentación

**Cómo usar este documento:**
- **Parte A:** toda la teoría, explicada en sencillo y en el orden de las diapositivas. Cada tema tiene 🧠 una imagen para entenderlo, 👉 la idea clave y 🎤 la frase para decir en la sustentación.
- **Parte B:** las tablas con cada variable y símbolo. Al final están las letras que tienen **más de un significado**.
- Lo que te trabe, pásalo al tablero del armario.

---

# PARTE A — Explicaciones sencillas

## A1. Espacios de Sobolev: L², H¹, Hᵏ⁺¹, H^½

Son "clubes" de funciones, según qué tan suaves son.

- **L²:** funciones cuyo cuadrado tiene área finita: ∫u² < ∞. Pueden tener saltos.
- **H¹:** funciones de L² cuyas **primeras derivadas** también están en L². No pueden tener saltos, pero sí "picos" (esquinas).
- **Hᵏ⁺¹:** funciones con k+1 derivadas en L². Mientras más grande el número, más suave la función.
- **H^½(∂Ω):** el club de los **valores en el borde** de las funciones H¹. Una función con un **salto** no entra.
- **Derivada débil:** una derivada que se define "por integración por partes". Sirve para funciones con picos, que no tienen derivada clásica en todos los puntos.

🧠 **Imagen:** L² es la entrada general; H¹ exige "sin saltos"; Hᵏ⁺¹ exige "muy suave".

👉 **Conformidad:** los polinomios a trozos **continuos** (P₁, P₂) están dentro de H¹. Por eso se pueden usar en Galerkin: V_h ⊂ H¹.

🎤 *"Trabajo en espacios de Sobolev porque la forma débil solo pide primeras derivadas en L², y los polinomios a trozos continuos pertenecen a H¹."*

---

## A2. La forma débil

1. Tomas la ecuación, por ejemplo −∇·σ = f.
2. La multiplicas por una función de prueba v.
3. Integras sobre el dominio.
4. **Integras por partes**: una derivada pasa de u a v.

Resultado: **a(u, v) = L(v) para toda v.**

👉 **Qué se gana:**
- Se piden **menos derivadas** a la solución: una en vez de dos.
- Las condiciones de **Neumann** (fuerzas en el borde) aparecen **solas** en la integral de borde: se llaman *naturales*.
- Las de **Dirichlet** (valores fijos) se imponen en el espacio: se llaman *esenciales*. Por eso las funciones de prueba valen 0 donde hay Dirichlet.

🧠 **Imagen:** para saber si una mesa está nivelada, no mides cada punto: pones canicas en muchos lugares y miras si alguna rueda. Cada v es una canica.

🎤 *"La forma débil reduce la regularidad exigida a la solución e incorpora de manera natural las condiciones de Neumann."*

---

## A3. Teorema de Lax-Milgram: ¿hay solución, y es única?

Si se cumplen tres cosas:
1. **a es continua:** |a(u, v)| ≤ M‖u‖‖v‖. *No empuja infinitamente fuerte.*
2. **a es coerciva:** a(v, v) ≥ α‖v‖². *Siempre "sostiene" con una fuerza mínima: no hay direcciones donde se afloje.*
3. **L es continua:** |L(v)| ≤ C‖v‖. *Los datos no son infinitos.*

→ Entonces **existe una única solución**.

🧠 **Imagen:** un resorte. Si es firme (coercivo) y no infinitamente duro (continuo), para cada fuerza hay exactamente una posición de equilibrio.

👉 **En Poisson:** la continuidad sale de **Cauchy-Schwarz** y la coercividad de **Poincaré** (si la función vale 0 en el borde, controlar su derivada controla la función).

👉 **En tu trabajo:** Lax-Milgram sirve para el **sólido** (gracias a Korn, ver A11), pero **no** para Stokes (ver A10).

🎤 *"Lax-Milgram garantiza existencia y unicidad cuando la forma bilineal es continua y coerciva y el funcional es continuo."*

---

## A4. El método de Galerkin y KU = F

**El problema de fondo:** una función tiene infinitos valores y la computadora solo maneja una cantidad finita de números. Galerkin cambia "encontrar una función" por "encontrar unos cuantos números".

1. Divides el dominio en triángulos: la malla.
2. Buscas la solución entre funciones **simples**: polinomios por pedazos. Ese conjunto es **V_h**, dentro de V.
3. Cada nodo tiene una función base φⱼ con forma de **carpita**: vale 1 en su nodo y 0 en los demás.
4. La solución aproximada es una suma de carpitas: **u_h = U₁φ₁ + U₂φ₂ + … + U_Nφ_N**. Las incógnitas son solo los números Uⱼ: la altura de cada carpita.
5. Pruebas con las mismas carpitas (v = φᵢ) y sale **KU = F**:
   - **K** (matriz de rigidez): K_ij = a(φⱼ, φᵢ), cuánto se influyen los nodos i y j.
   - **U:** los valores en los nodos.
   - **F** (vector de carga): F_i = L(φᵢ), las fuerzas en cada nodo.

👉 **K es dispersa:** casi todo son ceros, porque dos nodos lejanos no comparten triángulo. Y es invertible gracias a la coercividad.

🧠 **Imagen 1:** dibujar una curva uniendo puntos con rayitas rectas. Más puntos (h más pequeño), mejor dibujo.
🧠 **Imagen 2:** la ley de Hooke de muchos resortes conectados: F = k·x, pero con miles de resortes.

🎤 *"Galerkin busca la solución en un espacio de polinomios a trozos y la convierte en el sistema lineal KU = F."*

---

## A5. Ortogonalidad y lema de Céa

**Ortogonalidad: a(u − u_h, v_h) = 0.** El error es "perpendicular" a todas las funciones simples: Galerkin escoge la mejor que puede.

🧠 **Imagen:** la **sombra** de un palo sobre el piso con el sol justo arriba. La sombra es el punto del piso más cercano al palo, y lo que sobra (el error) apunta perpendicular al piso. u es el palo, V_h el piso y u_h la sombra.

**Lema de Céa: ‖u − u_h‖ ≤ (M/α) · inf ‖u − v_h‖.**
"El error de Galerkin es, como mucho, M/α veces el error de la **mejor aproximación posible** dentro de V_h."

- **inf ‖u − v_h‖:** lo mejor que cualquier función simple podría hacer.
- **M/α:** un número fijo que no depende de la malla.

🧠 **Imagen:** un GPS que te garantiza que tu ruta es, como mucho, el doble de larga que la ruta perfecta.

👉 **Por qué es tan importante:** cambia la pregunta difícil "¿qué tan bueno es Galerkin?" por una más fácil: "¿qué tan bien pueden los polinomios imitar a u?".

🎤 *"El lema de Céa garantiza que el error de Galerkin es comparable al de la mejor aproximación posible en el espacio discreto."*

---

## A6. Orden de convergencia y la letra pequeña de la regularidad

Si usas polinomios de grado k y la solución es **suficientemente suave** (u ∈ Hᵏ⁺¹):

| Qué mides | Cómo baja el error | P₁ (k = 1) | P₂ (k = 2) |
|---|---|---|---|
| **Las pendientes** (norma H¹) | hᵏ | h | h² |
| **Los valores** (norma L²) | hᵏ⁺¹ (Aubin-Nitsche) | h² | h³ |

- h → si divides h entre 2, el error se divide entre **2**.
- h² → entre **4**.
- h³ → entre **8**.

🧠 **Por qué las pendientes son peores:** al dibujar una curva con rayitas, la *altura* queda cerca, pero la *inclinación* salta de golpe en cada punto.

👉 **Aubin-Nitsche** es un argumento de **dualidad**: usa un problema "auxiliar" para demostrar que los valores ganan un orden extra sobre las pendientes.

👉 **La letra pequeña:** todo esto **solo vale si u es suave**. En tu caso la velocidad de la pared **salta** en las esquinas, u no es suave, la promesa de h³ no aplica y observas **h¹**. **La teoría explica tu resultado.**

🎤 *"Si la solución es suficientemente regular, el error baja como hᵏ en H¹ y como hᵏ⁺¹ en L². Esa hipótesis de regularidad es la que explica la tasa que observo."*

---

## A7. Malla, elemento de referencia y cuadratura (cómo calcula la computadora)

- **Elemento de referencia K̂:** un triángulo "modelo" con vértices (0,0), (1,0) y (0,1). Todas las cuentas se hacen ahí.
- **Transformación afín F_K:** x = B_K x̂ + b_K. Estira, gira y mueve el triángulo modelo hasta el triángulo real. **B_K** es la matriz jacobiana y **b_K** la traslación.
- **Jacobiano J_K = det B_K:** cuánto cambia el área. Si J_K > 0 el triángulo está bien; si J_K ≤ 0 está volteado.
- **Cuadratura:** las integrales se aproximan como una suma ponderada de valores en puntos especiales (**puntos de Gauss**). Para P₁ basta un punto, el baricentro.
- **Ensamblaje:** se calcula la "mini-matriz" de cada triángulo y se suman todas en la K global.

🧠 **Imagen:** un molde de galleta. Haces todas las cuentas en el molde perfecto y luego lo estiras para que encaje en cada triángulo real.

🎤 *"Las integrales se calculan en un elemento de referencia mediante una transformación afín y cuadratura de Gauss, y luego se ensamblan en la matriz global."*

---

## A8. Crímenes variacionales y lema de Strang

La teoría supone que las integrales son **exactas** y que V_h ⊂ V. En la práctica eso no siempre se cumple:
1. **Integración numérica:** la cuadratura aproxima las integrales.
2. **Aproximación del dominio:** un borde curvo se aproxima con segmentos rectos.

Strang llamó a esto **"crímenes variacionales"**. El **primer lema de Strang** dice que, si esos errores se mantienen controlados, la convergencia se conserva.

🧠 **Imagen:** "pequeñas trampas" del cálculo. Si son pequeñas, no arruinan el resultado.

🎤 *"Los crímenes variacionales son errores de consistencia, como la cuadratura; el lema de Strang garantiza que, controlados, no destruyen la convergencia."*

---

## A9. El problema acoplado y la no-linealidad geométrica

**Qué se busca:** la terna **(u, p, d)**: la velocidad y la presión del fluido y el desplazamiento de la estructura, en Ω = Ω_f ∪ Ω_s.
- El **fluido** se rige por **Stokes**.
- La **estructura** se rige por la **elasticidad lineal** (ley de Hooke).

👉 **La no-linealidad geométrica:** Stokes es lineal y la elasticidad también, pero el fluido vive en un dominio **Ω_f(d)** que **depende del desplazamiento d**, y d depende de lo que haga el fluido. Esa dependencia circular hace **no lineal** al problema completo.
- El fluido genera esfuerzos σ_f que **deforman el sólido**.
- Al deformarse **el sólido** (⚠ no "el fluido"), cambia la frontera del fluido, y con ella el lugar donde se calculan las derivadas.

🧠 **Imagen:** caminar sobre un trampolín. Tu peso hunde la lona, y la lona hundida cambia dónde pisas. **El problema modifica el lugar donde se resuelve el problema.**

🎤 *"Aunque Stokes y la elasticidad son lineales, el problema acoplado es no lineal, porque el dominio del fluido depende del desplazamiento del sólido: el fluido deforma al sólido, y el sólido modifica la pista por donde se mueve el fluido."*

---

## A10. Stokes y la condición inf-sup

**Stokes:** −∇·σ_f = 0 y ∇·u = 0. Es un fluido lento y viscoso (Re ≪ 1), **sin inercia**. La fuerza de la presión se equilibra con la fricción viscosa.

- **σ_f = −pI + 2μ_f ε(u):** presión, que empuja igual en todas direcciones, más fricción viscosa.
- **∇·u = 0:** incompresible. Si se aprieta por un lado, se expande por el otro.
- **Si te preguntan por la forma en componentes (μ_f Δu):** ∇·(2μ ε(u)) = μΔu + μ∇(∇·u), y el último término es 0 por incompresibilidad.

👉 **Stokes NO es coercivo:** en la forma débil la presión no aparece "al cuadrado", así que no hay control sobre p. **Lax-Milgram no aplica.**

👉 **Babuška-Brezzi y la condición inf-sup (LBB):** se pide que los espacios de velocidad y de presión sean **compatibles**: para cada presión discreta tiene que existir una velocidad que la "sienta" a través de la divergencia, con una constante β > 0 que no depende de h.
- Si falla, aparecen **modos espurios**: presiones con oscilaciones falsas, en "tablero de ajedrez".
- **P₁/P₁ falla**; **Taylor-Hood P₂/P₁ cumple**.

👉 **Presión de media cero:** como solo aparece ∇p, la presión está definida "a menos de una constante". La media cero **solo fija esa constante**; la estabilidad la da inf-sup.

👉 **Sistema de punto de silla:** la matriz de Stokes tiene un **cero** en la esquina, [A Bᵀ; B 0]. No es definida positiva, y por eso hace falta inf-sup.

🧠 **Imagen:** velocidad y presión son un equipo. Si la presión tiene "más jugadores" de los que la velocidad puede marcar, quedan jugadores libres que oscilan: los modos espurios.

🎤 *"Stokes no es coercivo, así que la estabilidad se garantiza con la condición inf-sup de Babuška-Brezzi; por eso uso el par Taylor-Hood P₂/P₁."*

---

## A11. Elasticidad lineal: deformaciones, esfuerzos, Navier-Lamé y Korn

**El orden de las ideas (diapositiva "Subsistema de la estructura"):**
1. **Cinemática:** derivas el desplazamiento d → **tensor de deformaciones ε**: *cuánto se deforma*.
2. **Constitución:** ley de Hooke → **tensor de esfuerzos σ**: *qué fuerzas internas aparecen*.
3. **Equilibrio:** leyes de Newton → **ecuaciones de Navier-Lamé**: *las fuerzas se compensan*.

### El tensor de deformaciones ε(d) = ½(∇d + ∇dᵀ)

🧠 Imagina un **cuadradito diminuto** dibujado sobre la viga. Al deformarse la viga, el cuadradito cambia de dos maneras:

- **ε_xx y ε_yy, estiramiento o compresión axial.** "Axial" significa **a lo largo de un eje**. ε_xx = ∂d_x/∂x dice cuánto se **alarga** (positivo) o se **acorta** (negativo, compresión) el lado horizontal. ε_yy, lo mismo con el lado vertical.
  → El cuadradito se vuelve un **rectángulo**.
- **ε_xy, cizalladura o distorsión angular.** Las esquinas dejan de ser de 90°.
  → El cuadradito se vuelve un **rombo**.
  🃏 **Imagen:** un mazo de cartas sobre la mesa al que empujas la carta de arriba hacia un lado. Las cartas no se estiran, pero el mazo se "inclina". Eso es cizalladura.
- **tr ε = ε_xx + ε_yy = ∇·d:** cuánto cambió el **volumen** (en 2D, el área) del cuadradito.
- Es "**lineal**" porque desprecia términos pequeños al cuadrado: solo vale para **pequeñas deformaciones**.

🎤 *"El tensor de deformaciones describe cómo cambia de forma cada punto: la diagonal mide estiramientos y compresiones a lo largo de los ejes, y la componente cruzada mide la distorsión angular."*

### El tensor de esfuerzos σ_s (se dice "de esfuerzos", no "de fuerzas")

ε dice **cuánto se deforma**; σ dice **qué fuerzas internas** aparecen por esa deformación (fuerza por unidad de área).
- **σ_xx, σ_yy:** fuerzas que **jalan o empujan** a lo largo de cada eje.
- **σ_xy:** fuerza que **raspa de lado**, como la fricción entre las cartas.

**Ley de Hooke:** σ_s = λ_s (tr ε) I + 2μ_s ε. El esfuerzo es **proporcional** a la deformación, como en un resorte.
- **λ_s** responde a los cambios de **volumen**.
- **μ_s** (módulo de cizalla) responde a los cambios de **forma**. Con μ_s grande, el material se resiste más a volverse "rombo".

### Navier-Lamé: −∇·σ_s = f_v

⚠ **∇· es DIVERGENCIA, no gradiente.**
- **Gradiente** (∇, sin punto): a una función le asigna la dirección en la que crece.
- **Divergencia** (∇·, con punto): mide cuánto se **desbalancean** las fuerzas en un punto.

🧠 **Qué dice la ecuación:** en cada punto de la viga, las fuerzas internas **compensan exactamente** a las externas, así que la viga queda quieta, en equilibrio.

**f_v es la fuerza de volumen:** actúa sobre **todo el cuerpo**, no solo en el borde. En tu caso es el **peso propio** de la viga:
- **f_v = (0, g)**: 0 en x (nada empuja de lado) y g en y.
- **g = −0.05**: negativa porque va **hacia abajo**.
- En la diapositiva de la forma débil aparece como **f_s**: es la misma fuerza.

👉 **En la presentación:** no expliques las componentes una por una. Di la frase de abajo (unos 15 segundos) y pasa a la siguiente; si el jurado quiere detalle, te pregunta.

🎤 *"El equilibrio del sólido lo dan las ecuaciones de Navier-Lamé: la divergencia de los esfuerzos equilibra la fuerza de volumen, que aquí es el peso propio de la viga."*

### La desigualdad de Korn

👉 **Desigualdad de Korn:** ‖ε(w)‖ ≥ C_K ‖w‖_H¹. Controlar **solo la parte simétrica** del gradiente (las deformaciones) controla **todo** el desplazamiento, *siempre que el cuerpo esté sujeto* en parte del borde.
- **Por qué hace falta estar sujeto:** un giro o una traslación rígida mueven el cuerpo sin deformarlo (ε = 0). Al empotrar la viga se eliminan esos movimientos.
- **Para qué sirve:** da la **coercividad** de la elasticidad → se aplica **Lax-Milgram** → existe solución única.

🧠 **Imagen:** si una regla está atornillada en los extremos, la única forma de moverla es doblándola. Medir cuánto se dobla te dice cuánto se movió.

🎤 *"La desigualdad de Korn da la coercividad de la forma de elasticidad en desplazamientos empotrados, y con ella Lax-Milgram garantiza existencia y unicidad para el sólido."*

---

## A12. Condiciones en la interfaz

1. **Compatibilidad geométrica:** x_actual = x_ref + d. La interfaz se mueve con el sólido.
2. **Cinemática (no deslizamiento):** u = 0. En estado estacionario, el fluido está quieto pegado a la viga.
3. **Dinámica (acción y reacción):** σ_f n_f + σ_s n_s = 0. Lo que el fluido empuja, el sólido lo recibe.

👉 **Normales:** n_f = −n_s. Cada una apunta "hacia afuera" de su propio dominio, así que son opuestas.

🎤 *"En la interfaz se imponen tres condiciones: compatibilidad geométrica, no deslizamiento y continuidad de tracciones."*

---

## A13. Monolítico frente a particionado, y la relajación

- **Monolítico:** todo junto en un solo sistema gigante. Es robusto, pero caro y mal condicionado.
- **Particionado (Dirichlet-Neumann):** cada física con su propio solver, y se iteran pasándose información:
  - El fluido recibe la **posición** de la interfaz (Dirichlet).
  - El sólido recibe la **fuerza** del fluido (Neumann).
- **Punto fijo:** repetir d → F(d) hasta que d deje de cambiar.
- **Relajación ω:** d_nuevo = ω·d̃ + (1 − ω)·d_anterior. "Medio paso" para no pasarse.
  - En tu caso **ω = 0.5** (21 iteraciones). Sin relajación (ω = 1) también converge, en 5 a 7, porque el acoplamiento es débil. 0.5 es **conservador**.
🧠 **Imagen:** dos personas acomodando un mueble a gritos: "un poco a la izquierda", "ahora a la derecha". La relajación es mover solo la mitad de lo que te dicen para no pasarte.

🎤 *"Uso un esquema particionado Dirichlet-Neumann con relajación constante, que permite reutilizar solvers independientes para cada física."*

### El efecto de masa añadida (así lo explicaste en el póster)

Cuando el fluido y el sólido tienen **densidades parecidas**, como sangre y arteria o agua y caucho, la inercia del fluido "arrastra" al sólido **como si fuera masa propia del sólido**, y la iteración Dirichlet-Neumann se vuelve **inestable**.
- **Aire empujando acero:** el efecto no importa.
- **Sangre empujando una arteria:** es brutal. Obliga a usar ω muy pequeño (y cuesta muchísimo) o esquemas monolíticos.
- **En tu caso no aparece:** el problema es **estacionario**, así que no hay inercia; además, el fluido es muy viscoso.

🧠 **Imagen:** intentar empujar un columpio que está dentro de una piscina. No mueves solo el columpio: también tienes que mover el agua que lo rodea, y eso lo hace pesar mucho más.

🎤 *"El efecto de masa añadida aparece cuando las densidades del fluido y del sólido son parecidas: la inercia del fluido actúa como masa extra del sólido y desestabiliza el esquema particionado. En mi caso estacionario no aparece, pero es una limitación conocida."*

### Sin inercia: el número de Reynolds (así lo explicaste en el póster)

**Re** compara la inercia con la viscosidad. Tu caso tiene **Re muy bajo**: el fluido es muy viscoso o se mueve muy despacio. Entonces los términos de inercia no cuentan, y Navier-Stokes se reduce a **Stokes**, que es lineal. Eso te permite concentrarte en lo difícil: **el acoplamiento** con el sólido.

🧠 **Imagen:** una cuchara moviéndose en miel. Si la sueltas, se detiene al instante: no tiene "impulso propio", solo la mueve la fuerza que le aplicas.

---

## A14. ALE: mover la malla del fluido

- **Lagrangiano:** la malla viaja pegada al material. ✗ Como el fluido gira, la malla se **enredaría** toda.
- **Euleriano:** la malla está quieta y el material pasa por ella. ✗ No podría **seguir a la viga** cuando se dobla.
- **ALE (Arbitraria Lagrangiana-Euleriana):** la malla se mueve como convenga. Los nodos del **borde siguen a la viga** y los del **interior se acomodan suavemente**. No hay que rehacer la malla: conserva su "topología" (los mismos triángulos, conectados igual).

**Extensión armónica:** el desplazamiento de la interfaz se "reparte" hacia el interior resolviendo una ecuación de **Laplace**, con la malla fija en las paredes. Las soluciones de Laplace son suaves, así que la malla no se arruga.
- El **coeficiente constante** α_m no es "porque es ALE": es solo la forma más simple de hacer la extensión. Una rigidez local 1/|K| es una mejora futura.

**El Jacobiano J_K (así lo explicaste en el póster):** si los triángulos se distorsionan demasiado, pueden quedar con **"área negativa"**, es decir, volteados, y eso hace fallar al solver. Se revisa con el determinante del Jacobiano de cada elemento: debe ser positivo.
- 👉 **Ahora puedes agregar:** *"y lo comprobé numéricamente en todo el dominio: el cociente mínimo entre el área deformada y la original es 0.945"*.
- Para desplazamientos grandes haría falta remallar o usar métodos de frontera inmersa.

🧠 **Imagen:** una sábana elástica clavada en los bordes. Si empujas un lado, toda la tela se acomoda suavemente, sin arrugarse.

🎤 *"Uso ALE porque la frontera del fluido se mueve con la viga: la malla sigue a la interfaz sin enredarse. El desplazamiento se extiende al interior con una extensión armónica, y comprobé que ningún elemento se invierte."*

---

## A15. Cómo se calcula la fuerza del fluido: proyección L²

- **σ_f** sale de **derivar** la velocidad P₂. Las derivadas dan funciones P₁ que **saltan** entre triángulos.
- **Proyección L²:** se busca la función **continua** P₁ más parecida a σ_f en norma L². Se calcula resolviendo un sistema con la **matriz de masa**: Mσ = b.
- Con ese σ_f continuo se calcula la tracción α·σ_f·n_s sobre la viga.
- **Alternativa más precisa (no implementada):** el **residuo variacional**, que obtiene las fuerzas nodales directamente de la ecuación del fluido, sin derivar en el borde. Queda como trabajo futuro.

🧠 **Imagen:** suavizar un dibujo hecho con piezas sueltas para que quede como una sola pieza continua.

🎤 *"La tracción se obtiene proyectando en L² el tensor de esfuerzos del fluido sobre el espacio continuo P₁."*

---

## A16. Las figuras de resultados

### Velocidad y presión
- La pared izquierda **sube** y arrastra el fluido: la recirculación se concentra en la **mitad izquierda**. En la derecha casi no hay movimiento.
- Presión **positiva arriba** y **negativa abajo**.
- En las **esquinas de la pared que se mueve** la presión es enorme (≈ 121 con N = 40), porque ahí la velocidad **salta** de 1 a 0: el dato de Dirichlet es **discontinuo** y la presión es **singular** (crece sin límite al acercarse a la esquina).

**¿Por qué se recorta la escala de color al percentil 98?**
🧠 Es como **tomar una foto con el sol de frente**: el sol es tan brillante que todo lo demás sale negro. En la cavidad la presión va de −1.7 a 1.7, pero en las esquinas llega a 121. Si la escala de colores fuera hasta 121, toda la figura se vería de un solo color. Por eso se "ajusta la exposición": los colores llegan solo hasta el valor que cubre el 98 % de los puntos.

🎤 *"Las esquinas tienen valores muy grandes por la singularidad, así que recorté la escala de color para que se vea el interior."*

### Respuesta de la viga y malla deformada
- La presión del fluido **empuja la viga hacia arriba**, contra su peso, y como es mayor cerca de la pared que se mueve, **alivia el lado izquierdo**.
- Por eso la deformación es **asimétrica**: el máximo, **0.103**, está en **x ≈ 6** y no en el centro (x = 5), que es donde estaría si solo pesara.
- Junto a la esquina hay una deformación local hacia arriba por la singularidad. Se queda siempre en el primer triángulo: es un efecto de la esquina, no de la viga.
- En la figura los desplazamientos están **amplificados ×5** para que se vean. El real es ≈ 5 % del espesor: deformaciones pequeñas.
- La malla deformada **no tiene triángulos volteados** (cociente mínimo de áreas 0.945).

🎤 *"El fluido empuja la viga hacia arriba y alivia su lado izquierdo, por eso el máximo desplazamiento, 0.103, está en x ≈ 6. La malla deformada se mantiene válida."*

---

## A17. Tu resultado de convergencia, de principio a fin

1. **No hay solución exacta**, así que se usa una **referencia muy fina**: N = 120.
2. Se calcula el error relativo E_N para N = 10, 20, 40 y 80.
3. **Orden q** = log(E_anterior / E_actual) / log 2. Tu resultado: **q ≈ 1** (1.00, 1.02 y 0.93).
4. **Por qué 1 y no 3:** en las esquinas, la pared que sube toca paredes quietas, así que el dato **salta** de U₀ a 0.
   - Una función con salto **no está en H^½** del borde → la solución **no es suave** → la promesa h³ (A6) no aplica.
   - Cerca de esas esquinas la presión crece como **1/r**.
   - En la malla, el salto se reparte en un solo triángulo y solo se resuelve al ritmo de h.
5. **Conclusión:** la teoría **explica** el resultado. No es un error del código.

👉 **La deflexión máxima se estabiliza:** cambia **menos del 1 %** entre N = 80 y la referencia N = 120.

### Diapositiva 26, versión corta (≈ 30 s) — ESTO es lo que dices

> 🎤 *"La teoría dice que, con elementos P₂, el error podría bajar como h al cubo, pero solo si la solución es muy suave. En mi caso no lo es: en las esquinas, la pared que sube toca paredes quietas, y la velocidad salta de golpe de 1 a 0. Ese salto le quita suavidad a la solución, y por eso el error baja solo como h. Es decir, la teoría explica mi resultado."*

Lo de **H^½** y **p ~ 1/r** guárdalo **solo por si te preguntan**.

---

## A18. Alcances, limitaciones y conclusiones

### Limitaciones del modelo físico
- **Stokes:** solo vale para Re ≪ 1 (sin inercia).
- **Elasticidad lineal:** solo para pequeñas deformaciones.
- **Estacionario:** no se ve la evolución en el tiempo, ni vibraciones ni *flutter*.
- **α = 0.2:** acoplamiento débil.

### Limitaciones numéricas (di las tres)
1. El esquema particionado es sensible a la **masa añadida** (A13).
2. El ALE puede fallar con **deformaciones grandes**, porque los elementos se invierten (A14).
3. La convergencia se midió contra una **referencia propia**, y la tasa está limitada por la **regularidad del caso** (A17).

### Conclusiones
1. **Esquema particionado viable:** Dirichlet-Neumann con **relajación** acopló Stokes y elasticidad en régimen estacionario, reutilizando solvers modulares.
2. **Estabilidad:** el par Taylor-Hood P₂/P₁ **garantiza la estabilidad de la presión** (cumple inf-sup), aunque por sí solo no garantiza la precisión de las tracciones en la interfaz.
3. **ALE:** la extensión armónica preservó la calidad de la malla en el rango de **deflexiones** considerado.
4. **Convergencia:** ⚠ no digas "fue bastante buena". Di: *"aproximadamente lineal, **explicada por la falta de regularidad** del caso"*.
5. **Puente teoría-computación**, en sencillo:
> 🎤 *"La teoría justifica cada decisión del código: la forma débil explica por qué trabajo en H¹, inf-sup explica por qué uso Taylor-Hood, Korn explica por qué el sólido tiene solución única, y la regularidad explica por qué el error baja como baja."*

### Trabajo futuro
Navier-Stokes; problema dinámico en el tiempo (por ejemplo con Newmark); grandes deformaciones con modelos hiperelásticos y el caso α = 1; relajación de Aitken o cuasi-Newton; regularizar el dato de la pared para recuperar el orden óptimo; calcular la carga con el residuo variacional; validación externa (Ghia et al.).

---

## A19. Errores del primer ensayo, para no repetirlos

| Dijiste | Lo correcto |
|---|---|
| "Esto no es necesario decirlo" (implementación propia) | ⚠ **SÍ dilo**: es la respuesta a la observación del jurado |
| Leer en voz alta las notas 💡 | Las 💡 son para ti; al jurado solo le dices lo 🎤 |
| "Gradiente del tensor" | **Divergencia** del tensor (∇·) |
| "Al deformarse el fluido" | Al deformarse **el sólido** |
| "La interfaz se mueve con el desplazamiento del fluido" | …del **sólido** |
| "Condición de no desplazamiento" | No **deslizamiento** |
| "Tensor de fuerza" | Tensor de **esfuerzos** |
| "Taylor-Hood fue el único que cumple inf-sup" | Es **un par estable** que cumple inf-sup (hay otros) |
| "El coeficiente es constante porque es ALE" | Es constante por **simplicidad** |
| Céa: "acotado por la mejor aproximación" | Acotado, **salvo una constante**, por la mejor aproximación |
| Aubin-Nitsche junto a H¹ | Aubin-Nitsche da el orden extra en **L²** |
| "Rango de fricciones" | Rango de **deflexiones** |
| "La convergencia fue bastante buena" | Aproximadamente lineal, **explicada por la regularidad** |
| Muchos "entonces" y "bueno" | Cámbialos por una **pausa corta**: suena más segura |

### Pronunciación

| Se escribe | Se dice más o menos |
|---|---|
| Neumann | **Nóiman** |
| Euler / euleriano | **Óiler** / oileriano |
| Céa | **Seá** |
| Aubin-Nitsche | **Obán-Níche** |
| Navier-Lamé | **Navié-Lamé** |
| inf-sup | **inf-sup** (ínfimo-supremo) |

⚠ **El guion del póster tiene datos viejos:** dice "10 iteraciones", "orden 2" y "relajación dinámica". **No los uses.** Ahora es: 21 iteraciones, orden 1 y relajación **constante**.

---

## A20. Lo que faltaba de la tesis (por si el jurado lo pregunta)

Estas tres cosas están en tu tesis pero no en las diapositivas. No tienes que explicarlas en la presentación: solo reconocerlas si te preguntan.

### 1. El interpolante nodal y el teorema del error de interpolación (capítulo 1)

- **Interpolante nodal Π_h u:** la función de V_h que **vale exactamente lo mismo que u en cada nodo**: Π_h u = Σ u(nodo j) · φⱼ. Son las "rayitas" del dibujo que une los puntos de la curva.
- **Para qué sirve:** Céa dice que el error de Galerkin es comparable al de la **mejor** aproximación. El interpolante es **una** aproximación concreta, y la mejor es al menos igual de buena. Así que basta con **medir el error del interpolante**.
- **Teorema del error de interpolación (con P₁):** si u ∈ H² y la malla es **regular**:
  - ‖u − Π_h u‖ en L² ≤ C h² |u|_H² → valores: **h²**
  - |u − Π_h u| en H¹ ≤ C h |u|_H² → pendientes: **h**
  Es exactamente la tabla de A6 para P₁, y la cuenta de la parábola (hueco = h²/4) es este teorema en su versión más sencilla.
- **Malla "regular":** que los triángulos **no se vuelvan muy aplanados** (como agujas) al refinar. Si se aplanan, la constante C se dispara. Tus mallas son estructuradas, con todos los triángulos iguales, así que lo cumplen.
- **Norma de energía:** cuando a(·,·) es simétrica, se puede medir con ‖v‖_E = √a(v,v), y en esa norma **Galerkin es exactamente la mejor aproximación**, sin constante. Es la "sombra" perfecta de A5.
- **Estimaciones "a priori" y "asintóticas":** *a priori* = se saben **antes** de calcular, sin conocer la solución; *asintóticas* = valen cuando **h es suficientemente pequeño**.

🎤 *"Por Céa, basta estimar el error del interpolante nodal; con elementos lineales y solución en H², ese error es de orden h² en L² y h en H¹, siempre que la malla sea regular."*

### 2. Teorema de Nanson (capítulo 2, nota del equilibrio en la interfaz)

- El sólido se describe en su configuración **de referencia** (sin deformar) y el fluido en la configuración **actual** (deformada). Para igualar fuerzas "de verdad", hay que traducir de una configuración a la otra: eso lo hace el **teorema de Nanson**, que dice cómo cambia un pedacito de superficie y su normal al deformarse.
- **En tu trabajo no hace falta:** como las deformaciones son **pequeñas**, la viga deformada y sin deformar son casi iguales, y se puede igualar directamente σ_s·n = σ_f·n.

🧠 **Imagen:** convertir pesos a dólares. Si la tasa de cambio es casi 1, puedes sumar directamente sin convertir.

🎤 *"En rigor habría que relacionar las configuraciones con el teorema de Nanson, pero bajo la hipótesis de pequeñas deformaciones se puede igualar directamente las tracciones."*

### 3. Cauchy-Schwarz y Poincaré (en Lax-Milgram, capítulo 1)

- **Cauchy-Schwarz:** |∫ f g| ≤ ‖f‖ · ‖g‖. "El producto de dos cosas no puede ser más grande que el producto de sus tamaños." Da la **continuidad**.
- **Poincaré:** si una función vale **cero en el borde**, controlar su derivada controla la función: ‖v‖ ≤ C ‖∇v‖. Da la **coercividad**.
  🧠 Si un trampolín está sujeto en los bordes y casi no se inclina en ningún punto, entonces no puede estar muy alto en ninguna parte.
- **Korn** (A11) es la "prima" de Poincaré para la elasticidad.

---

# PARTE B — Variables y símbolos

Ordenados en el orden en que aparecen en las diapositivas.

---

## 1. Método de elementos finitos (Galerkin y estimaciones de error)

| Símbolo | Qué es | En palabras sencillas |
|---|---|---|
| **Ω** | Dominio | La región completa donde se resuelve el problema |
| **𝒯_h** | Malla (triangulación) | Ω dividido en triángulos |
| **h** | Tamaño de malla | El tamaño típico de los triángulos; si h baja, la malla es más fina |
| **V** | Espacio de funciones continuo | Donde vive la solución exacta (por ejemplo H¹) |
| **V_h** | Espacio discreto, V_h ⊂ V | Polinomios a trozos sobre la malla: lo que la computadora puede manejar |
| **u** | Solución exacta | Lo que queremos y no conocemos |
| **u_h** | Solución aproximada (de Galerkin) | Lo que calcula el método |
| **v_h** | Función de prueba discreta | Se usa para "probar" la ecuación |
| **a(·,·)** | Forma bilineal | La parte de la ecuación que tiene a la incógnita (la "rigidez") |
| **L(·)** | Forma lineal | La parte de los datos: fuerzas, cargas |
| **K** (negrita) | Matriz de rigidez | K_ij = a(φⱼ, φᵢ). Cuánto se influyen los nodos i y j |
| **U** | Vector de incógnitas | Los valores de la solución en cada nodo |
| **F** | Vector de carga | F_i = L(φᵢ). Las fuerzas en cada nodo |
| **φᵢ** | Función base del nodo i | Vale 1 en su nodo y 0 en los demás |
| **a(u − u_h, v_h) = 0** | Ortogonalidad de Galerkin | El error es "perpendicular" al espacio discreto |
| **M** | Constante de continuidad de a | Cota: \|a(u,v)\| ≤ M‖u‖‖v‖ |
| **α** (en Céa) | Constante de coercividad de a | Cota: a(v,v) ≥ α‖v‖². ⚠ No confundir con el α del acoplamiento |
| **M/α** | Constante del lema de Céa | Cuánto peor que la mejor aproximación puede ser Galerkin |
| **inf** | Ínfimo | "La menor posible": la mejor aproximación dentro de V_h |
| **‖·‖_V** | Norma en V | Forma de medir el tamaño de una función |
| **k** | Grado del polinomio | P₁ → k = 1 (lineal), P₂ → k = 2 (cuadrático) |
| **P_k** | Polinomios de grado k por elemento | P₁ lineales, P₂ cuadráticos |
| **H¹** | Espacio de Sobolev de orden 1 | Funciones que, con sus primeras derivadas, son de cuadrado integrable |
| **H^(k+1)** | Espacio de Sobolev de orden k+1 | Funciones con k+1 derivadas de cuadrado integrable: "suficientemente suaves" |
| **L²** | Funciones de cuadrado integrable | ∫u² < ∞. Mide el error en la función misma |
| **\|u\|_(H^(k+1))** | Seminorma | Mide solo las derivadas de orden k+1: qué tan "curvada" es u |
| **C** | Constante | No depende de h |
| **h^k, h^(k+1)** | Orden de convergencia | Qué tan rápido baja el error al refinar. En L² se gana un orden (Aubin-Nitsche) |

---

## 2. El problema físico (fluido y sólido)

| Símbolo | Qué es | En palabras sencillas |
|---|---|---|
| **Ω_f** | Dominio del fluido | La cavidad |
| **Ω_s** | Dominio del sólido | La viga |
| **Ω_f(d)** | Dominio del fluido deformado | La cavidad depende de cómo se deforme la viga: de ahí la no-linealidad geométrica |
| **u = (u_x, u_y)** | Velocidad del fluido | Hacia dónde y qué tan rápido se mueve el fluido |
| **p** | Presión | Empuje del fluido, igual en todas las direcciones |
| **d = (d_x, d_y)** | Desplazamiento del sólido | Cuánto se movió cada punto de la viga |
| **σ_f** | Tensor de esfuerzos del fluido | σ_f = −pI + 2μ_f ε(u): presión más fricción viscosa |
| **σ_s** | Tensor de esfuerzos del sólido | σ_s = λ_s (tr ε) I + 2μ_s ε: ley de Hooke |
| **I** | Matriz identidad | Hace que la presión empuje igual en x y en y |
| **μ_f** | Viscosidad dinámica del fluido | Qué tan "espeso" es el fluido. Valor: 1.0 |
| **ε(u)** | Tensor de velocidad de deformación | Cómo se deforma el fluido mientras se mueve |
| **ε(d)** | Tensor de deformaciones (lineal) | ε = ½(∇d + ∇dᵀ). Cambio de forma local del sólido |
| **ε_xx, ε_yy** | Componentes normales | Estiramiento o compresión en x y en y |
| **ε_xy** | Componente de cizalladura | Cambio de los ángulos rectos (distorsión) |
| **tr ε** | Traza de ε | ε_xx + ε_yy = ∇·d: cambio relativo de volumen |
| **σ_xx, σ_yy, σ_xy** | Componentes de σ_s | Esfuerzos normales y cortante |
| **λ_s** | Primer parámetro de Lamé | Resistencia a cambiar de volumen. Con tus datos ≈ 11.51 |
| **μ_s** | Segundo parámetro de Lamé (módulo de cizalla) | Resistencia a deformarse en ángulo. Con tus datos ≈ 8.33 |
| **E** | Módulo de Young | Rigidez del material. Valor: 21.5 |
| **ν** | Coeficiente de Poisson | Cuánto se adelgaza al estirarse. Valor: 0.29 |
| **f_v = f_s = (0, g)** | Fuerza volumétrica (peso propio) | Las dos letras son lo mismo: el peso de la viga |
| **g** | Gravedad (fuerza másica) | −0.05: hacia abajo |
| **U₀** | Velocidad de la pared izquierda | 1.0: la pared sube con esa velocidad |
| **∇·** | Divergencia | Cuánto "sale" de un punto. ∇·u = 0 → incompresible |
| **∇** | Gradiente | Derivadas en x y en y |
| **∂/∂x, ∂²/∂x²** | Derivadas parciales | Cómo cambia algo en la dirección x |
| **: (dos puntos)** | Producto doble de tensores | A:B = Σ A_ij B_ij: "multiplicar casilla por casilla y sumar" |
| **Re** | Número de Reynolds | Inercia frente a viscosidad. Stokes vale si Re ≪ 1 |

**Nota que te pueden preguntar:** en la tesis la ecuación de Stokes aparece en componentes como μ_f (∂²u/∂x² + ∂²u/∂y²), es decir, μ_f Δu, en vez de ∇·(2μ_f ε(u)). Son iguales porque ∇·(2μ ε(u)) = μΔu + μ∇(∇·u), y el último término es cero por incompresibilidad.

---

## 3. Interfaz y espacios funcionales

| Símbolo | Qué es | En palabras sencillas |
|---|---|---|
| **Γ_int** | Interfaz fluido-sólido | La cara de abajo de la viga = la tapa de la cavidad |
| **∂Ω** | Frontera de Ω | El borde del dominio |
| **x_ref, x_actual** | Posición de referencia y actual | Dónde estaba un punto y dónde está tras deformarse: x_actual = x_ref + d |
| **n_f, n_s** | Normales exteriores del fluido y del sólido | Flechas perpendiculares a la frontera, hacia afuera de cada dominio. n_f = −n_s |
| **t_f = σ_f n_f** | Tracción del fluido | La fuerza por unidad de longitud que el fluido hace sobre la interfaz |
| **t_s** | Tracción sobre el sólido | La carga que recibe la viga (Neumann) |
| **Γ_(f,D), Γ_(s,D)** | Fronteras de Dirichlet | Donde se impone el valor: paredes del fluido y extremos empotrados de la viga |
| **V_f** | Espacio de velocidades | Funciones H¹ que valen 0 en las paredes y en Γ_int |
| **Q_f** | Espacio de presiones | Funciones L² con media cero (solo para fijar la constante) |
| **V_s** | Espacio de desplazamientos | Funciones H¹ que valen 0 en los extremos empotrados |
| **[H¹(Ω)]²** | Funciones vectoriales con 2 componentes en H¹ | Una para x y otra para y |
| **v, q, w** | Funciones de prueba | Del fluido (v velocidad, q presión) y del sólido (w) |
| **Z, z** | Espacio y función de prueba global | Solo en la formulación monolítica: continuas a través de Γ_int |
| **∫_(Ω_f) q = 0** | Media nula | Fija la constante de la presión; la estabilidad la da inf-sup |

---

## 4. Algoritmo particionado y ALE

| Símbolo | Qué es | En palabras sencillas |
|---|---|---|
| **k** (superíndice) | Número de iteración | d^k es el desplazamiento en la vuelta k. ⚠ No es el grado del polinomio |
| **d̃^(k+1)** | Desplazamiento calculado por el sólido | Antes de relajar |
| **d_int^k** | Desplazamiento de la interfaz | En la iteración k |
| **ω** | Factor de relajación | 0.5: se mezcla mitad nuevo y mitad anterior. ω = 1 → sin relajación |
| **10⁻⁶** | Tolerancia | Se para cuando el cambio relativo es menor que eso |
| **α** (acoplamiento) | Intensidad de acoplamiento | 0.2: fracción de la tracción que se transmite. ⚠ No es la α de Céa |
| **Ω_f^0, Ω_s^0** | Configuración inicial (de referencia) | La geometría sin deformar |
| **d_malla** | Desplazamiento de los nodos de la malla del fluido | Se obtiene extendiendo d al interior con Laplace |
| **α_m** | Coeficiente de la extensión armónica | Constante; con datos de Dirichlet en todo el borde no cambia la solución. ⚠ Tercera α |
| **x⁰, x^(k+1)** | Posiciones de los nodos | Originales y en la iteración k+1: x^(k+1) = x⁰ + d_malla |
| **J_K** | Jacobiano del elemento K | Si J_K > 0 el triángulo está bien; si J_K ≤ 0 se volteó |
| **\|K\|** | Área del elemento K | Para la rigidez local 1/\|K\| (mejora futura) |
| **P₂/P₁ (Taylor-Hood)** | Velocidad cuadrática, presión lineal | Par estable: cumple inf-sup |
| **ρ_f, ρ_s** | Densidades del fluido y del sólido | Si ρ_f ≈ ρ_s aparece el efecto de masa añadida |

---

## 5. Variables del código (diapositiva de discretización)

| En el código | Significa | Símbolo matemático |
|---|---|---|
| `th`, `sh` | Malla del sólido y del fluido | 𝒯_h de Ω_s y de Ω_f |
| `dt1, dt2` | Desplazamiento calculado por el sólido (x, y) | d̃ |
| `d1, d2` | Desplazamiento ya relajado | d^(k+1) |
| `d1old` | Desplazamiento de la iteración anterior | d^k |
| `w, s` | Funciones de prueba del sólido (x, y) | w. ⚠ Aquí "s" no significa "sólido" |
| `lambda`, `mus` | Parámetros de Lamé | λ_s, μ_s |
| `gravity` | Fuerza másica | g |
| `coefalpha` | Intensidad de acoplamiento | α = 0.2 |
| `omega` | Relajación | ω = 0.5 |
| `s11r, s12r, s22r` | Componentes de σ_f tras la proyección L², en la malla de referencia | σ_xx, σ_xy, σ_yy del fluido |
| `N`, `N.x`, `N.y` | Normal exterior del dominio integrado y sus componentes | n_s |
| `bottombeam` | Etiqueta de la cara inferior de la viga | Γ_int |
| `on(2, 4, ...)` | Condición de Dirichlet en las etiquetas 2 y 4 | Extremos empotrados (Γ_(s,D)) |
| `int2d`, `int1d` | Integral en el área / en un borde | ∫_Ω, ∫_Γ |
| `epsilon`, `div` | Macros | ε (con 1/√2 en la cruzada) y ∇· |
| `solve` | Arma K y F y resuelve KU = F | — |

---

## 6. Resultados y convergencia

| Símbolo | Qué es | En palabras sencillas |
|---|---|---|
| **N** | Subdivisiones por lado | N = 10, 20, 40, 80; referencia N = 120 |
| **L** | Lado de la cavidad | 10 |
| **h/L = 1/N** | Tamaño relativo de malla | Se divide a la mitad de una malla a la siguiente |
| **u_ref** | Solución de referencia | La de la malla más fina (N = 120), que hace de "verdad" |
| **ℐ_N** | Operador de interpolación | Pasa u_ref a los nodos de la malla N para comparar |
| **E_N** | Error relativo en L² de la velocidad | ‖u_N − ℐ_N u_ref‖ / ‖ℐ_N u_ref‖ |
| **q** (orden) | Orden de convergencia experimental | q = log(E_anterior/E_actual) / log(h_anterior/h_actual). Tu resultado: q ≈ 1. ⚠ No es la q de presión |
| **O(h)** | "Del orden de h" | El error baja proporcional a h: si h se divide entre 2, el error también |
| **\|d_y\|** | Magnitud del desplazamiento vertical | Máximo ≈ 0.103 en x ≈ 6 |
| **r** | Distancia a la esquina | Cerca de las esquinas, p ~ 1/r: la presión crece sin límite |
| **H^½(∂Ω_f)** | Espacio de trazas | Donde deben vivir los datos de borde de una función H¹. Una función con un salto no está ahí |
| **Ghia et al. (1982)** | Referencia clásica de la cavidad impulsada | Para una validación externa futura |

---

## ⚠ Letras con más de un significado

| Letra | Significados | Cómo distinguirlos |
|---|---|---|
| **α** | (1) coercividad en Céa, (2) intensidad de acoplamiento = 0.2, (3) α_m del ALE | Por el contexto: teoría, caso de estudio o malla |
| **K** | (1) matriz de rigidez (negrita), (2) un elemento de la malla (J_K, \|K\|) | La matriz va en negrita; el elemento aparece como subíndice |
| **k** | (1) grado del polinomio, (2) número de iteración (superíndice) | El grado aparece en P_k y h^k; la iteración arriba: d^k |
| **q** | (1) función de prueba de la presión, (2) orden de convergencia | La de presión aparece en integrales; la del orden, en la tabla |
| **s** | (1) subíndice de "sólido" (σ_s, Ω_s), (2) función de prueba en el código | Solo en el código es una variable |
| **ε** | (1) tensor de deformaciones del sólido, (2) velocidad de deformación del fluido | ε(d) en el sólido, ε(u) en el fluido |
| **f_v / f_s** | La misma fuerza (peso propio) con dos nombres | Son lo mismo |
