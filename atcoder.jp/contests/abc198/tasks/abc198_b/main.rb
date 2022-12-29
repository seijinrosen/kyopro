# frozen_string_literal: true

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

N = String gets.chomp

ans = palindrome? rstrip(N, '0')
puts ans ? 'Yes' : 'No'
