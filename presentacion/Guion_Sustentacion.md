# Guion de la sustentación — 20 minutos

**Trabajo de grado:** Descripción y simulación de un modelo matemático para problemas acoplados fluido-estructura usando el método de los elementos finitos
**Sharon Nicole Acosta Caraballo** — Director: Humberto David Pérez González, PhD — Universidad de Cartagena

---

## Cómo usar este guion

Cada diapositiva tiene tres partes:

- **⏱ Tiempo:** cuánto dedicarle.
- **🗣 Qué decir:** el texto para practicar en voz alta. No tienes que decirlo palabra por palabra; es para que sepas qué idea va en cada diapositiva.
- **💡 Para entender:** la explicación de fondo. **Léela primero**, antes de practicar lo que vas a decir. Si entiendes esto, lo que dices te sale solo y aguantas las preguntas.

**Plan de estudio sugerido:**
1. **Día 1:** lee solo las partes 💡 de principio a fin, como si fuera un resumen de tu tesis.
2. **Día 2:** practica las partes 🗣 en voz alta, con la presentación abierta.
3. **Día 3 en adelante:** cronométrate. Meta: entre 19 y 20 minutos.

**Si vas corta de tiempo:** las diapositivas 9 a 12 (sólido y tensores) se pueden pasar rápido, en 15 a 20 segundos cada una. Son el detalle de cosas que ya dijiste en la 5.

---

## Mapa de tiempos

| Bloque | Diapositivas | Tiempo |
|---|---|---|
| Apertura y objetivos | 1–2 | 1:30 |
| Fundamentos del MEF | 3–4 | 1:45 |
| Modelo físico (fluido y sólido) | 5–12 | 4:00 |
| Acoplamiento y formulación | 13–19 | 5:00 |
| Implementación | 20–22 | 2:15 |
| Resultados y convergencia | 23–26 | 2:45 |
| Cierre | 27–31 | 1:50 |
| **Total** | | **≈ 19 min** |

---

## 1. Portada
⏱ 30 s

🗣 *"Buenos días. Mi nombre es Sharon Nicole Acosta Caraballo y voy a presentar mi trabajo de grado, titulado 'Descripción y simulación de un modelo matemático para problemas acoplados fluido-estructura usando el método de los elementos finitos', dirigido por el profesor Humberto Pérez González."*

💡 Respira antes de empezar. La primera frase marca el ritmo de toda la presentación: dila despacio.

---

## 2. Objetivos
⏱ 1 min

🗣 *"El objetivo general fue describir un modelo matemático para problemas acoplados fluido-estructura usando el método de los elementos finitos y el software FreeFEM++. Para lograrlo me propuse cuatro objetivos específicos: primero, explicar los fundamentos del método de elementos finitos, desde la formulación débil hasta su implementación; segundo, formular las ecuaciones del fluido y de la estructura; tercero, describir cómo se acoplan en la interfaz y presentar la forma débil del problema; y cuarto, implementar el modelo en FreeFEM++."*

💡 Estos son **exactamente** los objetivos de tu propuesta aprobada. Fíjate en que la presentación sigue ese mismo orden: teoría del MEF → ecuaciones → acoplamiento → implementación. Si te preguntan "¿cumpliste los objetivos?", la respuesta es recorrer esa lista.

Tu trabajo es **descriptivo**: el objetivo no era inventar un método nuevo, sino entender, explicar e implementar uno conocido. Así lo aclaraste también en la corrección de la propuesta.

---

## 3. Introducción al Método de Elementos Finitos
⏱ 45 s

🗣 *"El método de los elementos finitos es una técnica numérica para aproximar soluciones de ecuaciones en derivadas parciales en dominios complejos. Se basa en tres ideas: primero, la formulación débil, que transforma la ecuación en una forma integral; segundo, la discretización del dominio en una malla de elementos; y tercero, la aproximación con funciones polinómicas a trozos, que convierte el problema en un sistema de ecuaciones algebraicas que se puede resolver en el computador. (Segunda página:) Aquí se ve una malla: el dominio se divide en triángulos que solo comparten vértices o lados completos, y a la derecha, un elemento triangular con sus tres vértices."*

💡 **La idea del MEF en una frase:** no puedes resolver la ecuación exactamente, así que partes el dominio en triángulos pequeños, supones que en cada uno la solución es un polinomio sencillo y buscas los coeficientes de esos polinomios. Eso se convierte en un sistema lineal **KU = F**.

- **Formulación débil:** en lugar de exigir que la ecuación se cumpla punto por punto, se exige que se cumpla "en promedio" contra muchas funciones de prueba. Así se necesitan menos derivadas.
- **Malla 𝒯ₕ (la figura nueva, que pidió tu tutor):** el conjunto de triángulos. "Sin nodos colgantes" quiere decir que ningún vértice de un triángulo cae en la mitad del lado de otro. La letra **h** es el tamaño de los triángulos: entre más pequeño h, más fina la malla.
- **Galerkin:** usar el mismo espacio de polinomios para la solución y para las funciones de prueba.

