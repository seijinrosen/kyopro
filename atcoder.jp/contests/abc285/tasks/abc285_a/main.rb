# frozen_string_literal: true

a, b = gets.split.map(&:to_i)

ans = a == b / 2

puts ans ? 'Yes' : 'No'
