import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const main = () => {
  const N = +input();
  const ST = [...Array(N)].map(() =>
    (([s, t]) => [s, +t] as [string, number])(input().split(" "))
  );
  const X = input();

  const i = ST.findIndex(([s]) => s === X);
  const ans = sum(ST.slice(i + 1).map(([, t]) => t));

  console.log(ans);
};

main();
