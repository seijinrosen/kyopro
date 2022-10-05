import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);
const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);
const sumOfEachDigit = (i: number) => sum(i.toString().split("").map(Number));

// input functions -------------------------------------------------------------
const inputNumberArray = () => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const [N, A, B] = inputNumberArray();

  const ans = sum(
    range(1, N + 1).filter((i) => {
      const s = sumOfEachDigit(i);
      return A <= s && s <= B;
    })
  );

  print(ans);
};

main();
