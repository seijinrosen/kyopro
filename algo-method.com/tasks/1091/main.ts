import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

const isLeapYear = (n: number): boolean => {
  if (n % 400 === 0) return true;
  if (n % 100 === 0) return false;
  if (n % 4 === 0) return true;
  return false;
};

const main = () => {
  const N = +input();

  const ans = isLeapYear(N);

  print(yesNo(ans));
};

main();
