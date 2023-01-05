# frozen_string_literal: true

require 'set'

def weak1?(xs = [])
  Set.new(xs).size == 1
end

def weak2?(xs = [])
  return true if xs.size < 2

  x = xs[0]
  y = xs[1]
  (x + 1) % 10 == y && weak2?(xs[1..])
end

XS = gets.chomp.chars.map(&:to_i)

is_weak = weak1?(XS) || weak2?(XS)

puts is_weak ? 'Weak' : 'Strong'
