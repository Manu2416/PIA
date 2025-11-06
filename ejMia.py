
C1 = "Problema de Alimentación Eléctrica"
C2 = "Reponer Consumibles (Tóner/Cartucho)"
C3 = "Reponer Consumibles (Papel)"
C4 = "Solucionar Problema de Software/Cola"
C5 = "Solucionar Atasco Físico"
C6 = "Fallo Genérico de Hardware/Mecánico"
C7 = "Funcionamiento Normal (Imprimiendo o en Espera)"


def comprobar_resultados(p1, p2, p3, p4, p5, p6):
    
    if p1 == False:
        return C1

    
    if p1 == True and p2 == True:
        return C5

   
    if p1 == True and p3 == False and p2 == False:
        return C3

   
    if p1 == True and p4 == True and p3 == True:
        return C2

    
    if p1 == True and p4 == True and p3 == False:
        return f"{C2} — prioridad sobre papel si indicador tóner crítico"

    
    if p1 == True and p4 == False and p5 == True:
        return C4

    
    if p1 == True and p4 == False and p5 == False and p6 == True and p2 == False:
        return C6


    if (
        p1 == True and
        p3 == True and
        p4 == False and
        p5 == False and
        p6 == False and
        p2 == False
    ):
        return C7

    if p1 == True and p2 == True and p6 == True:
        return f"{C5} (con posible daño)"
    
    if p1 == True and p3 == False and p5 == True:
        return f"{C3} y {C4} (preferencia: reponer papel primero)"

    return "Sin diagnóstico claro — revisar manualmente."



resultado = comprobar_resultados(
    p1=True, 
    p2=False,  
    p3=False,   
    p4=False, 
    p5=False, 
    p6=True 
)

print(resultado)
