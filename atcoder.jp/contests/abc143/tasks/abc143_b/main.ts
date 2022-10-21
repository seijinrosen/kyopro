import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const combinations2 = <T>(array: T[]) => {
  const x = array.length - 2;
  const ret: [T, T][] = [];
  for (let i = 0; i < x + 1; i++)
    for (let j = i + 1; j < x + 2; j++) ret.push([array[i], array[j]]);
  return ret;
};
const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const main = () => {
  const N = +input();
  const D = input().split(" ").map(Number);

  const ans = sum(combinations2(D).map(([x, y]) => x * y));
  console.log(ans);
};

main();
