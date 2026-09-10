import sys
import json
from client import ThresholdBLSSignature

bls = ThresholdBLSSignature()

def handle_call(name, arguments):
    if name == "aggregate":
        shares = {int(k): v for k, v in arguments["shares"].items()}
        signers = [int(s) for s in arguments["signers"]]
        mod = arguments.get("modulus", 10007)
        return {"aggregated": bls.aggregate(shares, signers, mod)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
