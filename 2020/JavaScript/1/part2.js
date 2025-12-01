import { readFile } from 'fs/promises';

console.log('Loading input.txt...');
const contents = (await readFile('input.txt', 'utf8')).split('\n').map(line => line.trim());
console.log(`Loaded ${contents.length} lines`);

const target = 2020;
let found = false;
for (let i = 0; i < contents.length; i++) {
    const num1 = parseInt(contents[i]);
    for (let j = i + 1; j < contents.length; j++) {
        const num2 = parseInt(contents[j]);
        
        var firstSum = num1 + num2;
        if (firstSum > target) {
            continue;
        }
        
        for (let k = j + 1; k < contents.length; k++) {
            const num3 = parseInt(contents[k]);
            
            if (firstSum + num3 === target) {
                console.log(`Found numbers: ${num1}, ${num2}, and ${num3}`);
                console.log(`Product: ${num1 * num2 * num3}`);
                found = true;
                break;
            }
        }

        if (found) {
            break;
        }
    }
    if (found) {
        break;
    }
}