---

## 4. Galerkin y estimaciones de error
⏱ 1 min

🗣 *"El método de Galerkin busca la solución aproximada uₕ en un subespacio de dimensión finita Vₕ, lo que lleva al sistema KU = F. Una propiedad clave es la ortogonalidad del error, y de ella se deduce el lema de Céa: el error de Galerkin está acotado por la mejor aproximación posible dentro del subespacio. Con esto, para elementos de grado k y una solución suficientemente regular, el error en norma H¹ es de orden hᵏ y, por el argumento de dualidad de Aubin-Nitsche, en norma L² es de orden hᵏ⁺¹. Esta teoría es la referencia para interpretar el estudio de convergencia que muestro al final."*

💡 Esta diapositiva es la base matemática de los resultados.

- **Lax-Milgram:** si la forma bilineal *a* es **continua** (no crece demasiado) y **coerciva** (a(v,v) ≥ α‖v‖², es decir, "empuja hacia arriba"), entonces la solución débil **existe y es única**.
- **Ortogonalidad de Galerkin:** a(u − uₕ, vₕ) = 0. El error es "perpendicular" al subespacio.
- **Lema de Céa:** ‖u − uₕ‖ ≤ (M/α)·inf ‖u − vₕ‖. En palabras: Galerkin es casi tan bueno como la mejor aproximación posible con esos polinomios. Así, estimar el error se reduce a estimar qué tan bien aproximan los polinomios.
- **Órdenes de convergencia:**
  - con polinomios de grado k, el error en la derivada (norma H¹) baja como hᵏ;
  - el error en la función (norma L²) baja una potencia más rápido, como hᵏ⁺¹. Eso se demuestra con **Aubin-Nitsche**, un truco de dualidad: se resuelve un problema auxiliar "al revés" y se usa su regularidad.
  - **Ejemplo:** P₁ (lineales) da L² ~ h²; P₂ (cuadráticos) da L² ~ h³.
- **Importante:** estos órdenes exigen que la solución sea **suficientemente regular** (suave). Esa condición es la clave de la diapositiva 26.

---

## 5. El Problema Fuerte: Sistema Acoplado
⏱ 45 s

🗣 *"El problema consiste en encontrar la terna (u, p, d): la velocidad y la presión del fluido, y el desplazamiento de la estructura. El fluido se modela con las ecuaciones de Stokes en el dominio deformado Ω_f(d), y el sólido con las ecuaciones de elasticidad lineal en Ω_s. Desde ya aparece la dificultad principal: el dominio del fluido depende del desplazamiento del sólido."*

💡 **Las incógnitas:**
- **u** = velocidad del fluido (vector);
- **p** = presión (escalar);
- **d** = desplazamiento del sólido (vector: cuánto se mueve cada punto de la viga).

**Stokes** es la versión "lenta" de Navier-Stokes: fluido muy viscoso, sin inercia. **Elasticidad lineal** quiere decir que el sólido se deforma poco y la relación entre fuerza y deformación es lineal, como un resorte.

---

## 6. Subsistema del Fluido (Stokes) — el tensor de esfuerzos
⏱ 40 s

🗣 *"El estado de fuerzas internas del fluido se describe con el tensor de esfuerzos σ_f, que tiene dos partes: la presión, que actúa de forma normal y por igual en todas las direcciones, y la parte viscosa, que genera tanto tensiones normales como tangenciales, es decir, la fricción entre capas de fluido."*

💡 **σ_f = −pI + 2μ_f ε(u)**
- **−pI:** la presión solo empuja perpendicular a las superficies. Por eso es diagonal.
- **2μ_f ε(u):** la viscosidad (μ_f) resiste que el fluido se deforme. **ε(u)** es la parte simétrica del gradiente de velocidad (la "tasa de deformación").
- Los términos fuera de la diagonal son el **cortante**: la fricción entre capas.

---

## 7. Subsistema de Stokes en 2D
⏱ 35 s

🗣 *"La ecuación de momento, menos la divergencia de σ_f igual a cero, dice que la presión se equilibra exactamente con la fricción viscosa: no hay inercia, porque el número de Reynolds es muy bajo. La ecuación de continuidad, divergencia de u igual a cero, dice que el fluido es incompresible: su volumen se conserva."*

