from math import sqrt


class TinyStatistician:
    @staticmethod
    def mean(x):
        if not x:
            return None
        return float(sum(x) / len(x))

    @staticmethod
    def median(x):
        if not x:
            return None
        return float(sorted(x)[int(len(x)/2)])

    @staticmethod
    def quartile(x, percentile):
        if not x:
            return None
        idx = int(len(x) * percentile / 100)
        return float(sorted(x)[idx])

    @staticmethod
    def var(x):
        if not x:
            return None
        mean = TinyStatistician.mean(x)
        return float(sum(pow(v - mean, 2) for v in x) / len(x))

    @staticmethod
    def std(x):
        if not x:
            return None
        var = TinyStatistician.var(x)
        return float(sqrt(var))


if __name__ == '__main__':
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    print(tstat.median(a))
    print(tstat.quartile(a, 25))
    print(tstat.quartile(a, 75))
    print(tstat.var(a))
    print(tstat.std(a))
