import sys

def lerp(a,b,t):
    return (1-t)*a + t*b
# Linear Interpolation (or LERP) allows you to smoothly scale between two points (a and b) by providing a percentage (t). It essentially mixes numbers based on a sliding scale.
def get_relative_position(N,L,H):
    return (N - L)/(H - L)
# Relative position helps us determine where we are between two points (L and H)

def main():
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        N, L, H = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
        data = {}
        for _ in range(N):
            control_points = sys.stdin.readline().rstrip().split(" ")
            position = float(control_points[0])
            R, G, B = [int(x) for x in control_points[1:]]
            data[position] = (R, G, B)
        temperature = int(sys.stdin.readline().rstrip())
        temperature_position = get_relative_position(temperature, L, H)
        low_position = None
        high_position = None
        for position1, position2 in zip(list(data.keys()), list(data.keys())[1:]):
            # The zip function allows us to package two iterables together and returns an array of tuples that pairs them together. In this case, we are zipping together the temperature positions and the positions offset by 1. In effect, this is what happens:
            # [0.00, 0.25, 0.50, 0.75, 1.00] zips to -> [(0.00, 0.25), (0.25, 0.50), (0.50, 0.75), (0.75, 1.00)]
            # [0.25, 0.50, 0.75, 1.00]
            if temperature_position > position1 and temperature_position < position2: # between condition
                low_position, high_position = position1, position2
                break
        rgb_low = data[low_position]
        rgb_high = data[high_position]
        relative_color_position = get_relative_position(temperature_position, low_position, high_position) #Here, we need the relative position between two temperature positions since the colors are changing.

        colors = [str(int(lerp(color1, color2, relative_color_position))) for color1, color2 in zip(rgb_low, rgb_high)]
        print(' '.join(colors))

if __name__ == "__main__":
    main()