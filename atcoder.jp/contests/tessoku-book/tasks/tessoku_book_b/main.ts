import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

const inputNumberArray = (): number[] => input().split(" ").map(Number);

const [N, X] = inputNumberArray();
const A = inputNumberArray();

const ans = A.includes(X);
print(yesNo(ans));
