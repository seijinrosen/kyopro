import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const bin2int = (b: string) => parseInt(b, 2);

const main = () => {
  const N = input();

  const ans = bin2int(N);

  print(ans);
};

main();
