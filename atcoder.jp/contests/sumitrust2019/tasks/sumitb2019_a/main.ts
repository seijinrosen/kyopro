import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [M1, D1] = input().split(" ").map(Number);
  const [M2, D2] = input().split(" ").map(Number);

  const ans = M2 - M1;
  console.log(ans);
};

main();
