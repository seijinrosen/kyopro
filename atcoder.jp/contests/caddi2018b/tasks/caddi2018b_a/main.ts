import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const N = input();

  const ans = N.split("").filter((v) => v === "2").length;
  console.log(ans);
};

main();
