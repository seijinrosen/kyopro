# frozen_string_literal: true

require 'set'

# @return [Integer]
def input_int
  gets.to_i
end

def compare(x = 0, y = 0)
  return '<' if x < y
  return '>' if x > y

  '='
end

def leap?(year)
  return true if (year % 400).zero?
  return false if (year % 100).zero?

  (year % 4).zero?
end

def palindrome?(str = '')
  str.reverse == str
end

def rstrip(str = '', char = '')
  n = str.size
  (0...n).reverse_each do |i|
    break if str[i] != char

    n -= 1
  end
  str[0...n]
end

def weak2?(xs = [])
  return true if xs.size < 2

  x = xs[0]
  y = xs[1]
  (x + 1) % 10 == y && weak2?(xs[1..])
end

def solve(a = 0, b = 0, c = 0)
  return compare(a.abs, b.abs) if c.even?

  compare(a, b)
end

# input
N = gets.to_i
S = String gets.chomp
A = gets.split.map(&:to_i)
A, B, C = gets.split.map(&:to_i)
S = Array.new(N) { gets.chomp }
XS = gets.chomp.chars.map(&:to_i)

# main
# ans = case day
#       when 'Monday'
#         5
#       when 'Tuesday'
#         4
#       else
#         0
#       end
ans = Set.new(S).size

# output
p ans
puts (leap? Y) && 'YES' || 'NO'
puts ans ? 'Yes' : 'No'
puts solve(A, B, C)
