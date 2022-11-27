import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [H1, M1, H2, M2, K] = input().split(" ").map(Number);

  const ans = 60 * (H2 - H1) + M2 - M1 - K;
  console.log(ans);
};

main();
