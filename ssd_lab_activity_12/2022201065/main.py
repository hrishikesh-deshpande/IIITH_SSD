
def q1():
    with open('Readings for 42x25 mat.txt') as f:
        last_i, last_j, stride, last_sec, stepTime = -1, -1, 0.0, 0.0, 0.0

        def readMat():
            firstline = f.readline().split()

            timestring = firstline[0]
            timestampsec = 0.0

            for i in timestring.split(':'):
                timestampsec = timestampsec * 60 + float(i)

            mat = [[*map(int, firstline[1:])]]

            for _ in range(41):
                mat.append([*map(int, f.readline().split()[1:])])
                pass

            wt = 0
            wtd_i = 0
            wtd_j = 0
            for i in range(42):
                for j in range(25):
                    wt += mat[i][j]
                    wtd_i += mat[i][j]*i
                    wtd_j += mat[i][j]*j
                    pass
                pass
            return wtd_i/(wt or 1), wtd_j/(wt or 1), wt, timestampsec

        for _ in range(20):
            i, j, w, t = readMat()
            if(w):
                # print(i, j, w)
                if(last_i == -1):
                    # print('detected first step')
                    last_i = i
                    last_j = j
                    last_sec = t
                    # print(i, j, t)

                elif(abs(last_j - j) < 2 and abs(last_i - i) > 4):
                    # print('detected second step')
                    stride = abs(last_i - i)
                    stepTime = abs(last_sec - t)
                    break

            f.readlines(2)

        print('The values for question 1 are')
        print('stride', stride, 'units',
              #   '\nstepTime', stepTime,
              'seconds\nvelocity', stride/stepTime, 'units per seconds',
              '\ncadence', 180/stepTime)


def q2():
    with open('Readings for 42x25 mat.txt') as f:
        last_i, last_j, stride, last_sec, stepTime = -1, -1, 0.0, 0.0, 0.0

        def readMat():
            firstline = f.readline().split()

            if(firstline == []):
                return 0, 0, 0, 0

            timestring = firstline[0]
            timestampsec = 0.0

            for i in timestring.split(':'):
                timestampsec = timestampsec * 60 + float(i)

            mat = [[*map(int, firstline[1:])]]

            for _ in range(41):
                mat.append([*map(int, f.readline().split()[1:])])
                pass

            f.readlines(2)
            firstline = f.readline().split()

            if(firstline != []):
                mat.append([*map(int, firstline[1:])])
                for _ in range(41):
                    mat.append([*map(int, f.readline().split()[1:])])
                    pass
                f.readlines(2)

            firstline = f.readline().split()

            if(firstline != []):
                mat.append([*map(int, firstline[1:])])

                for _ in range(41):
                    mat.append([*map(int, f.readline().split()[1:])])
                    pass
                f.readlines(2)

            wt = 0
            wtd_i = 0
            wtd_j = 0
            # print(mat)
            for i in range(len(mat)):
                for j in range(25):
                    wt += mat[i][j]
                    wtd_i += mat[i][j]*i
                    wtd_j += mat[i][j]*j
                    pass
                pass
            return wtd_i/(wt or 1), wtd_j/(wt or 1), wt, timestampsec

        for _ in range(7):
            i, j, w, t = readMat()
            if(w):
                # print(i, j, w)
                if(last_i == -1):
                    # print('detected first step')
                    last_i = i
                    last_j = j
                    last_sec = t
                    # print(i, j, t)

                elif(abs(last_j - j) < 2 and abs(last_i - i) > 4):
                    # print('detected second step')
                    stride = abs(last_i - i)
                    stepTime = abs(last_sec - t)
                    break

            # f.readlines(2)

        print('\nThe values for question 2 are')
        print('stride', stride, 'units',
              #   '\nstepTime', stepTime,
              'seconds\nvelocity', stride/stepTime, 'units per seconds',
              '\ncadence', 180/stepTime)


q1()
q2()
