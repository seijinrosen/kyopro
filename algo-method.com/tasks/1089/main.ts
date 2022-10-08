import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const solve = (n: number): string => {
  const fizz = n % 4 === 0 ? "Fizz" : "";
  const buzz = n % 6 === 0 ? "Buzz" : "";
  return fizz + buzz || n.toString();
};

const main = () => {
  const N = +input();

  const ans = range(1, N + 1).map(solve);

  print(ans.join("\n"));
};

main();
