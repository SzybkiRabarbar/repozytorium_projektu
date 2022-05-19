from timer_decorator import timer

def generate_pascal_triangle(layers:int)->list:
    triangle = [[1],[1,1]]
    for i in range(2,layers):
        temp = [(triangle[-1][indx]+triangle[-1][indx-1]) for indx in range(1,i)]
        temp.insert(0,1)
        temp.append(1)
        triangle.append(temp)
    return triangle

def draw_triangle_in_term(layers:int):
    pascal_triangle = generate_pascal_triangle(layers)
    for l in pascal_triangle:
        print(f"{' '*(layers)}{l}")
        layers-=1
        
@timer
def main(layers):
    draw_triangle_in_term(layers)

if __name__ == '__main__':
    main(100)