from visualizer import run_commands
from solver import generate_sudoku

def draw_puzzle(start_delta,tile_size,visualize=False):
    puzzle = generate_sudoku(0.5)

    numbers = [
        None,
        [[0,0], [0.5,0], [0.5, 0.8]],
        [[0,0],[0.8,0], [0.8, 0.2], [0.2,0.2],[0.2, 0.5], [0.8, 0.5], [0.8,0.8], [0.2, 0.8]],
        [[0,0], [0.2,0], [0.2,0.2], [0.8, 0.2], [0.8, 0.5], [0.3, 0.5], [0.8, 0.5], [0.8, 0.8], [0.2,0.8]],
        [[0,0], [0.6,0], [0.6, 0.8], [0.6, 0.5], [0.2,0.5], [0.2,0.8]],
        [[0,0], [0.2 ,0], [0.2, 0.2], [0.8, 0.2], [0.8, 0.5], [0.2, 0.5], [0.2, 0.8], [0.8, 0.8]],
        [[0,0], [0.2, 0], [0.2, 0.2], [0.8, 0.2], [0.8, 0.5], [0.2, 0.5], [0.2, 0.2], [0.2, 0.8], [0.8, 0.8]],
        [[0,0],[0.4, 0], [0.8, 0.8], [0.2, 0.8]],
        [[0,0], [0.8, 0], [0.8, 0.2], [0.2, 0.2], [0.2, 0.5], [0.8,0.5], [0.8, 0.2], [0.8,0.8], [0.2,0.8], [0.2, 0.5], [0.8,0.5]],
        [[0,0], [0.2, 0], [0.2,0.2], [0.8,0.2], [0.8, 0.8], [0.2,0.8], [0.2, 0.5], [0.8, 0.5]]

    ]


    top = tile_size*9

    commands = ["G28", f"G1 X{start_delta} Y{start_delta}"]

    def move_to_coords(x=None,y=None):
        if x is not None and y is not None:
            commands.append(f"G1 X{x+start_delta} Y{y+start_delta}")
        elif y is None:
            commands.append(f"G1 X{x+start_delta}")
        elif x is None:
            commands.append(f"G1 Y{y+start_delta}")

    
    def gen_grid():   
        for x in range(0,9,2):
            move_to_coords(x*tile_size, top)
            move_to_coords((x+1)*tile_size, top)
            move_to_coords((x+1)*tile_size, 0)
            move_to_coords((x+2)*tile_size, 0)

        del commands[-1]

        move_to_coords(0,0)


        for y in range(0,9,2):
            move_to_coords(top, y*tile_size)
            move_to_coords(top, (y+1)*tile_size)
            move_to_coords(0, (y+1)*tile_size)
            move_to_coords(0,(y+2)*tile_size)

        del commands[-1]



    def go_to_tile(x,y):
        move_to_coords(x*tile_size)
        move_to_coords(y=y*tile_size)

        return (x*tile_size, y*tile_size)
    
    def draw_number(number, curr_loc):
        ops = numbers[number]
    
        for op in ops:
            move_to_coords(curr_loc[0]+tile_size*op[0],curr_loc[1]+tile_size*op[1])

        for op in reversed(ops):
            move_to_coords(curr_loc[0]+tile_size*op[0],curr_loc[1]+tile_size*op[1])

            # commands.append(f"G1 X{curr_loc[0]+tile_size*op[0]+start_delta} Y{curr_loc[1]+tile_size*op[0]+start_delta}")

    for row in puzzle:
        print(row)
    gen_grid()


    for i in range(9):
        for j in range(9):
            digit = puzzle[8-j][i]
            if (digit == 0): continue

            loc = go_to_tile(i,j)
            draw_number(digit, loc)



    open("output.cnc", "w").write("\n".join(commands))
    if (visualize):
        run_commands(commands, (300,300), 2)

if __name__ == "__main__":
    draw_puzzle(10, 10, True)

