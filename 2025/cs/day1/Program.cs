const int DialSpace = 100;

var input = await File.ReadAllLinesAsync("input.txt");

var position = 50;
Console.WriteLine($"Initial Position: {position}");

var zeroCount = 0;
var passZeroCount = 0;
foreach (var line in input)
{
    (position, var crossZero) = Adjust(position, line);
    
    passZeroCount += crossZero;

    if (position == 0)
    {
        zeroCount++;
    }
}

Console.WriteLine($"Zero count: {zeroCount}");
Console.WriteLine($"Pass zero count: {passZeroCount + zeroCount}");

static (int, int) Adjust(int pos, string command)
{
    var left = command[0] switch
    {
        'L' => true,
        'R' => false,
        _ => throw new InvalidOperationException("Invalid command")
    };

    if (left && pos == 0)
    {
        pos = 100;
    }

    if (!int.TryParse(command[1..], out var increment))
    {
        throw new InvalidOperationException("Invalid increment");
    }

    var newPosition = left ? pos - increment : pos + increment;

    var crossZero = 0;
    while (newPosition < 0)
    {
        crossZero++;
        newPosition += DialSpace;
    }

    // > rather than >= to avoid counting landing on zero as crossing zero
    while (newPosition > DialSpace)
    {
        crossZero++;
        newPosition -= DialSpace;
    }

    // % is required despite the while loops to handle cases where newPosition == 100
    return (newPosition % DialSpace, crossZero);
}