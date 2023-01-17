# frozen_string_literal: true

require 'set'

N, K = gets.split.map(&:to_i)

st = Set.new

K.times do
  _d = gets.to_i
  as = gets.split.map(&:to_i)

  as.each do |a|
    st.add(a)
  end
end

ans = N - st.size
p ans