💡
- **Momento:** −∇·σ_f = 0. Lo que empuja (presión) = lo que frena (viscosidad).
- **Continuidad:** ∇·u = 0. Si el fluido se aprieta por un lado, se expande por el otro.
- **Por qué no hay inercia:** Stokes vale cuando Re ≪ 1: fluido muy viscoso o muy lento. Por eso no aparece el término (u·∇)u de Navier-Stokes.
- **Si te preguntan por la forma en componentes:** −∇p + μ_f Δu = 0. Es lo mismo, porque ∇·(2μ_f ε(u)) = μ_f Δu + μ_f ∇(∇·u), y el último término es cero por incompresibilidad.

---

## 8. El Verdadero Reto: No-linealidad Geométrica
⏱ 35 s

🗣 *"Aunque las ecuaciones de Stokes y de elasticidad son lineales, el problema acoplado no lo es: las derivadas del fluido se calculan sobre Ω_f(d), un dominio que depende del desplazamiento. El fluido deforma al sólido, y el sólido cambia el espacio donde se mueve el fluido."*

💡 Esta es **la idea central de la tesis**. Cada ecuación por separado es lineal, pero el **dominio** del fluido es una incógnita. A eso se le llama **problema de frontera libre** y obliga a iterar: resuelves, mueves el dominio, vuelves a resolver.

---

## 9. Subsistema de la estructura (Elasticidad lineal)
⏱ 25 s

🗣 *"Para el sólido sigo tres pasos: la cinemática, que lleva del desplazamiento al tensor de deformaciones; la ley constitutiva de Hooke, que lleva de las deformaciones a los esfuerzos; y el equilibrio, que da las ecuaciones de Navier-Lamé."*

💡 La cadena es **d → ε (cuánto se deforma) → σ (qué fuerzas internas aparecen) → equilibrio**. Las diapositivas 10 a 12 desarrollan cada paso.

---

## 10. Deformaciones y esfuerzos
⏱ 40 s

🗣 *"El tensor de deformaciones mide el cambio de forma de cada punto: la diagonal mide estiramientos o compresiones a lo largo de los ejes, y la componente cruzada, la cizalladura, es decir, el cambio de los ángulos rectos. Los esfuerzos se obtienen con la ley de Hooke: el esfuerzo es proporcional a la deformación, y la traza de ε representa el cambio de volumen."*

💡
- **ε(d) = ½(∇d + ∇dᵀ).** 🧠 Imagina un cuadradito dibujado en la viga: si se estira o se aplasta, se vuelve **rectángulo** (ε_xx, ε_yy); si se tuerce, se vuelve **rombo** (ε_xy, cizalladura), como un mazo de cartas empujado de lado.
- Es "lineal" porque desprecia términos cuadráticos: solo vale para **deformaciones pequeñas**, que es la hipótesis de tu modelo.
- **σ_s = λ_s (tr ε) I + 2μ_s ε:** las fuerzas internas. λ_s responde al cambio de **volumen** y μ_s al cambio de **forma**. Material **isótropo**: responde igual en todas las direcciones.
- **tr ε = ∇·d:** cuánto cambia el volumen (en 2D, el área).

---

## 11. Interpretación física de los parámetros
⏱ 25 s

🗣 *"Los coeficientes de Lamé definen la respuesta elástica: λ_s está relacionado con la resistencia a cambios de volumen y μ_s, el módulo de rigidez, con la resistencia al cizallamiento."*

💡 En la simulación no se dan λ y μ directamente, sino **E = 21.5** (módulo de Young, rigidez) y **ν = 0.29** (coeficiente de Poisson). De ahí se calculan:
**μ = E / (2(1+ν))** y **λ = Eν / ((1+ν)(1−2ν))**.

---

## 12. Ecuaciones de Navier-Lamé
⏱ 30 s

🗣 *"El equilibrio del sólido lo dan las ecuaciones de Navier-Lamé: la divergencia de los esfuerzos equilibra la fuerza de volumen, que aquí es el peso propio de la viga, con g negativo porque apunta hacia abajo."*

💡 **∇· es divergencia, no gradiente.** **f_v = (0, g)** con **g = −0.05**: el peso propio de la viga. El signo negativo quiere decir "hacia abajo". Este signo se corrigió en la tesis para que coincidiera con el código.

---

## 13. Condiciones en la Interfaz (Γ_int)
⏱ 50 s

🗣 *"La interacción ocurre en la interfaz común Γ_int, y la gobiernan tres condiciones. La primera es la compatibilidad geométrica: la interfaz se mueve con el desplazamiento del sólido. La segunda es la condición cinemática de no deslizamiento: como el problema es estacionario, la estructura está en reposo y el fluido tiene velocidad cero sobre la interfaz. La tercera es el equilibrio dinámico, la acción y reacción: las tracciones del fluido y del sólido se cancelan, σ_f n_f + σ_s n_s = 0."*

