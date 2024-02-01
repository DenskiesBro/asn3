import a3q3 as asn3

# gcd_test_cases = [[49, 7], (8, 63), (250, 250), ()]

gcd_test_cases = [
    {
        "input": (63, 9),
        "expected": 9,
        "reason": "Testing a > b"
    },
    {
        "input": (7, 49),
        "expected": 7,
        "reason": "Testing a < b"
    },

    {
        "input": (250, 250),
        "expected": 250,
        "reason": "Testing a = b"

    },
]

for testcase in gcd_test_cases:
    inputs = testcase['input']
    expected = testcase['expected']
    result = asn3.gcd(inputs[0], inputs[1])
    if result == expected:
        print("it works")

    if result != expected:
        print('Error: returned', result,
              'when given', input,
              'Reason:', testcase['reason'])
