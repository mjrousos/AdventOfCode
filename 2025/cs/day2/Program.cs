using System.Text.RegularExpressions;

public partial class Day2
{
    [GeneratedRegex(@"^(\d+)\1$")]
    private static partial Regex GetDuplicatedRegex();

    [GeneratedRegex(@"^(\d+)\1+$")]
    private static partial Regex GetRepeatedDigitsRegex();

    public static void Main()
    {
        var dupTotal = 0L;
        var repeatedTotal = 0L;

        var duplicatedDigitsRegex = GetDuplicatedRegex();
        var repeatedDigitsRegex = GetRepeatedDigitsRegex();

        var inputs = File.ReadAllText("input.txt").Trim().Split(',');
        foreach (var input in inputs)
        {
            Console.WriteLine($"Processing input: {input}");
            var ends = input.Split('-', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries).Select(long.Parse).ToArray();

            if (ends.Length == 1)
            {
                if (repeatedDigitsRegex.IsMatch(ends[0].ToString()))
                {
                    Console.WriteLine($"Found repeated ID: {ends[0]}");
                    repeatedTotal += ends[0];
                }

                if (duplicatedDigitsRegex.IsMatch(ends[0].ToString()))
                {
                    Console.WriteLine($"Found duplicated ID: {ends[0]}");
                    dupTotal += ends[0];
                }
            }
            else if (ends.Length == 2)
            {
                for (var i = ends[0]; i <= ends[1]; i++)
                {
                    if (repeatedDigitsRegex.IsMatch(i.ToString()))
                    {
                        Console.WriteLine($"Found repeated ID: {i}");
                        repeatedTotal += i;
                    }

                    if (duplicatedDigitsRegex.IsMatch(i.ToString()))
                    {
                        Console.WriteLine($"Found duplicated ID: {i}");
                        dupTotal += i;
                    }
                }
            }
            else
            {
                throw new InvalidOperationException("Invalid input range.");
            }
        }

        Console.WriteLine($"Total duplicated IDs sum: {dupTotal}");
        Console.WriteLine($"Total repeated IDs sum: {repeatedTotal}");
    }
}