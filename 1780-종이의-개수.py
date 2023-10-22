import sys


counter = {
    '-1': 0,
    '0': 0,
    '1': 0,
}

grid: list[list[int]]


def solve(y0: int, x0: int, n: int):
    # 행렬 grid에서 (y0, x0) 좌표를 좌상단으로 갖는 n x n 크기의 부분행렬에 대하여
    # 1. 모든 원소가 동일한 값을 가지면, 카운터에 해당 원소로 이루어진 부분행렬의 갯수를 1 증가
    # 2. 모든 원소가 동일한 값을 갖지 않으면, 이 부분행렬을 같은 크기의 종이 9개로 자르고, 각 부분행렬에 대하여 재귀적으로 풀이
    if is_consists_of_same_value(y0, x0, n):
        # 동일한 값을 갖는지 검사한다. (degenerate case)
        counter[grid[y0][x0]] += 1
    else:
        # divide and conquor
        for y in range(y0, y0+n, n//3):
            for x in range(x0, x0+n, n//3):
                solve(y, x, n//3)


def is_consists_of_same_value(y0: int, x0: int, n: int) -> bool:
    for y in range(y0, y0+n):
        for x in range(x0, x0+n):
            if grid[y][x] != grid[y0][x0]:
                return False
    return True


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    grid = [sys.stdin.readline().strip().split() for n in range(N)]
    solve(0, 0, N)
    print(counter['-1'])
    print(counter['0'])
    print(counter['1'])
