# frozen_string_literal: true

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

# input
Y = gets.to_i
N = String gets.chomp

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
