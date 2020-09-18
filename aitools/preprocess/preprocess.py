from sklearn.preprocessing import StandardScaler


class StandardScalerTransformer:

    def __init__(self, df, cols):
        self.df = df.copy()
        self.transformed = False
        self.res = {}
        self.origin = {}
        for c in cols:
            self.res[c] = StandardScaler().fit(self.df[c].values.reshape(-1, 1))
        pass

    def transform(self):
        for c in self.res.keys():
            self.origin[c] = self.df[c].copy()
            self.df[c] = self.res[c].transform(self.df[c].values.reshape(-1, 1)).flatten()
        self.transformed = True
        return self.df

    def inverse_transform(self):
        if not self.transformed:
            raise Exception('must transform first')
        for c in self.res.keys():
            self.df[c] = self.origin[c]
        return self.df
