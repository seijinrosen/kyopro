# frozen_string_literal: true

require 'set'

def dedup(s = '')
  return s if s.size <= 1

  array = [s[0]]
  (1...s.size).each do |i|
    array.push(s[i]) if s[i - 1] != s[i]
  end
  array.join
end

N = gets.to_i
S = gets.chomp

ans = dedup(S).size

puts ans
