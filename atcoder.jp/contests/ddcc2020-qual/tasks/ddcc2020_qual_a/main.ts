import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const prize = (n: number) =>
  new Map([
    [3, 100000],
    [2, 200000],
    [1, 300000],
  ]).get(n) || 0;

const additionalPrize = (x: number, y: number) =>
  x === 1 && y === 1 ? 400000 : 0;

const main = () => {
  const [X, Y] = input().split(" ").map(Number);

  const ans = prize(X) + prize(Y) + additionalPrize(X, Y);
  console.log(ans);
};

main();
