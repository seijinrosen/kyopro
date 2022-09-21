import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const yesNo = (b: boolean) => (b ? "Yes" : "No");

const [A, M] = input().split(" ").map(Number);

const ans = (A & M) === M;
print(yesNo(ans));
