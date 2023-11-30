using System.Text.RegularExpressions;

internal class Part1
{
    private static Regex MoveRegex = new Regex(@"move\s([0-9]+)\sfrom\s([0-9]+)\sto\s([0-9]+)");

    internal static async Task ExecuteAsync()
    {
        var stacks = GenerateStacks();

        foreach (var line in await File.ReadAllLinesAsync("input.txt"))
        {
            var match = MoveRegex.Match(line);

            if (match.Success)
            {
                var move = new Move(int.Parse(match.Groups[1].Value), int.Parse(match.Groups[2].Value), int.Parse(match.Groups[3].Value));

                for (var i = 0; i < move.Number; i++)
                {
                    var c = stacks[move.From - 1].Pop();
                    stacks[move.To - 1].Push(c);
                }
            }
        }

        foreach (var s in stacks)
        {
            Console.Write(s.Peek());
        }

        Console.WriteLine();
    }

    private static Stack<char>[] GenerateStacks()
    {
        var stacks = new Stack<char>[9];

        stacks[0] = new Stack<char>();
        PushAll(stacks[0], "FTCLRPGQ");

        stacks[1] = new Stack<char>();
        PushAll(stacks[1], "NQHWRFSJ");

        stacks[2] = new Stack<char>();
        PushAll(stacks[2], "FBHWPMQ");

        stacks[3] = new Stack<char>();
        PushAll(stacks[3], "VSTDF");

        stacks[4] = new Stack<char>();
        PushAll(stacks[4], "QLDWVFZ");

        stacks[5] = new Stack<char>();
        PushAll(stacks[5], "ZCLS");

        stacks[6] = new Stack<char>();
        PushAll(stacks[6], "ZBMVDF");

        stacks[7] = new Stack<char>();
        PushAll(stacks[7], "TJB");

        stacks[8] = new Stack<char>();
        PushAll(stacks[8], "QNBGLSPH");

        return stacks;
    }

    private static void PushAll(Stack<char> stack, string v)
    {
        foreach (var c in v)
        {
            stack.Push(c);
        }
    }

    private record Move(int Number, int From, int To);
}