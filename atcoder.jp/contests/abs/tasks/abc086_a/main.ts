import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const isOdd = (n: number): boolean => n % 2 === 1;

const inputNumberArray = (): number[] => input().split(" ").map(Number);

const main = () => {
  const [A, B] = inputNumberArray();

  const ans = isOdd(A * B) ? "Odd" : "Even";
  print(ans);
};

main();
