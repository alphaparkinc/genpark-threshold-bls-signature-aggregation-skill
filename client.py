class ThresholdBLSSignature:
    """
    Threshold BLS Signature Aggregation.
    Combines signatures sigma_i from k-of-n signers using Lagrange interpolation.
    """
    def lagrange_coeff(self, signers, i, modulus=10007):
        num = 1
        den = 1
        for j in signers:
            if j != i:
                num = (num * (-j)) % modulus
                den = (den * (i - j)) % modulus
        return (num * pow(den, -1, modulus)) % modulus

    def aggregate(self, shares, signers, modulus=10007):
        agg_sig = 0
        for i in signers:
            coeff = self.lagrange_coeff(signers, i, modulus)
            agg_sig = (agg_sig + coeff * shares[i]) % modulus
        return agg_sig
