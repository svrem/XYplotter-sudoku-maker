import cv2
import numpy as np
from parse_command import parse


def run_commands(commands, size, scale=2):

    img = np.zeros(size, np.uint8)
    img.fill(255)

    loc = None

    for command in commands:
        coords = parse(command, loc, size)
        try:
            coords = (coords[0], size[1]-coords[1])
        except TypeError: pass

        if (not loc):
            loc = coords
            continue


        img = cv2.line(img, loc, coords, 0, 1)
        loc = coords

        _img = cv2.circle(img.copy(), loc, 2, 122)
        _img = cv2.resize(_img, (0,0), fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)

        cv2.imshow("img", _img)
        cv2.waitKey(100)

    cv2.imshow("img", _img)

    cv2.waitKey(0)


