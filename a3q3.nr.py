import a3q3 as asn3

nr_test_cases = [
    {
        "input": 64,
        "expected": 8.00000000000017,
        "reason": "Testing a > b"
    },

    {
        "input": 0.5,
        "expected": 0.7071078431372548,
        "reason": "Testing a < b"
    },

    {
        "input": 0,
        "expected": 0.001953125,
        "reason": "Testing a = b"

    },

    {
        "input": 1,
        "expected": 1,
        "reason": "Testing a = b"
    }
]

for testcase in nr_test_cases:
    inputs = testcase['input']
    expected = testcase['expected']
    result = asn3.newtonraphson(inputs)

    if result != expected:
        print('Error: returned', result,
              'when given', input,
              'Reason:', testcase['reason'])
