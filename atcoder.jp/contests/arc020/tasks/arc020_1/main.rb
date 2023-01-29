# frozen_string_literal: true

A, B = gets.split.map(&:to_i)

if A.abs < B.abs
  puts 'Ant'
elsif A.abs == B.abs
  puts 'Draw'
else
  puts 'Bug'
end
