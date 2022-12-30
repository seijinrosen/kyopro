# frozen_string_literal: true

def compare(x = 0, y = 0)
  return '<' if x < y
  return '>' if x > y

  '='
end

def solve(a = 0, b = 0, c = 0)
  return compare(a.abs, b.abs) if c.even?

  compare(a, b)
end

A, B, C = gets.split.map(&:to_i)
puts solve(A, B, C)
