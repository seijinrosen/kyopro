# frozen_string_literal: true

require 'set'

N = gets.to_i
S = Array.new(N) { gets.chomp }

S.reverse.each do |s|
  puts s
end
