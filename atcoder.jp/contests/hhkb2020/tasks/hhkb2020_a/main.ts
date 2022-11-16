import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const S = input();
  const T = input();

  const ans = S === "Y" ? T.toUpperCase() : T;
  console.log(ans);
};

main();
