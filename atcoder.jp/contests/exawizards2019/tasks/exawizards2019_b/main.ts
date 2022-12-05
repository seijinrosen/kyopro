import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const count: {
  (x: string, iterable: string): number;
  <T>(x: T, iterable: T[]): number;
} = <T>(x: string | T, iterable: string | T[]) =>
  typeof iterable === "string"
    ? iterable.split("").filter((a) => a === x).length
    : iterable.filter((a) => a === x).length;

const main = () => {
  input();
  const S = input();

  const ans = count("B", S) < count("R", S);
  console.log(ans ? "Yes" : "No");
};

main();
