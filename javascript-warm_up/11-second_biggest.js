#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
    console.log(0);
} else {
    const integers = args.map(arg => parseInt(arg));
    const maxNumber = Math.max(...integers);
    const filteredIntegers = integers.filter(num => num !== maxNumber);
    const secondMaxNumber = Math.max(...filteredIntegers);

    console.log(secondMaxNumber);
}
