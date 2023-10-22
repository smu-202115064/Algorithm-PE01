import sys


unused_cube_counts: list[int]
used_cube_count: int
X: int
Y: int
Z: int


def fill_box(i: int, x: int = 0, y: int = 0, z: int = 0) -> int:
    global used_cube_count
    size = 1 << i
    if x >= X or y >= Y or z >= Z:
        # 만약 박스의 크기를 벗어났다면 탐색하지 않음.
        return
    elif unused_cube_counts[i] > 0 and (x+size) <= X and (y+size) <= Y and (z+size) <= Z:
        # 지금 보고있는 부분공간이 상자 안에 있고,
        # 부분 공간을 채울 수 있는 큐브가 존재한다면 채운다
        # (한 변의 길이가 2^{i}인 큐브)
        unused_cube_counts[i] -= 1
        used_cube_count += 1
        return
    elif i == 0:
        # 1x1x1 크기를 채울 큐브가 없어 여기까지 왔다면
        # 이 상자는 채울 수 없는 상자인 것이다.
        raise ValueError()
    else:
        # 3차원 공간의 중심을 기준으로
        # 8개의 부분공간으로 쪼개어 분할 정복
        i -= 1
        size = 1 << i
        fill_box(i, x, y, z)
        fill_box(i, x, y, z+size)
        fill_box(i, x, y+size, z)
        fill_box(i, x, y+size, z+size)
        fill_box(i, x+size, y, z)
        fill_box(i, x+size, y, z+size)
        fill_box(i, x+size, y+size, z)
        fill_box(i, x+size, y+size, z+size)


if __name__ == '__main__':
    MAX_N = 20

    unused_cube_counts = [0] * (1 << MAX_N)
    used_cube_count = 0

    X, Y, Z = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())

    for i in range(N):
        unused_cube_counts[i] = int(sys.stdin.readline().split()[1])

    try:
        fill_box(MAX_N)
    except ValueError:
        used_cube_count = -1
    finally:
        print(used_cube_count)
