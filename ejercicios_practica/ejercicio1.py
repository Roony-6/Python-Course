#a) DIferencia en porcentaje de lo que dura el curso actual y 
# el mas rapido de otrod cursos 
# el mas lento de otros cursos 
# el promedio de optro cursos

curso_actual=1.5
curso_min=2.5
curso_promedio=4
curso_maximo=7

#diferencia con la duracion minima de otros cursos
diferencia_min= 100- (curso_actual/curso_min*100)    
print(f"diferencia con la duracion minima de otros cursos: {diferencia_min}")
#diferencia con la duracion promedio de ortrs cursos
diferencia_prom=100-(curso_actual/curso_promedio*100)
print(f"diferencia con la duracion promedio de ortrs cursos: {diferencia_prom}")
#diferencia con la duracion maxima de otros cursos
diferencia_maxima= 100- (curso_actual/curso_maximo*100)
print(f"diferencia con la duracion maxima de otros cursos{diferencia_maxima}")

#b) Porcentaje de material inservible que se reduce en ambos casos de los cursos si el crudo de este curso es de 3.5 hrs y se reedujo a 1.5 y el de los otros es en priomedio 5hr que se reducen a 4

material_inservible_otros_cursos= 100-((4/5)*100)
print(f"porcentaje del material inservible otros cursos: {material_inservible_otros_cursos}")
material_inservible_curso_actual=100-((1.5/3.5)*100)
print(f"material inservible curso actual: {material_inservible_curso_actual}")


#c) ver 10 hrs de este curso a cuiantas horas de otros cursos equivale?

horas_equivalentes=(4/1.5)*10
print(f"horas equivalentes de ver 10 heres del curso actual con otros cursos: {horas_equivalentes}")

print(f"horas equivalentes de ver 10 horas de otros cursos con curso actual: {1.5/4*10}")