💡 Esta diapositiva es **muy preguntable**.
- **Compatibilidad geométrica:** x_actual = x_ref + d. El fluido y el sólido no se separan ni se superponen.
- **Cinemática:** en general, la velocidad del fluido en la interfaz es igual a la del sólido (u = ∂d/∂t). En estado estacionario nada se mueve, así que **u = 0**. Esta fue la **observación 1 del jurado**: en la interfaz NO se impone ninguna velocidad; el fluido lo mueve la **pared izquierda**.
- **Dinámica:** la fuerza que el fluido hace sobre el sólido es igual y opuesta a la que el sólido hace sobre el fluido. Es la tercera ley de Newton.

---

## 14. Geometría y Normales
⏱ 20 s

🗣 *"Cada dominio tiene su normal exterior, y sobre la interfaz se cumple n_f = −n_s. Fijé esta convención una sola vez y la respeto en todo el trabajo, incluido el código."*

💡 La normal exterior del fluido apunta hacia el sólido y la del sólido apunta hacia el fluido: son opuestas. Esta convención fue la **observación 3 del jurado** (el signo de la fuerza). Fijarla una vez evita errores de signo.

---

## 15. Espacios Funcionales
⏱ 50 s

🗣 *"Para la forma variacional defino los espacios de Sobolev. Para el fluido, V_f son las velocidades de H¹ que se anulan en las fronteras de Dirichlet y también en la interfaz, porque en el esquema particionado la velocidad ahí es un dato impuesto. Q_f son las presiones, en L². Para el sólido, V_s son los desplazamientos de H¹ que se anulan donde la viga está empotrada."*

💡
- **H¹** = funciones que, junto con sus primeras derivadas, son de cuadrado integrable. Es el espacio natural cuando aparecen derivadas de primer orden.
- **¿Por qué v = 0 en Γ_int?** En el esquema que programaste, la velocidad del fluido en la interfaz **se impone** (u = 0). Donde se impone un valor, la función de prueba vale cero.
- **¿Por qué media nula en la presión?** En una cavidad cerrada, la presión solo aparece como gradiente (∇p), así que p y p + 5 dan el mismo resultado. Exigir ∫p = 0 elimina esa constante y la presión queda única. 🧠 Como escoger el nivel del mar para medir alturas. **No tiene nada que ver con estabilidad** (eso lo da inf-sup); fue una observación del jurado, así que **ten lista la frase**: *"La media cero solo escoge una presión entre todas las posibles, porque la presión está definida a menos de una constante; la estabilidad la da inf-sup."*
- **Inf-sup / LBB:** Stokes **no es coercivo** (la presión no aparece "al cuadrado"), así que Lax-Milgram no aplica. Se usa la teoría de **Babuška-Brezzi**, que exige que velocidad y presión sean "compatibles": el espacio de velocidades debe ser lo bastante rico para controlar la presión.
- **Korn:** para el sólido sí aplica Lax-Milgram, gracias a la desigualdad de Korn: controlar ε(w) controla todo ‖w‖_H¹, si la viga está fija en alguna parte.

---

## 16. Formulación Variacional (Forma Débil)
⏱ 50 s

🗣 *"Multiplicando por las funciones de prueba e integrando por partes obtengo las formas débiles. Para el fluido, como las funciones de prueba se anulan en la interfaz, la integral de tracción es cero: la ecuación del fluido queda igualada a cero. La tracción no desaparece del modelo; se recupera después de resolver el fluido y se transfiere al sólido como condición de Neumann, que es el término de frontera de la ecuación del sólido."*

💡 Esta fue la **observación 2 del jurado** y conviene que la entiendas bien.
- Al integrar por partes aparece una integral sobre la frontera: ∫ (σn)·v.
- Si v = 0 en la interfaz, esa integral **vale cero**. Por eso no tenía sentido dejarla escrita en la ecuación del fluido.
- **Dirichlet** = imponer el valor (velocidad). **Neumann** = imponer la fuerza (tracción).
- En tu esquema: **el fluido recibe Dirichlet y el sólido recibe Neumann**. De ahí el nombre **Dirichlet-Neumann**.

---

## 17. El Acoplamiento Global
⏱ 50 s

🗣 *"Si en cambio se plantea el problema de forma monolítica, se usa un único espacio de prueba global Z, de funciones de H¹ en todo el dominio que se anulan en las fronteras de Dirichlet. Estas funciones son continuas a través de la interfaz, pero libres sobre ella. Tomando v = w = z y usando acción y reacción, los términos de frontera de la interfaz se cancelan: el trabajo virtual total de las fuerzas de interacción es nulo. Este es el fundamento de la formulación monolítica; el esquema que implementé es el particionado."*

