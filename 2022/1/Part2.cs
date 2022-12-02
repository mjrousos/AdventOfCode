using System;

public static class Part2
{
	public static int[] GetMaxCalories()
	{
        var largestInventory = 0;
        var secondLargestInventory = 0;
        var thirdLargestInventory = 0;
        var currentInventory = 0;

        foreach (var line in File.ReadAllLines("input.txt"))
        {
            if (string.IsNullOrEmpty(line))
            {
                if (currentInventory > largestInventory)
                    currentInventory = Interlocked.Exchange(ref largestInventory, currentInventory);

                if (currentInventory > secondLargestInventory)
                    currentInventory = Interlocked.Exchange(ref secondLargestInventory, currentInventory);

                if (currentInventory > thirdLargestInventory)
                    currentInventory = Interlocked.Exchange(ref thirdLargestInventory, currentInventory);

                currentInventory = 0;
            }
            else
            {
                currentInventory += int.Parse(line);
            }
        }

        if (currentInventory > largestInventory)
            currentInventory = Interlocked.Exchange(ref largestInventory, currentInventory);

        if (currentInventory > secondLargestInventory)
            currentInventory = Interlocked.Exchange(ref secondLargestInventory, currentInventory);

        if (currentInventory > thirdLargestInventory)
            currentInventory = Interlocked.Exchange(ref thirdLargestInventory, currentInventory);

        Console.WriteLine(largestInventory + secondLargestInventory + thirdLargestInventory);
        return new[] { largestInventory, secondLargestInventory, thirdLargestInventory };
    }
}
