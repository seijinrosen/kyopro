import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

const X = input().split("").map(Number);
const [P, Q] = input().split(" ");

const user = new Map([
  ["o", 0],
  ["g", 1],
  ["u", 2],
]);
const permission = new Map([
  ["r", 4],
  ["w", 2],
  ["x", 1],
]);

const ans = X[user.get(P)!] & permission.get(Q)!;
print(yesNo(ans));
