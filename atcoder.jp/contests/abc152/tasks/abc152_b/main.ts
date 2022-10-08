import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const main = () => {
  const [a, b] = input().split(" ");

  const ans = [a.repeat(+b), b.repeat(+a)].sort()[0];

  print(ans);
};

main();
