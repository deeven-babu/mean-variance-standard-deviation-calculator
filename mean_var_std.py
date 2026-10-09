import numpy as np


def calculate(values):
    if len(values) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        n = np.array([values])
        reshaped = np.reshape(n, (3,3))
        mean = np.mean(reshaped).item()
        mean0 = np.mean(reshaped,axis=0).tolist()
        mean1 = np.mean(reshaped,axis=1).tolist()
        std = np.std(reshaped).item()
        std0 = np.std(reshaped,axis=0).tolist()
        std1 = np.std(reshaped,axis=1).tolist()
        var = np.var(reshaped).item()
        vara0 = np.var(reshaped,axis=0).tolist()
        vara1 = np.var(reshaped,axis=1).tolist()
        maxi = np.max(reshaped).item()
        maxi0 = np.max(reshaped,axis=0).tolist()
        maxi1 = np.max(reshaped,axis=1).tolist()
        mini = np.min(reshaped).item()
        mini0 = np.min(reshaped,axis=0).tolist()
        mini1 = np.min(reshaped,axis=1).tolist()
        summ = np.sum(reshaped).item()
        suma0 = np.sum(reshaped,axis=0).tolist()
        suma1 = np.sum(reshaped,axis=1).tolist()
        dicts = {
            "mean":[mean1,mean0,mean],
            "standard deviation":[std1,std0,std],
            "variance":[vara1,vara0,var],
            "max":[maxi1,maxi0,maxi],
            "min":[mini1,mini0,mini],
            "sum":[suma1,suma0,summ],
        }
        return dicts


if __name__ == "__main__":
    values = list(map(int, input("enter numbers").split()))
    print(calculate(values))
