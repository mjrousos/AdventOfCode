public static class Part2
{
    public async static Task ExecuteAsync()
    {
        var score = 0;
        foreach (var line in await File.ReadAllLinesAsync("input.txt"))
        {
            score += line switch
            {
                "A X" => 3 + 0,
                "A Y" => 1 + 3,
                "A Z" => 2 + 6,

                "B X" => 1 + 0,
                "B Y" => 2 + 3,
                "B Z" => 3 + 6,

                "C X" => 2 + 0,
                "C Y" => 3 + 3,
                "C Z" => 1 + 6,

                _ => 0
            };
        }

        Console.WriteLine(score);
    }
}
