def z(n: int, r: int, c: int, y: int = 0, x: int = 0, offset: int = 0):
    # 2차원 이진탐색과 비슷하다.
    # r, c  : z모양으로 방문 할 순서를 구해야 하는 좌표
    # n     : (지금 보고있는) 부분행렬의 크기 (2^{n} x 2^{n})의 지수.
    # y, x  : (지금 보고있는) 부분행렬의 좌상단 위치
    # order : (y, x) 의 방문 순서
    if r == y and c == x:
        return offset
    else:
        step = 1 << (n-1) # 2^{n-1}
        skip = 0 # 건너 뛴 2^{n-1} x 2^{n-1} 크기의 부분행렬 개수
        ny = y
        nx = x
        if c >= x+step:
            skip += 1
            nx += step
        if r >= y+step:
            skip += 2
            ny += step
        return z(n-1, r, c, ny, nx, offset + (step * step) * skip)



if __name__ == '__main__':
    N, r, c = map(int, input().split())
    print(z(N, r, c))
