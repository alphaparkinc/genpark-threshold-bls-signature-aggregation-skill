from client import ThresholdBLSSignature

def main():
    print("=== Testing Threshold BLS Signature Aggregation ===")
    bls = ThresholdBLSSignature()

    # Secret = 88. Polynomial f(x) = 88 + 3x mod 10007.
    # Signer 1: 91, Signer 2: 94
    shares = {1: 91, 2: 94}
    aggregated = bls.aggregate(shares, [1, 2], modulus=10007)

    print("Aggregated signature / reconstructed secret:", aggregated)
    assert aggregated == 88
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