💡 Esta fue la **observación manuscrita del segundo jurado (página 40)**.
- **El problema original:** si v = 0 en la interfaz, decir "v = w en la interfaz" era vacío (0 = 0).
- **La solución:** usar **Z ⊂ [H¹(Ω)]²** en todo el dominio. Estar en H¹ de todo Ω obliga a que la función sea **continua** al cruzar la interfaz, pero no la obliga a valer cero ahí. Así la cancelación tiene contenido.
- **Monolítico vs. particionado:**
  - **Monolítico:** resolver fluido y sólido juntos en un solo sistema gigante.
  - **Particionado:** resolver cada uno por separado e intercambiar información.
  - En la tesis **presentas** el monolítico como teoría, pero **implementas** el particionado.

---

## 18. Estrategia de Solución: Método Particionado
⏱ 50 s

🗣 *"Como el sistema monolítico es costoso y mal condicionado, usé el algoritmo de Dirichlet-Neumann. En cada iteración: resuelvo el fluido en la malla actual; calculo la tracción del fluido proyectando en L² el tensor de esfuerzos; resuelvo el sólido con esa carga como condición de Neumann; relajo el desplazamiento con un factor ω = 0.5 constante; actualizo la malla del fluido; y repito hasta que el cambio relativo del desplazamiento en la interfaz sea menor que 10⁻⁶. Con ω = 0.5 converge en 21 iteraciones; sin relajación también converge, en 5 a 7, porque en este caso el acoplamiento es débil."*

💡
- **¿Por qué relajar?** En general, si aplicas directamente el desplazamiento nuevo, la iteración puede oscilar o diverger. Con ω = 0.5 das "medio paso": d_nuevo = 0.5·d_calculado + 0.5·d_anterior.
- **En tu caso no hacía falta:** se probó que sin relajación (ω = 1) también converge, y hacia la misma solución. ω = 0.5 es una elección **conservadora**, no una condición necesaria. No digas que "garantiza" la convergencia.
- Es **relajación constante**, no dinámica. La relajación **de Aitken** (que ajusta ω en cada paso) queda como trabajo futuro. El jurado pidió no llamarla "dinámica".
- **¿Cómo se calcula la fuerza?** Con la **proyección L²** del tensor σ_f: el tensor sale de derivar la velocidad y es discontinuo entre elementos; la proyección lo vuelve continuo antes de evaluarlo en la interfaz. **No digas "residuo variacional":** esa es una alternativa más precisa que no se implementó y está en la tesis como trabajo futuro.
- **Masa añadida:** cuando el fluido es tan denso como el sólido, este esquema se vuelve inestable. En tu caso estacionario y viscoso no es un problema, pero es una limitación conocida.

---

## 19. Flujo del Algoritmo
⏱ 30 s

🗣 *"Este diagrama resume el ciclo: parto de la configuración inicial, resuelvo el fluido, calculo la tracción, resuelvo el sólido, relajo, y si no ha convergido muevo la malla y vuelvo a empezar."*

💡 Señala el diagrama con el dedo o el puntero mientras hablas. Es la misma lista de la diapositiva anterior, pero en dibujo.

---

## 20. Caso de estudio: cavidad con tapa elástica
⏱ 50 s

🗣 *"Como caso de estudio tomé la geometría y los parámetros del ejemplo de problema acoplado de la documentación oficial de FreeFEM++. Sobre ese caso escribí mi propia implementación del esquema del capítulo 2, que está completa en el Anexo A. Es una cavidad cuadrada de 10 × 10 llena de fluido viscoso, cuya tapa superior es una viga elástica de 10 × 2, empotrada en sus extremos. El fluido se mueve porque la pared izquierda tiene una velocidad tangencial hacia arriba; en las demás paredes y en la interfaz la velocidad es cero. La tabla muestra los parámetros. El factor α = 0.2 indica que solo se transmite una fracción de la tracción, lo que corresponde a un régimen de acoplamiento débil."*

💡 **Decir de dónde viene el caso es importante y te protege.** Del ejemplo de FreeFEM se toman **solo la geometría y los parámetros**. El programa y todas las figuras de resultados son **tuyos**.
- **"Cavidad impulsada" (driven cavity):** es un problema clásico de la mecánica de fluidos. Normalmente se mueve la tapa; aquí se mueve **la pared izquierda** y la tapa es elástica.
- **α = 0.2:** el código multiplica la fuerza del fluido por 0.2. Al reducir la carga, la viga se deforma poco y la elasticidad lineal sigue siendo válida. El caso α = 1 **no se analizó**; queda como trabajo futuro.
- **Parámetros:** E = 21.5, ν = 0.29, g = −0.05, μ_f = 1, U₀ = 1. Son **adimensionales** (sin unidades físicas).

---

## 21. Discretización y transferencia de carga
⏱ 45 s

