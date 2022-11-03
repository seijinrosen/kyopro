import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [X, Y] = input().split(" ").map(Number);

  const ans = [...Array(X + 1)].some((_, crane) => 2 * crane === 4 * X - Y);

  console.log(ans ? "Yes" : "No");
};

main();
