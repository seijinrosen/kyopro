import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const combinations3 = <T>(array: T[]): [T, T, T][] => {
  const n = array.length;
  const ret: [T, T, T][] = [];
  for (let i = 0; i < n - 2; i++)
    for (let j = i + 1; j < n - 1; j++)
      for (let k = j + 1; k < n; k++) ret.push([array[i], array[j], array[k]]);
  return ret;
};
const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

// input functions -------------------------------------------------------------
const inputNumberArray = (): number[] => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const N = +input();
  const A = inputNumberArray();

  const ans = combinations3(A).some(([a, b, c]) => a + b + c === 1000);
  print(yesNo(ans));
};

main();
