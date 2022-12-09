def parse(command_str: str, loc: tuple[int,int], size):
    try:
        loc = (loc[0], size[1]-loc[1])
    except TypeError: pass


    command_str = command_str.replace("\n", "")

    command = command_str.split(" ")[0]
    args = command_str.split(" ")[1:]

    match command:
        case "G1":
            X = None
            Y = None

            for arg in args:
                if (arg.startswith("X")):
                    X = int(float(arg[1:]))
                elif (arg.startswith("Y")):
                    Y = int(float(arg[1:]))


            X = loc[0] if not X else X
            Y = loc[1] if not Y else Y

            return (X,  Y)

        case "G28":
            X = 0
            Y = 0

            return(X,Y)
    