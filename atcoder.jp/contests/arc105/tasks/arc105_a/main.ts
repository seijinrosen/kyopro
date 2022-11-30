import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sort = <T extends number | bigint>(array: T[], reverse = false) =>
  reverse
    ? array.slice().sort((a, b) => (a > b ? -1 : a < b ? 1 : 0))
    : array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

const main = () => {
  const ABCD = input().split(" ").map(Number);

  const [A, B, C, D] = sort(ABCD);
  const ans = A + B + C === D || A + D === B + C;

  console.log(ans ? "Yes" : "No");
};

main();