🗣 *"Para el fluido usé el par de Taylor-Hood P₂/P₁: velocidad cuadrática y presión lineal, un par estable que cumple la condición inf-sup. Para el sólido, elementos P₁ vectoriales. En el código, la carga del fluido se integra sobre la frontera inferior de la viga, que es la interfaz. El vector N de FreeFEM++ es la normal exterior del sólido, de modo que la carga es σ_f n_s; el signo menos solo refleja que en el comando solve todos los términos se escriben del lado izquierdo, igual que el peso propio. La última línea es la relajación."*

💡
- **¿Por qué no P₁/P₁?** Ese par **no** cumple inf-sup y produce presiones con oscilaciones falsas ("modos espurios"). P₂/P₁ sí es estable.
- **El signo menos:** FreeFEM escribe todo como "... = 0". Lo que en la ecuación va a la derecha pasa a la izquierda con signo cambiado. Por eso aparece "−coefalpha·(...)", igual que "−gravity·s". **No** invierte la fuerza. Fue la **observación 3 del jurado**.
- **`s11r`, `s12r`, `s22r`:** son las componentes del tensor del fluido después de la proyección L², trasladadas a la malla de referencia.
- **`bottombeam`:** es la etiqueta del código para la cara inferior de la viga, o sea, Γ_int.
- **El factor 1/√2** en la macro epsilon hace que el producto en el código dé exactamente ε:ε. Se corrigió en la tesis.

---

## 22. Movimiento de malla: técnica ALE
⏱ 40 s

🗣 *"Para mover la malla del fluido usé la técnica ALE, que significa Arbitraria Lagrangiana-Euleriana: la malla no sigue a las partículas del fluido ni se queda quieta, sino que se mueve como convenga. El desplazamiento de la interfaz se extiende al interior del dominio resolviendo una ecuación de Laplace con coeficiente constante, la extensión armónica, y con la malla fija en las paredes rígidas. Así los nodos internos se redistribuyen suavemente."*

💡
- **Lagrangiano** = la malla viaja con el material. **Euleriano** = la malla está quieta y el material pasa. **ALE** = la malla se mueve "como convenga", ni una cosa ni la otra.
- **¿Por qué Laplace?** Porque sus soluciones son suaves: si mueves el borde, el interior se acomoda sin arrugarse.
- **Coeficiente constante:** fue la **observación 4 del jurado**. El código usaba el área **total**, no el área de cada elemento, así que era una constante. La rigidez local 1/|K| queda como mejora futura.
- **J_K > 0:** el jacobiano de cada triángulo debe ser positivo; si se vuelve negativo, el triángulo se "voltea" y la malla deja de servir.

---

## 23. Campos de velocidad y presión
⏱ 40 s (+ 1 min de ejecución en vivo)

▶ **Ejecución en vivo (lo pidió tu tutor):** antes de explicar esta diapositiva, abre **Simulacion** desde el escritorio.
- 🗣 *"Ahora ejecuto el programa: en la consola se ve cómo baja el residuo en cada iteración del acoplamiento, hasta converger en 21 iteraciones."*
- Tarda unos 25 segundos. Luego aparecen las gráficas de FreeFEM (malla deformada → presión y velocidad → desplazamiento de la viga); presiona **ENTER** para pasar de una a otra. Después se abren las **figuras de Python**, iguales a las de la presentación; ciérralas para terminar.
- Al terminar, vuelve a la presentación y explica con la figura de la diapositiva.


🗣 *"La pared izquierda sube y arrastra el fluido, que gira bajo la viga y forma una recirculación concentrada en la mitad izquierda de la cavidad. La presión es positiva en la mitad de arriba y negativa en la de abajo. Los valores extremos están en las dos esquinas de la pared que se mueve: ahí la velocidad impuesta salta de golpe a cero y la presión es singular. Estas figuras son de mi simulación, con la malla N = 40."*

💡
- **Recirculación:** la pared izquierda sube, arrastra el fluido, el fluido gira. En la mitad derecha casi no hay movimiento.
- **Singularidad en las esquinas:** en la esquina, la pared que se mueve toca una pared quieta; la velocidad "salta" de U₀ a 0 y la presión se dispara (≈ 121 en la esquina de arriba con N = 40). Esto **reduce la regularidad** de la solución y es la clave de la diapositiva 26.
- **Escala recortada al percentil 98 (solo si te preguntan):** 🧠 como una foto con el sol de frente. En las esquinas la presión llega a ≈ 121 y en el resto está entre −1.7 y 1.7; si la escala llegara a 121, toda la figura saldría de un solo color.
- **Ya no digas** "fuerza hacia abajo por succión": cerca de la viga la presión es **positiva** y la empuja **hacia arriba**.

---

## 24. Respuesta estructural y malla deformada
⏱ 40 s

