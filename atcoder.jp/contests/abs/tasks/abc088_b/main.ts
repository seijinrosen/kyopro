import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const sort = <T extends number | bigint>(array: T[], reverse = false) =>
  reverse
    ? array.slice().sort((a, b) => (a > b ? -1 : a < b ? 1 : 0))
    : array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

const step2 = <T>(array: T[]) => array.filter((_, i) => i % 2 === 0);

const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const tail = <T>(array: T[]) => array.slice(1);

// input functions -------------------------------------------------------------
const inputNumberArray = () => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const N = +input();
  const A = inputNumberArray();

  const sortedA = sort(A, true);
  const alice = sum(step2(sortedA));
  const bob = sum(step2(tail(sortedA)));
  const ans = alice - bob;

  print(ans);
};

main();
