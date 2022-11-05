import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const S = input();

  const i = S.lastIndexOf("a");
  const ans = i === -1 ? -1 : i + 1;

  console.log(ans);
};

main();