🗣 *"La presión del fluido empuja la viga hacia arriba, en contra de su peso, y como es mayor cerca de la pared que se mueve, alivia el lado izquierdo. Por eso la elástica es asimétrica: el desplazamiento máximo, de 0,103, está en x ≈ 6 y no en el centro. Junto a la esquina hay una deformación local producida por la singularidad. En la malla deformada comprobé numéricamente que ningún triángulo se invierte: el cociente mínimo entre el área deformada y la original es 0,945."*

💡
- **Viga cargada solo por su peso:** tendría el máximo justo en el centro (x = 5). El fluido rompe esa simetría.
- **Deformación local junto a la esquina:** se queda siempre en el primer elemento y se acerca a la esquina al refinar la malla (x = 0,25 con N = 40; x ≈ 0,08 con N = 120). Es un efecto de la singularidad, no de la viga.
- **Amplificación ×5:** en la figura los desplazamientos se dibujan 5 veces más grandes para que se vean. El real es ≈ 5 % del espesor: pequeñas deformaciones, como exige la elasticidad lineal.
- **J_K > 0 comprobado:** ya no es "solo visual". Se calculó el área con signo de cada triángulo y se comparó con la original; el mínimo es 0,945, así que ninguno se volteó.

---

## 25. Estudio de convergencia de malla
⏱ 50 s

🗣 *"Para verificar la consistencia numérica hice un estudio de convergencia de malla. Tomé como referencia una solución muy refinada, con N = 120, y calculé el error relativo de la velocidad en norma L² para N = 10, 20, 40 y 80. El orden experimental q se calcula comparando mallas sucesivas. Al dividir h a la mitad, el error se reduce aproximadamente a la mitad, y los órdenes estimados son 1,00, 1,02 y 0,93. Los resultados evidencian una tasa de convergencia experimental aproximadamente lineal. La deflexión máxima de la viga se estabiliza: cambia menos del 1 % entre N = 80 y la referencia."*

💡
- **¿Por qué una solución de referencia?** Este problema no tiene solución exacta conocida, así que la malla muy fina hace de "verdad".
- **El orden q:** q = log(E_anterior / E_actual) / log(h_anterior / h_actual). Si el error se divide entre 2 cuando h se divide entre 2: log 2 / log 2 = **1**.
- **El 0,93 del final** se lee con cautela: N = 80 está relativamente cerca de la referencia N = 120.
- **h/L:** tamaño de malla relativo al lado de la cavidad (L = 10); h/L = 1/N. Los órdenes no cambian con esa normalización.
- **Cuidado con la palabra:** "evidencian", **no** "demuestran". Una tabla de errores no es una demostración. Fue la **observación 5 del jurado**.
- **Limitación honesta:** es una verificación contra una solución propia, no una validación contra datos externos (por ejemplo Ghia et al., 1982). Si te preguntan, lo reconoces y lo propones como trabajo futuro.

---

## 26. ¿Por qué orden 1 y no 3?
⏱ 35 s

🗣 *"La teoría dice que, con elementos P₂, el error podría bajar como h al cubo, pero solo si la solución es muy suave. En mi caso no lo es: en las esquinas, la pared que sube toca paredes quietas, y la velocidad salta de golpe de 1 a 0. Ese salto le quita suavidad a la solución, y por eso el error baja solo como h. Es decir, la teoría explica mi resultado."*

💡 **Esta pregunta te la van a hacer casi seguro, y es tu respuesta al jurado** que dijo que lo analítico no corresponde a lo numérico. Ahora sí corresponden: el capítulo 1 dice que el orden óptimo exige regularidad; el caso no la tiene, y la simulación lo muestra.
- **Recuerda la diapositiva 4:** el orden hᵏ⁺¹ exige que u ∈ H^(k+1). Si la solución es menos suave (por las esquinas), el orden baja, sin importar lo bueno que sea el polinomio.
- **Solo si te piden más detalle:**
  - Los datos de frontera de una solución en H¹ deben estar en **H^½**. Una función con un salto no está ahí: es el caso clásico de la cavidad impulsada, donde la presión crece como **1/r** cerca de las esquinas.
  - En la malla, el salto se reparte en un solo triángulo y solo se resuelve al ritmo con que se refina la malla.
- **Palabras clave:** "interpretación numérica", "parece estar gobernada por". **Nunca** digas "se demuestra que".
- **Si preguntan cómo recuperar el orden:** regularizar la velocidad de la pared para que se anule en las esquinas, o refinar la malla cerca de ellas. Quedó como trabajo futuro.
- **Trampa frecuente:** "¿no será por el P₁ del sólido?". Respuesta: no directamente, porque el error que se mide es el de la velocidad del fluido, que es P₂.

---

## 27. Alcances y limitaciones
⏱ 35 s

