import numpy as np

class HMM:
    def __init__(self, observed, transition_matrix, emission_matrix, initial_distribution):
        self.I = initial_distribution
        self.V = np.array(observed)
        self.A = np.array(transition_matrix)
        self.B = np.array(emission_matrix)

        self.K = self.A.shape[0]
        self.N = self.V.shape[0]


    def forward(self):
        alpha = np.zeros((self.N, self.K))
        # TODO: calculate forward values
        alpha[0, :] = self.I * self.B[:, self.V[0]]

        for i in range(1, self.V.shape[0]):
            for j in range(self.A.shape[0]):
                alpha[i, j] = alpha[i-1].dot(self.A[:, j]) * self.B[j, self.V[i]]

        return np.argmax(alpha, axis=1), alpha

    def backward(self):
        beta = np.zeros((self.N, self.K))
        # TODO: calculate backward values
        beta[self.V.shape[0] - 1] = np.ones((self.A.shape[0]))

        for t in range(self.V.shape[0] - 2, -1, -1):
            for j in range(self.A.shape[0]):
                beta[t, j] = (beta[t + 1] * self.B[:, self.V[t + 1]]).dot(self.A[j, :])

        return np.argmax(beta, axis=1), beta

    def forward_backward(self):
        fbv = np.zeros((self.N, self.K))
        # TODO: calculate forward-backward values


        return np.argmax(fbv, axis=1)

    def viterbi(self):
        T1 = np.empty((self.N, self.K))
        T2 = np.empty((self.N - 1, self.K))

        T1[0, :] = np.log(self.I * self.B[:, self.V[0]])

        for t in range(1, self.N):
            for j in range(self.K):
                T2[t - 1, j] = np.argmax(T1[t - 1] + np.log(self.A[:, j]) + np.log(self.B[j, self.V[t]]))
                T1[t, j] = np.max(T1[t - 1] + np.log(self.A[:, j]) + np.log(self.B[j, self.V[t]]))

        viterbi = np.zeros(self.N)

        last_state = np.argmax(T1[self.N - 1, :])

        viterbi[0] = last_state

        backtrack_index = 1
        for i in range(self.N - 2, -1, -1):
            viterbi[backtrack_index] = T2[i, int(last_state)]
            last_state = T2[i, int(last_state)]
            backtrack_index += 1

        viterbi = np.flip(viterbi, axis=0)

        return viterbi





