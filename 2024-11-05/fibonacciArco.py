import turtle

def desenhar_quadrado_com_arco(L):
    for _ in range(4):
        turtle.forward(L)
        turtle.left(90)
    if L != 0:
        turtle.circle(L, 90)

def sequencia_fibonacci(n):
    sequencia = []

    for i in range(n):
        if i in [0, 1]:
            sequencia.append(i)
            continue
        
        sequencia.append(sequencia[i - 1] + sequencia[i - 2])
    
    return sequencia

def desenhar_espiral_fibonacci(n):
    for num in sequencia_fibonacci(n):
        desenhar_quadrado_com_arco(num)
    
    turtle.exitonclick()

desenhar_espiral_fibonacci(19)