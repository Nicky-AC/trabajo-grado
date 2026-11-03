# Preguntas de práctica para la sustentación

## Del jurado
1. "La parte analítica no corresponde a la parte numérica." ¿Qué responde?

## Sobre la implementación y los resultados
2. ¿De dónde salen los números de la tabla de convergencia?
3. ¿Qué se toma del ejemplo de la documentación de FreeFEM y qué es suyo?
4. ¿Cómo se calcula la fuerza que el fluido ejerce sobre la viga? ¿Por qué proyección L² y no residuo variacional?
5. ¿Por qué se observa orden h si Taylor-Hood P₂/P₁ predice h³?
6. ¿Por qué la presión es tan grande en las esquinas de la pared que se mueve?
7. ¿Por qué el desplazamiento máximo de la viga está en x ≈ 6 y no en el centro?
8. ¿Por qué α = 0.2? ¿Qué cambia con α = 1?
9. ¿Por qué ω = 0.5 si sin relajación también converge?
10. ¿Cómo comprobó que ningún elemento de la malla se invierte?
11. ¿Cómo validó los resultados si no hay solución exacta?

## Sobre la teoría
12. ¿Qué dice el teorema de Lax-Milgram y por qué aplica aquí?
13. ¿Qué es la condición inf-sup y por qué importa en Stokes?
14. ¿Para qué sirve la desigualdad de Korn en el sólido?
15. ¿Qué dice el lema de Céa?
16. ¿Por qué el error en L² es un orden mayor que en H¹?
17. ¿Por qué una función con un salto no está en H^½ de la frontera, y qué consecuencia tiene?
18. ¿Qué es el efecto de masa añadida?
19. ¿Por qué un esquema particionado y no uno monolítico?
20. ¿Qué pasa si la malla ALE se invierte?
