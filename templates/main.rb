# frozen_string_literal: true

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

def solve(a = 0, b = 0, c = 0)
  return compare(a.abs, b.abs) if c.even?

  compare(a, b)
end

# input
Y = gets.to_i
N = String gets.chomp
A, B, C = gets.split.map(&:to_i)

# main
ans = case day
      when 'Monday'
        5
      when 'Tuesday'
        4
      else
        0
      end

# output
p ans
puts (leap? Y) && 'YES' || 'NO'
puts ans ? 'Yes' : 'No'
puts solve(A, B, C)
