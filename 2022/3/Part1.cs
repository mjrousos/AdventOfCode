using System.Text.RegularExpressions;

internal class Part1
{
    private static int count;
    private static Regex RangesRegex = new Regex(@"([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)");

    internal async static Task ExecuteAsync()
    {
        count = 0;
        foreach (var line in await File.ReadAllLinesAsync("input.txt"))
        {
            if (FullyContained(line))
            {
                count++;
            }
        }

        Console.WriteLine(count);
    }

    private static bool FullyContained(string line)
    {
        var match = RangesRegex.Match(line);
        if (match.Success)
        {
            var firstRange = new Range(int.Parse(match.Groups[1].Value), int.Parse(match.Groups[2].Value));
            var secondRange = new Range(int.Parse(match.Groups[3].Value), int.Parse(match.Groups[4].Value));


            return Contains(firstRange, secondRange) || Contains(secondRange, firstRange);
        }

        throw new InvalidOperationException($"Should not be here! Bad input: {line}");
    }

    private static bool Contains(Range r1, Range r2) =>
        r1.Start >= r2.Start && r1.End <= r2.End;

    private record Range(int Start, int End);
}