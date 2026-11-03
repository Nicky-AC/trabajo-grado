# Hoja de repaso — sustentación

## Lo que NO puede faltar
1. **"El programa es una implementación propia"**, en el caso de estudio. La geometría y los parámetros vienen del ejemplo de FreeFEM.
2. **Simulación en vivo** (diapositiva 23): abrir *Simulacion*. Frase: *"El residuo mide cuánto cambia la interfaz entre iteraciones; baja de 10⁻⁶ en 21 iteraciones."*
3. **Orden 1 con su causa:** *"La teoría promete h³ si la solución es suave. En las esquinas la velocidad salta de 1 a 0, la solución no es suave, y por eso el error baja como h."*
4. **Conclusión:** *"La teoría justifica cada decisión: la forma débil → H¹; inf-sup → Taylor-Hood; Korn → solución única del sólido; la regularidad → el orden observado."*

## Frases clave
- **Galerkin:** *Busca la solución en un subespacio finito → KU = F. El error es ortogonal a ese subespacio → Céa: error acotado, **salvo una constante**, por la mejor aproximación. Si la solución es suave: **hᵏ en H¹ y hᵏ⁺¹ en L²** (Aubin-Nitsche).*
- **No linealidad:** *El dominio del fluido depende del desplazamiento de la viga.*
- **Interfaz:** *se mueve con la viga · no deslizamiento (u = 0) · las tracciones se equilibran.*
- **Particionado:** fluido recibe la **posición** (Dirichlet); viga recibe la **fuerza** (Neumann). ω = 0.5 → 21 iteraciones; con ω = 1 → 5 a 7.
- **ALE:** la **malla del fluido** sigue a la viga. Lagrangiano se enredaría; Euleriano no seguiría a la viga.
- **Malla válida:** *movemesh* da error si un triángulo se voltea, y el cociente mínimo de áreas es **0.945**.
- **Resultados:** el fluido empuja la viga **hacia arriba**, alivia el lado izquierdo; máximo **0.103 en x ≈ 6**.
- **Convergencia:** N = 10, 20, 40 y 80 contra referencia N = 120; error baja **como h** (órdenes 1.00, 1.02, 0.93). La deflexión cambia <1 % entre N = 80 y 120.

## Se me confunde → lo correcto
| No digas | Di |
|---|---|
| "baja a H1" | "baja **como h**" / "orden 1" |
| "las tracciones se anulan" | "se **equilibran**" |
| "no desplazamiento" | "no **deslizamiento**" |
| "ε = Euler, σ = omega" | **épsilon**, **sigma** |
| "gradiente del tensor" | **divergencia** (∇·) |
| "el código no tiene errores" | "no lo atribuyo a un error: la teoría explica esa tasa" |
| "porque quise" (Stokes) | "Re bajo, sin inercia, y me concentro en el acoplamiento" |
| "ALE garantiza..." | "el ALE **puede fallar** con deformaciones grandes" |
| viga 10 × 10 | viga **10 × 2** |
| "relajo el sólido" | relajo **el desplazamiento de la interfaz** |
| "Einstein" / "Kohn" | **Aitken** / **Korn** |

## Preguntas de jurado, en una línea
- **¿Qué es suyo?** Geometría y parámetros: del ejemplo. Mío: la fundamentación, el programa del esquema completo y el estudio de convergencia.
- **¿Por qué ω = 0.5?** Conservador; con ω = 1 también converge.
- **¿Por qué no medió la presión?** Es singular en las esquinas.
- **¿Por qué referencia propia?** No hay solución exacta conocida; es una verificación, no validación externa.
- **¿Por qué Taylor-Hood?** P₁/P₁ no cumple inf-sup (presión en tablero de ajedrez); P₂/P₁ sí.
- **¿α = 0.2?** Transmite el 20 % de la fuerza → deformación pequeña. α = 1 → trabajo futuro (hiperelasticidad).
- **¿Masa añadida?** Densidades parecidas → la inercia del fluido actúa como masa extra del sólido → inestabilidad. Aquí no hay inercia.
- **¿Demostró inf-sup o Lax-Milgram?** No: usé resultados conocidos para justificar las decisiones. Mi trabajo es descriptivo.

## Antes de entrar
Respira 4-4-6 (inhala 4, aguanta 4, exhala 6), cinco veces. Mira al jurado, una idea por diapositiva, sin leer.
