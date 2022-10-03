import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const zip: {
  (a: string, b: string): [string, string][];
  <B>(a: string, b: B[]): [string, B][];
  <A>(a: A[], b: string): [A, string][];
  <A, B>(a: A[], b: B[]): [A, B][];
} = <A, B>(a: string | A[], b: string | B[]) =>
  typeof a === "string" && typeof b === "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [string, string]
      )
    : typeof a === "string" && typeof b !== "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [string, B]
      )
    : typeof a !== "string" && typeof b === "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [A, string]
      )
    : [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [A, B]
      );

const main = () => {
  const S = input();
  const T = input();

  const ans = zip(S, T).filter(([s, t]) => s !== t).length;
  print(ans);
};

main();
