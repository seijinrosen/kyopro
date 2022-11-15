import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const S = input();

  const ans = S.slice(0, 3);
  console.log(ans);
};

main();
