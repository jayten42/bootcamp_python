if __name__ == '__main__':
    t = (3, 30, 2019, 9, 25)
    fmt = "{3:02d}/{4:02d}/{2} {0:02d}:{1:02d}"
    print(fmt.format(*t))
