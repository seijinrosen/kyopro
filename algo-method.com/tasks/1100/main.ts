import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sort = <T extends number | bigint>(array: T[], reverse = false) =>
  reverse
    ? array.slice().sort((a, b) => (a > b ? -1 : a < b ? 1 : 0))
    : array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

const main = () => {
  const N = +input();
  const A = input().split(" ").map(Number);

  const ans = sort(A)[N - 2];
  console.log(ans);
};

main();
