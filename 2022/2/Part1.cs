public static class Part1
{
    public async static Task ExecuteAsync()
    {
        var score = 0;
        foreach (var line in await File.ReadAllLinesAsync("input.txt"))
        {
            score += line switch
            {
                "A X" => 1 + 3,
                "A Y" => 2 + 6,
                "A Z" => 3 + 0,

                "B X" => 1 + 0,
                "B Y" => 2 + 3,
                "B Z" => 3 + 6,

                "C X" => 1 + 6,
                "C Y" => 2 + 0,
                "C Z" => 3 + 3,

                _ => 0
            };
        }

        Console.WriteLine(score);
    }
}