🗣 *"El modelo tiene límites claros. Stokes solo vale para números de Reynolds muy bajos; la elasticidad lineal, para pequeñas deformaciones; el caso es estacionario, así que no captura vibraciones; y α = 0.2 corresponde a un acoplamiento débil. En lo numérico, el esquema particionado es sensible al efecto de masa añadida, el ALE puede fallar con deformaciones grandes, y la convergencia se midió contra una referencia propia, con una tasa limitada por la regularidad del caso."*

💡 **Mostrar las limitaciones tú misma suma puntos.** Un jurado confía más en quien conoce los límites de su trabajo. Recuerda que es un trabajo de pregrado y descriptivo: estos límites son normales y esperados.

---

## 28. Conclusiones
⏱ 40 s

🗣 *"Como conclusiones: el esquema particionado Dirichlet-Neumann con relajación permitió acoplar Stokes y elasticidad lineal en régimen estacionario. El par Taylor-Hood garantiza la estabilidad de la presión, aunque por sí solo no garantiza la precisión de las tracciones en la interfaz. La extensión armónica preservó la calidad de la malla en el rango de deflexiones considerado. Los resultados evidencian una convergencia aproximadamente lineal, explicada por la falta de regularidad del caso. Y, sobre todo, el trabajo muestra cómo el análisis funcional (los espacios de Sobolev, Lax-Milgram, la condición inf-sup y Korn) sustenta cada decisión de la implementación, y explica incluso la tasa de convergencia observada."*

💡 La última conclusión es tu **mensaje como matemática**: no solo corriste un programa, entendiste **por qué** funciona y **por qué** converge como converge. Dila con convicción.

---

## 29. Trabajo futuro
⏱ 25 s

🗣 *"Como trabajo futuro propongo: pasar a Navier-Stokes, estudiar el problema dinámico en el tiempo, usar modelos hiperelásticos para grandes deformaciones y el caso α = 1, acelerar el acoplamiento con relajación de Aitken o métodos cuasi-Newton, regularizar el dato de la pared para recuperar el orden óptimo, calcular la carga con el residuo variacional, y hacer una validación cuantitativa externa."*

💡 Cada punto de trabajo futuro responde a una limitación de la diapositiva 27 o de la 26. Si te preguntan "¿qué harías distinto?", sale de aquí.

---

## 30. Referencias principales
⏱ 5 s

🗣 *"Estas son las referencias principales del trabajo."*

💡 No la leas: solo muéstrala y pasa a la siguiente.

---

## 31. ¡Gracias! — Preguntas
⏱ 5 s

🗣 *"Muchas gracias por su atención. Quedo atenta a sus preguntas."*

💡 Sonríe, toma agua y respira. Ya pasó lo más largo.

---

## Mini glosario para repasar

| Término | En una línea |
|---|---|
| **FSI** | Interacción fluido-estructura: el fluido deforma al sólido y el sólido cambia el dominio del fluido. |
| **Stokes** | Fluido viscoso, lento e incompresible, sin inercia (Re ≪ 1). |
| **Elasticidad lineal** | Sólido con pequeñas deformaciones; fuerza proporcional a deformación (Hooke). |
| **Forma débil** | La ecuación multiplicada por funciones de prueba e integrada; pide menos derivadas. |
| **H¹** | Funciones con primeras derivadas de cuadrado integrable. |
| **Lax-Milgram** | Continuidad + coercividad ⇒ existe una única solución. |
| **Lema de Céa** | El error de Galerkin es comparable al de la mejor aproximación posible. |
| **Aubin-Nitsche** | Argumento de dualidad que da un orden más en L² que en H¹. |
| **Inf-sup / LBB** | Condición de compatibilidad entre velocidad y presión; da la estabilidad de Stokes. |
| **Taylor-Hood P₂/P₁** | Velocidad cuadrática y presión lineal: par estable. |
| **Korn** | Controlar ε(w) controla todo el desplazamiento; da coercividad al sólido. |
| **Dirichlet / Neumann** | Imponer el valor / imponer la fuerza (flujo). |
| **Particionado / monolítico** | Resolver cada física por separado e iterar / todo junto en un sistema. |
| **Relajación ω** | Mezclar el desplazamiento nuevo con el anterior para que la iteración no oscile. |
| **Masa añadida** | Inestabilidad del esquema particionado cuando ρ_fluido ≈ ρ_sólido. |
| **ALE** | Malla que se mueve libremente, ni pegada al material ni quieta. |
| **Jacobiano J_K** | Mide si un triángulo se deformó bien; si J_K ≤ 0, el triángulo se volteó. |
| **Orden de convergencia** | Exponente q con el que el error baja: error ~ h^q. En tu caso q ≈ 1. |
| **Singularidad de esquina** | Donde el dato de Dirichlet salta (pared que se mueve contra pared quieta); la presión crece como 1/r y la solución pierde regularidad. |
| **Proyección L²** | Volver continuo un campo discontinuo (como σ_f) buscando el más cercano en norma L². |
