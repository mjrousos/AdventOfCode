using System;

public static class Part1
{
	public static int GetMaxCalories()
	{
        var largestInventory = 0;
        var currentInventory = 0;

        foreach (var line in File.ReadAllLines("input.txt"))
        {
            if (string.IsNullOrEmpty(line))
            {
                if (currentInventory > largestInventory)
                {
                    largestInventory = currentInventory;
                    currentInventory = 0;
                }
            }
            else
            {
                currentInventory += int.Parse(line);
            }
        }

        if (currentInventory > largestInventory)
        {
            largestInventory = currentInventory;
        }

        Console.WriteLine(largestInventory);

        return largestInventory;
    }
}
